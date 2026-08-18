# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo-based static documentation site for the GroupDocs.Total product family, published to https://docs.groupdocs.com/total/. It contains Markdown documentation for four platforms: .NET (`net/`), Java (`java/`), Node.js via Java (`nodejs-java/`), and Python via .NET (`python-net/`).

## Build and Run Locally

Prerequisites: `npm install -g hugo-extended postcss postcss-cli autoprefixer`

**Windows:**
```
build_docs.cmd
```

**Unix/macOS:**
```
bash build_docs.sh
```

Both scripts initialize the `common/` git submodule, copy platform content into `common/content/total/`, and start `hugo server` with the geekdoc theme config.

## Architecture

- **Content directories** (`net/`, `java/`, `nodejs-java/`, `python-net/`): Markdown documentation organized per platform. Each has `getting-started/`, product overview, and support pages.
- **`common/`**: Git submodule pointing to `docs.groupdocs.com`. Contains the Hugo configuration (`config-geekdoc.toml`, `show-feedback-config.toml`), the `hugo-geekdoc` theme, and shared assets. This directory is gitignored.
- **`_index.md`**: Root landing page with links to all four platform docs.
- **Build process**: Content from `net/`, `java/`, `nodejs-java/`, `python-net/`, and `_index.md` is copied into `common/content/total/` before Hugo builds. Hugo reads config from `common/`.

## Deployment

- Pushing to `master` triggers the `publish-prod` GitHub Actions workflow, which builds with Hugo 0.101.0 (extended) and deploys via rsync to the production server.
- The `publish-qa` workflow is manual (workflow_dispatch only) and deploys to a QA environment.
- Hugo build command: `hugo --source common --minify --config config-geekdoc.toml,show-feedback-config.toml`

## Content Conventions

- Markdown files use Hugo front matter (YAML between `---` delimiters) with fields like `id`, `url`, `title`, `weight`, `productName`.
- Pages can include raw HTML for custom layouts (landing pages, platform cards).
- Images go in `_images/` subdirectories; sample files go in `_sample_files/`.
- Hugo goldmark renderer is used with unsafe HTML enabled.
