---
id: developer-guide
url: total/nodejs-java/developer-guide
title: Developer guide
linkTitle: Developer guide
weight: 8
description: "Key features of every API bundled in GroupDocs.Total for Node.js via Java, with runnable JavaScript examples you can copy, plus the input and output files for each one."
keywords: GroupDocs.Total, Node.js, code examples, view documents, convert documents, sign documents, document automation
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

GroupDocs.Total for Node.js via Java installs a single npm package that contains every GroupDocs document API. This guide shows the main features of each one, with a complete JavaScript example per feature that you can copy and run as-is — each comes with the sample file it reads and the file it produces.

These pages are a starting point, not a reference. Once you know which API you need, follow the **Learn more** links at the bottom of each page to that product's own documentation, where every option is documented in full.

## Products in the suite

| Product | Use it to | Entry point |
|:--|:--|:--|
| [Conversion](/total/nodejs-java/developer-guide/conversion/) | Convert between 170+ document and image formats | `Converter` |
| [Viewer](/total/nodejs-java/developer-guide/viewer/) | Render documents to HTML, PDF or images without any external software | `Viewer` |
| [Comparison](/total/nodejs-java/developer-guide/comparison/) | Find the differences between two versions and accept or reject them | `Comparer` |
| [Watermark](/total/nodejs-java/developer-guide/watermark/) | Stamp text or image watermarks onto documents | `Watermarker` |
| [Metadata](/total/nodejs-java/developer-guide/metadata/) | Read, edit and strip document metadata | `Metadata` |
| [Parser](/total/nodejs-java/developer-guide/parser/) | Extract text, images and data from documents | `Parser` |
| [Merger](/total/nodejs-java/developer-guide/merger/) | Join, split and rearrange documents and their pages | `Merger` |
| [Redaction](/total/nodejs-java/developer-guide/redaction/) | Remove sensitive content so it cannot be recovered | `Redactor` |
| [Signature](/total/nodejs-java/developer-guide/signature/) | Sign documents electronically and verify existing signatures | `Signature` |
| [Search](/total/nodejs-java/developer-guide/search/) | Index a document collection and query it | `Index` |
| [Editor](/total/nodejs-java/developer-guide/editor/) | Round-trip a document through HTML for a web editor | `Editor` |
| [Annotation](/total/nodejs-java/developer-guide/annotation/) | Add review markup and read it back | `Annotator` |

GroupDocs.Assembly and GroupDocs.Classification are not part of GroupDocs.Total for Node.js via Java and are not covered here.

Most of these follow the same shape — open a file, do one thing, save. Two do not, and their pages
explain why: **Search** works on a folder rather than a file and indexes before it queries, and
**Editor** is a three-stage round trip through HTML rather than a single call.

{{< alert style="info" >}}
Main entry points (`Viewer`, `Converter`, `Comparer`, and the rest) are exported from `@groupdocs/groupdocs.total`. Options and helper classes are loaded with `java.import('fully.qualified.ClassName')` after you have imported the package.
{{< /alert >}}

## Before you start

1. Install the package as described in [Installation]({{< ref "/total/nodejs-java/getting-started/installation.md" >}}).
2. Set a license as described in [Licensing and evaluation]({{< ref "/total/nodejs-java/getting-started/licensing-and-subscription.md" >}}). Without one, the APIs run in evaluation mode and add trial watermarks to output.
3. Every example on these pages uses a sample file you can download from the tab beside the code.
