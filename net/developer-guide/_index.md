---
id: developer-guide
url: total/net/developer-guide
title: Developer guide
linkTitle: Developer guide
weight: 6
description: "Key features of every API bundled in GroupDocs.Total for .NET, with runnable C# examples you can copy, plus the input and output files for each one."
keywords: GroupDocs.Total, .NET, C#, code examples, view documents, convert documents, sign documents, document automation
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Total for .NET installs a single package that contains every GroupDocs document API. This guide shows the main features of each one, with a complete C# example per feature that you can copy and run as-is — each comes with the sample file it reads and the file it produces.

These pages are a starting point, not a reference. Once you know which API you need, follow the **Learn more** links at the bottom of each page to that product's own documentation, where every option is documented in full.

## Products in the suite

| Product | Use it to | Entry point |
|:--|:--|:--|
| [Conversion]({{< ref "/total/net/developer-guide/conversion.md" >}}) | Convert between 170+ document and image formats | `Converter` |
| [Viewer]({{< ref "/total/net/developer-guide/viewer.md" >}}) | Render documents to HTML, PDF or images without any external software | `Viewer` |
| [Comparison]({{< ref "/total/net/developer-guide/comparison.md" >}}) | Find the differences between two versions and accept or reject them | `Comparer` |
| [Watermark]({{< ref "/total/net/developer-guide/watermark.md" >}}) | Stamp text or image watermarks onto documents | `Watermarker` |
| [Metadata]({{< ref "/total/net/developer-guide/metadata.md" >}}) | Read, edit and strip document metadata | `Metadata` |
| [Parser]({{< ref "/total/net/developer-guide/parser.md" >}}) | Extract text, images and data from documents | `Parser` |
| [Merger]({{< ref "/total/net/developer-guide/merger.md" >}}) | Join, split and rearrange documents and their pages | `Merger` |
| [Assembly]({{< ref "/total/net/developer-guide/assembly.md" >}}) | Generate documents from a template and a data source | `DocumentAssembler` |
| [Redaction]({{< ref "/total/net/developer-guide/redaction.md" >}}) | Remove sensitive content so it cannot be recovered | `Redactor` |
| [Signature]({{< ref "/total/net/developer-guide/signature.md" >}}) | Sign documents electronically and verify existing signatures | `Signature` |
| [Search]({{< ref "/total/net/developer-guide/search.md" >}}) | Index a document collection and query it | `Index` |
| [Editor]({{< ref "/total/net/developer-guide/editor.md" >}}) | Round-trip a document through HTML for a web editor | `Editor` |
| [Annotation]({{< ref "/total/net/developer-guide/annotation.md" >}}) | Add review markup and read it back | `Annotator` |

GroupDocs.Classification is not part of GroupDocs.Total and is not covered here.

Most of these follow the same shape — open a file, do one thing, save. Three do not, and their pages
explain why: **Search** works on a folder rather than a file and indexes before it queries,
**Assembly** needs a template you author first, and **Editor** is a three-stage round trip through
HTML rather than a single call.

## Before you start

1. Install the package as described in [Installation]({{< ref "/total/net/getting-started/installation.md" >}}).
2. Set a license as described in [Licensing and evaluation]({{< ref "/total/net/getting-started/licensing-and-subscription.md" >}}). Without one, the APIs run in evaluation mode and add trial watermarks to output.
3. Every example on these pages uses a sample file you can download from the tab beside the code.
