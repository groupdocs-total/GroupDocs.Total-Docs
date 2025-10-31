## Platforms Matrix Builder for groupdocs-total-net

This tool generates a Markdown table showing platform support for each product included in the `groupdocs-total-net` metapackage. It fetches dependency metadata from PyPI and infers support by inspecting the wheel filenames (platform tags).

### How it works
- Reads dependencies (requires_dist) of a meta package on PyPI (default: `groupdocs-total-net`).
- For each dependency, inspects available wheel files and extracts platform tags (e.g., `win32`, `win_amd64`, `manylinux2014_x86_64`, `macosx_11_0_arm64`).
- Builds a Markdown table with products as rows and platforms as columns.
- Marks supported cells with: `[(tick)](/total/python-net/_images/check-blue.png)`.

### Requirements
- Python 3.8+
- No external dependencies (uses only the Python standard library).

### Usage
Run from the repository root:

```bash
python matrix_builder.py --meta groupdocs-total-net --output matrix.md
```

Options:
- `--meta`: Meta package name on PyPI. Defaults to `groupdocs-total-net`.
- `--output`: Path to write the Markdown table. If omitted, prints to stdout.

### Example output (truncated)
```markdown
| Product | win32 | win_amd64 |
|---|---|---|
| groupdocs-assembly-net | [(tick)](/total/python-net/_images/check-blue.png) | [(tick)](/total/python-net/_images/check-blue.png) |
| groupdocs-viewer-net |  | [(tick)](/total/python-net/_images/check-blue.png) |
```

The actual platforms (columns) are computed from the union of platform tags found across all dependency wheel files for the specified meta package.


