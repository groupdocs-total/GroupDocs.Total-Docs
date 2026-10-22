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

## Useful paths

- `java/_index.md` - Java section home
- `java/getting-started/installation.md`
- `java/getting-started/supported-document-formats.md`
- `java/getting-started/sdk-cloud-mcp.md` - when to use the Java SDK, Cloud, or MCP

## Do not

- Invent a format count. Read the format pages that already exist.
- Edit Cloud product repositories from this tree.
- Patch the MCP server. MCP is link-only: https://github.com/groupdocs-total/GroupDocs.Total.Mcp
