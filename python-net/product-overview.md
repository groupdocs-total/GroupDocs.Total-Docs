---
id: product-overview
url: total/python-net/product-overview
title: GroupDocs.Total for Python via .NET Overview
linkTitle: Product Overview
weight: 1
description: "GroupDocs.Total for Python via .NET is a comprehensive collection of all GroupDocs on-premise .NET APIs, compiled monthly to include the latest versions for document processing and automation."
keywords: document automation, convert files, view files, HTML, PDF, PNG, JPEG
productName: GroupDocs.Total for Python via .NET
toc: True
---

[GroupDocs.Total for Python via .NET](https://products.groupdocs.com/total/python-net/) is a powerful document processing SDK for Python developers.  
It enables you to compare, convert, view, sign, and watermark various document formats, including PDF, DOCX, XLSX, PPTX, and more — all within your Python applications.

## Technology Stack

**GroupDocs.Total for Python via .NET** is built on a hybrid technology stack that combines the flexibility of Python with the performance and reliability of the modern .NET runtime. Installing .NET runtime is not required as it is already embedded within each product package.

- **Programming Language:** Python 3.5 to 3.14
- **Supported Platforms:** Windows x64, Linux x86_64 (glibc 2.27 or later) and macOS 13 or later (Intel and Apple Silicon); see [System Requirements]({{< ref "/total/python-net/getting-started/system-requirements.md" >}})
- **Distribution Format:** the `groupdocs-total-net` metapackage on [PyPI](https://pypi.org/project/groupdocs-total-net/), which installs the 14 product wheels (`.whl`); each product's wheels can also be downloaded from its page on the [official GroupDocs releases](https://releases.groupdocs.com/total/python-net/) website

## Key Features

**GroupDocs.Total for Python via .NET** combines the functionality of multiple GroupDocs APIs into a single, unified solution for professional document automation.

With this toolkit, you can:

- **Convert** between more than 200 file formats, including Word, PDF, Excel, PowerPoint, images, and text files.  
- **Compare** and highlight differences between documents to track changes efficiently.  
- **Sign and verify** documents using digital or image-based signatures.  
- **Redact** sensitive information to ensure data privacy and compliance.  
- **Add or detect watermarks** to protect intellectual property and maintain branding.  
- **Merge or split** multi-page documents for flexible document management.  
- **Extract text, metadata, and structured data** from office files, images, and archives.  
- **Index and search** document collections in full text.  
- **Annotate and edit** documents, and **convert** them to Markdown.  
- **Automate workflows** - combine operations like conversion, signing, and watermarking into one processing pipeline.  

Free technical assistance is available to all users, provided directly by the GroupDocs product teams.

## Included APIs

The `groupdocs-total-net` metapackage installs the following 14 products:

| Product | Description |
|:--|:--|
| [GroupDocs.Conversion&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/conversion/python-net/) | Convert documents between multiple formats using this library, offering flexible and high-performance conversion options. |
| [GroupDocs.Viewer&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/viewer/python-net/) | Add document viewing capabilities to your Python applications, supporting a wide range of document types for seamless display. |
| [GroupDocs.Comparison&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/comparison/python-net/) | Compare documents and visualize changes to easily identify differences between file versions. |
| [GroupDocs.Watermark&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/watermark/python-net/) | Protect your files by adding text or image watermarks, with various customization and detection options. |
| [GroupDocs.Metadata&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/metadata/python-net/) | Access, edit, and manage metadata properties across multiple document formats. |
| [GroupDocs.Merger&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/merger/python-net/) | Merge, split, or rearrange pages within documents easily. |
| [GroupDocs.Assembly&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/assembly/python-net/) | Generate documents dynamically from templates by merging data from various sources. |
| [GroupDocs.Redaction&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/redaction/python-net/) | Securely remove or mask confidential content to maintain compliance and data privacy. |
| [GroupDocs.Signature&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/signature/python-net/) | Sign and verify documents with text, image, barcode/QR, and digital signatures. |
| [GroupDocs.Parser&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/parser/python-net/) | Extract text, tables, images, metadata and barcodes from documents. |
| [GroupDocs.Search&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/search/python-net/) | Index documents and search them in full text. |
| [GroupDocs.Annotation&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/annotation/python-net/) | Add annotations, markups and comments to documents and images. |
| [GroupDocs.Editor&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/editor/python-net/) | Edit documents through HTML and save them back to their format. |
| [GroupDocs.Markdown&nbsp;for&nbsp;Python&nbsp;via&nbsp;.NET](https://docs.groupdocs.com/markdown/python-net/) | Convert documents to Markdown. |

## Several Products in One Script

Each product ships its own .NET runtime, and products can be combined in one Python process. On Windows, set `os.environ["DOTNET_MULTILEVEL_LOOKUP"] = "0"` at the top of the script, before the first call into any product: on a machine with a newer .NET installed system-wide, it keeps Viewer, Metadata, Annotation, Comparison, Editor, Merger and Redaction on their own runtimes, so that two of them can share a process. The [Quick Start Guide]({{< ref "/total/python-net/getting-started/quick-start-guide.md" >}}) shows an example.

## Getting Started

To start working with GroupDocs.Total for Python via .NET, refer to the following sections:  
- [System Requirements]({{< ref "/total/python-net/getting-started/system-requirements.md" >}})  
- [Installation]({{< ref "/total/python-net/getting-started/installation.md" >}})  
- [Quick Start Guide]({{< ref "/total/python-net/getting-started/quick-start-guide.md" >}})  

These resources will help you set up and integrate the SDK into your projects quickly.

## Developer Guide

For detailed examples and advanced usage instructions, see the **Developer Guides** within the documentation of each individual GroupDocs product.

## Technical Support

If you encounter any issues or have suggestions for improvement, please visit the [Technical Support]({{< ref "/total/python-net/technical-support" >}}) page.  
It provides multiple support channels to help you get assistance and resolve issues efficiently.
