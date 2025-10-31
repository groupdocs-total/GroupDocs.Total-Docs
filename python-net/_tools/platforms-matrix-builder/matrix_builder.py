import json
import sys
import argparse
import urllib.request
import urllib.error
from typing import Dict, List, Set, Tuple


PYPI_JSON_URL = "https://pypi.org/pypi/{package}/json"
TICK_MARKDOWN = "![(tick)](/total/python-net/_images/check-blue.png)"


class PypiClient:
    """Minimal PyPI JSON client using urllib to avoid external deps."""

    def fetch_project(self, package_name: str) -> Dict:
        url = PYPI_JSON_URL.format(package=package_name)
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read().decode("utf-8")
                return json.loads(data)
        except urllib.error.HTTPError as http_err:
            raise RuntimeError(f"Failed to fetch {package_name} from PyPI: HTTP {http_err.code}") from http_err
        except urllib.error.URLError as url_err:
            raise RuntimeError(f"Network error while fetching {package_name} from PyPI: {url_err.reason}") from url_err


def parse_requires_dist(require_lines: List[str]) -> List[Tuple[str, str]]:
    """
    Parse requires_dist entries from PyPI metadata.

    Supports common PEP 508 forms, including:
    - "pkg-name (==1.2.3)"
    - "pkg-name==1.2.3"
    - With extras: "pkg-name[extra]==1.2.3"
    - With environment markers: "; python_version>='3.8'" (ignored)

    Returns list of tuples: (package_name, exact_version_or_empty)
    If exact version (==X.Y.Z) is present, it is returned; otherwise version is ''
    """
    import re

    if not require_lines:
        return []

    name_regex = re.compile(r"^\s*([A-Za-z0-9_.-]+)(?:\[[^\]]+\])?")
    eq_version_regex = re.compile(r"==\s*([A-Za-z0-9_.+-]+)")

    results: List[Tuple[str, str]] = []
    for raw in require_lines:
        # Remove environment markers, keep left side of ';'
        left = raw.split(";", 1)[0].strip()

        # Extract normalized name (without extras)
        name_match = name_regex.match(left)
        if not name_match:
            continue
        name = name_match.group(1)

        # Prefer version inside parentheses if present, else anywhere in the spec
        paren_version = ""
        if "(" in left and ")" in left:
            inside = left[left.find("(") + 1 : left.rfind(")")]
            m = eq_version_regex.search(inside)
            if m:
                paren_version = m.group(1)

        if paren_version:
            version = paren_version
        else:
            m2 = eq_version_regex.search(left)
            version = m2.group(1) if m2 else ""

        results.append((name, version))

    return results


def extract_platform_tags_from_wheel(filename: str) -> List[str]:
    """
    Extract platform tags from a wheel filename per PEP 427:
    {dist}-{ver}(-{build tag})?-{py tag}-{abi tag}-{plat tag}.whl
    Platform tag may contain multiple dot-separated entries.
    Returns empty list for non-wheel filenames.
    """
    if not filename.endswith(".whl"):
        return []
    base = filename.rsplit("/", 1)[-1]
    name = base[:-4]  # drop .whl
    parts = name.split("-")
    if len(parts) < 5:
        return []
    platform_part = parts[-1]
    return platform_part.split(".")


def platform_sort_key(platform: str) -> Tuple[int, str]:
    if platform.startswith("win"):
        return (0, platform)
    if platform.startswith("manylinux") or platform.startswith("linux"):
        return (1, platform)
    if platform.startswith("macosx"):
        return (2, platform)
    if platform == "any":
        return (3, platform)
    return (4, platform)


def humanize_platform_tag(platform: str) -> str:
    """Convert wheel platform tags into readable labels for the table header."""
    # Windows
    if platform == "win32":
        return "Windows 32-bit"
    if platform == "win_amd64":
        return "Windows 64-bit"
    if platform == "win_arm64":
        return "Windows ARM64"

    # Linux (manylinux and linux tags)
    if platform.startswith("manylinux"):
        # examples: manylinux1_x86_64, manylinux2014_aarch64, manylinux_2_17_x86_64
        known_arches = [
            "x86_64",
            "i686",
            "aarch64",
            "arm64",
            "ppc64le",
            "s390x",
            "armv7l",
            "armv6l",
        ]
        arch = None
        for a in known_arches:
            if platform.endswith("_" + a):
                arch = a
                break
        if arch is None:
            # Fallback: take last token, may be imperfect but avoids parentheses
            arch = platform.split("_")[-1]

        arch_label = {
            "x86_64": "x86_64",
            "aarch64": "ARM64",
            "arm64": "ARM64",
            "i686": "x86 (32-bit)",
        }.get(arch, arch)

        return f"Linux {arch_label}"

    if platform.startswith("linux"):
        # examples: linux_x86_64, linux_aarch64
        _, _, arch = platform.partition("_")
        arch_label = {
            "x86_64": "x86_64",
            "aarch64": "ARM64",
            "arm64": "ARM64",
            "i686": "x86 (32-bit)",
        }.get(arch, arch or "")
        return f"Linux {arch_label}".strip()

    # macOS
    if platform.startswith("macosx"):
        # example: macosx_10_14_x86_64, macosx_11_0_arm64, macosx_11_0_universal2
        parts = platform.split("_")
        # parts: [macosx, major, minor, arch]
        if len(parts) >= 4:
            major = parts[1]
            minor = parts[2]
            arch = parts[3]
            version_label = f"{major}.{minor}" if minor.isdigit() else major
            if arch == "x86_64":
                arch_label = "Intel"
            elif arch == "arm64":
                arch_label = "Apple Silicon"
            elif arch == "universal2":
                arch_label = "Universal 2"
            else:
                arch_label = arch
            return f"macOS {version_label} {arch_label}"
        return "macOS"

    if platform == "any":
        return "Pure Python (any)"

    # Fallback to raw tag
    return platform


def make_non_breaking(text: str) -> str:
    """Return text with non-breaking hyphens and spaces to avoid line wraps in Markdown cells."""
    # Non-breaking hyphen U+2011; Non-breaking space U+00A0
    return text.replace("-", "\u2011").replace(" ", "\u00A0")


def build_platform_matrix(meta_package: str, client: PypiClient) -> str:
    meta_data = client.fetch_project(meta_package)
    requires_dist = meta_data.get("info", {}).get("requires_dist") or []
    dependencies = parse_requires_dist(requires_dist)

    # Keep only groupdocs-* packages excluding the meta package itself
    filtered: List[Tuple[str, str]] = []
    for pkg, ver in dependencies:
        pname = pkg.strip()
        if not pname:
            continue
        if pname.lower() == meta_package.lower():
            continue
        if pname.lower().startswith("groupdocs-"):
            filtered.append((pname, ver.strip()))

    product_to_platforms: Dict[str, Set[str]] = {}
    all_platforms: Set[str] = set()

    for package_name, pinned_version in filtered:
        proj = client.fetch_project(package_name)
        releases = proj.get("releases", {})
        # Prefer pinned version if available; otherwise fallback to latest
        version = pinned_version if pinned_version in releases else proj.get("info", {}).get("version", "")
        files = releases.get(version, [])

        platforms: Set[str] = set()
        for file_meta in files:
            filename = file_meta.get("filename", "")
            for tag in extract_platform_tags_from_wheel(filename):
                platforms.add(tag)

        product_to_platforms[package_name] = platforms
        all_platforms.update(platforms)

    sorted_platforms = sorted(all_platforms, key=platform_sort_key)

    display_headers: List[str] = [humanize_platform_tag(p) for p in sorted_platforms]
    headers: List[str] = ["Package"] + display_headers
    lines: List[str] = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")

    for product in sorted(product_to_platforms.keys(), key=lambda s: s.lower()):
        support = product_to_platforms[product]
        display_name = make_non_breaking(product)
        product_link = f"[{display_name}](https://pypi.org/project/{product}/)"
        cells: List[str] = [product_link]
        for plat in sorted_platforms:
            cells.append(TICK_MARKDOWN if plat in support else "")
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Build platform support matrix for a meta package from PyPI")
    parser.add_argument("--meta", default="groupdocs-total-net", help="Meta package name on PyPI (default: groupdocs-total-net)")
    parser.add_argument("--output", default="", help="Optional path to write the markdown table; prints to stdout if empty")
    args = parser.parse_args(argv)

    client = PypiClient()
    try:
        table = build_platform_matrix(args.meta, client)
    except RuntimeError as err:
        print(str(err), file=sys.stderr)
        return 1

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(table)
        except OSError as os_err:
            print(f"Failed to write output file: {os_err}", file=sys.stderr)
            return 1
    else:
        print(table)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))


