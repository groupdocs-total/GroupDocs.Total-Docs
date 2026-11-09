# AGENTS.md

Guidance for AI agents (and people) working in this documentation repository.

## What this is

Hugo sources for the GroupDocs.Total documentation site:

https://docs.groupdocs.com/total/

Platform folders in this tree: `net/`, `java/`, `nodejs-java/`, `python-net/`. Do not delete them. `CLAUDE.md` describes the build. This file is the AI entry for the same repo.

## Build

Prerequisites named in `CLAUDE.md`: `hugo-extended`, `postcss`, `postcss-cli`, `autoprefixer`.

- Windows: `build_docs.cmd`
- Unix: `bash build_docs.sh`

`common/` is a git submodule and is gitignored. The scripts copy platform content into `common/content/total/` and start Hugo.

## Java package

- groupId: `com.groupdocs`
- artifactId: `groupdocs-total`
- Repository: https://releases.groupdocs.com/java/repo/
- Examples pin seen in the Java examples repo: 26.10

## Python package

- PyPI: `groupdocs-total-net` (https://pypi.org/project/groupdocs-total-net/), version 26.11.0
- A metapackage: it installs the 14 GroupDocs for Python via .NET products and holds no code. Code imports each product from its own package (`groupdocs.conversion`, `groupdocs.viewer`, ...), and licenses each product separately (`GROUPDOCS_LIC_PATH` covers all of them).
- Python 3.5-3.14; Windows x64, Linux x86_64 with glibc 2.27+, macOS 13+

## Useful paths

- `java/_index.md` - Java section home
- `java/getting-started/installation.md`
- `java/getting-started/supported-document-formats.md`
- `java/getting-started/sdk-cloud-mcp.md` - when to use the Java SDK, Cloud, or MCP
- `python-net/_index.md` - Python via .NET section home
- `python-net/getting-started/installation.md`
- `python-net/getting-started/quick-start-guide.md`

## Do not

- Invent a format count. Read the format pages that already exist.
- Edit Cloud product repositories from this tree.
- Patch the MCP server. MCP is link-only: https://github.com/groupdocs-total/GroupDocs.Total.Mcp
