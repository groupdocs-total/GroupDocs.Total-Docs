---
id: conversion
url: total/net/developer-guide/conversion
title: Convert documents with GroupDocs.Conversion
linkTitle: Conversion
weight: 1
description: "Convert between 170+ formats from GroupDocs.Total for .NET — PDF to Word, Word to PDF, and more — with runnable C# examples and downloadable input and output files."
keywords: GroupDocs.Conversion, convert document, PDF to DOCX, DOCX to PDF, file conversion, document converter, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Conversion turns a document of one format into another — over 170 formats in total, covering word processing, spreadsheets, presentations, PDF, email, images, CAD and more. The API is the same regardless of the direction: open the source with `Converter`, pick the convert options for the target format, call `Convert`.

## Convert PDF to Word

`WordProcessingConvertOptions` targets the Word family. With no format specified it produces DOCX.

{{< tabs "conversion-pdf-to-word" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Conversion;
using GroupDocs.Conversion.Options.Convert;

using (Converter converter = new Converter("contract.pdf"))
{
    WordProcessingConvertOptions convertOptions = new WordProcessingConvertOptions();

    converter.Convert("conversion-pdf-to-word.docx", convertOptions);
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "conversion-pdf-to-word.docx" >}}  
```text
Binary file (DOCX, 22 KB)
```
[Download full output](/total/net/_output_files/developer-guide/conversion/ConversionPdfToWord/conversion-pdf-to-word.docx)
{{< /tab >}}
{{< /tabs >}}

## Convert Word to PDF

The reverse direction swaps the options type. Nothing else changes — that symmetry holds for every format pair.

{{< tabs "conversion-word-to-pdf" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Conversion;
using GroupDocs.Conversion.Options.Convert;

using (Converter converter = new Converter("contract.docx"))
{
    PdfConvertOptions convertOptions = new PdfConvertOptions();

    converter.Convert("conversion-word-to-pdf.pdf", convertOptions);
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "conversion-word-to-pdf.pdf" >}}  
```text
Binary file (PDF, 123 KB)
```
[Download full output](/total/net/_output_files/developer-guide/conversion/ConversionWordToPdf/conversion-word-to-pdf.pdf)
{{< /tab >}}
{{< /tabs >}}

## Convert only specific pages

Converting a long document page by page is wasteful when you only need a few. Convert options accept a page range.

{{< tabs "conversion-specific-pages" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Conversion;
using GroupDocs.Conversion.Options.Convert;

using (Converter converter = new Converter("contract.docx"))
{
    PdfConvertOptions convertOptions = new PdfConvertOptions
    {
        PageNumber = 1,
        PagesCount = 2
    };

    converter.Convert("conversion-specific-pages.pdf", convertOptions);
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "conversion-specific-pages.pdf" >}}  
```text
Binary file (PDF, 123 KB)
```
[Download full output](/total/net/_output_files/developer-guide/conversion/ConversionSpecificPages/conversion-specific-pages.pdf)
{{< /tab >}}
{{< /tabs >}}

## Read source document information

`GetDocumentInfo` reports what the source actually is, which is worth checking before you convert a file you did not produce.

{{< tabs "conversion-document-info" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Conversion;
using GroupDocs.Conversion.Contracts;

using (Converter converter = new Converter("contract.pdf"))
{
    IDocumentInfo info = converter.GetDocumentInfo();

    Console.WriteLine("Format: " + info.Format);
    Console.WriteLine("Pages: " + info.PagesCount);
    Console.WriteLine("Size: " + info.Size + " bytes");
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "conversion-document-info.txt" >}}  
```text
Format: pdf
Pages: 3
Size: 130412 bytes
```
[Download full output](/total/net/_output_files/developer-guide/conversion/ConversionDocumentInfo/conversion-document-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Learn more

Beyond the basics, GroupDocs.Conversion loads sources from streams, URLs and cloud storage, converts to and from spreadsheets, presentations, images, ebooks and CAD drawings, applies watermarks during conversion, and offers a fluent API for chained operations.

* [GroupDocs.Conversion for .NET documentation](https://docs.groupdocs.com/conversion/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/conversion/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/conversion/net/)
