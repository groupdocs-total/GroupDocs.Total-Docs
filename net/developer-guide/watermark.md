---
id: watermark
url: total/net/developer-guide/watermark
title: Add watermarks with GroupDocs.Watermark
linkTitle: Watermark
weight: 4
description: "Add text and image watermarks to documents from GroupDocs.Total for .NET, and inspect what a document contains — runnable C# examples with downloadable input and output files."
keywords: GroupDocs.Watermark, add watermark, text watermark, image watermark, protect documents, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Watermark stamps text or images onto documents — Word, PDF, spreadsheets, presentations, images and more — and can find and remove watermarks that are already there.

## Add a text watermark

A `TextWatermark` takes the text and a font. Everything else — rotation, opacity, colour, alignment — is a property you set before adding it.

{{< tabs "watermark-add-text" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Watermark;
using GroupDocs.Watermark.Common;
using GroupDocs.Watermark.Watermarks;

using (Watermarker watermarker = new Watermarker("contract.docx"))
{
    TextWatermark watermark = new TextWatermark(
        "CONFIDENTIAL", new Font("Arial", 42, FontStyle.Bold));

    watermark.ForegroundColor = Color.Red;
    watermark.Opacity = 0.4;
    watermark.RotateAngle = -45;
    watermark.HorizontalAlignment = HorizontalAlignment.Center;
    watermark.VerticalAlignment = VerticalAlignment.Center;

    watermarker.Add(watermark);
    watermarker.Save("watermark-add-text.docx");
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "watermark-add-text.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/net/_output_files/developer-guide/watermark/WatermarkAddText/watermark-add-text.docx)
{{< /tab >}}
{{< /tabs >}}

## Add an image watermark

An `ImageWatermark` places a picture instead of text — a logo, a stamp, a QR code. It supports the same alignment and opacity properties.

{{< tabs "watermark-add-image" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Watermark;
using GroupDocs.Watermark.Common;
using GroupDocs.Watermark.Watermarks;

using (Watermarker watermarker = new Watermarker("contract.pdf"))
{
    using (ImageWatermark watermark = new ImageWatermark("logo.png"))
    {
        watermark.Opacity = 0.5;
        watermark.HorizontalAlignment = HorizontalAlignment.Center;
        watermark.VerticalAlignment = VerticalAlignment.Center;

        watermarker.Add(watermark);
    }

    watermarker.Save("watermark-add-image.pdf");
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` and `logo.png` are the sample files used in this example. Download [contract.pdf](/total/net/_sample_files/contract.pdf) and [logo.png](/total/net/_sample_files/logo.png).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "watermark-add-image.pdf" >}}  
```text
Binary file (PDF, 154 KB)
```
[Download full output](/total/net/_output_files/developer-guide/watermark/WatermarkAddImage/watermark-add-image.pdf)
{{< /tab >}}
{{< /tabs >}}

## Watermark a spreadsheet

The same two calls work on any supported format. Only the file you open changes.

{{< tabs "watermark-spreadsheet" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Watermark;
using GroupDocs.Watermark.Watermarks;

using (Watermarker watermarker = new Watermarker("rate-card.xlsx"))
{
    TextWatermark watermark = new TextWatermark(
        "DRAFT", new Font("Calibri", 36, FontStyle.Bold));

    watermark.Opacity = 0.3;
    watermark.RotateAngle = -30;

    watermarker.Add(watermark);
    watermarker.Save("watermark-spreadsheet.xlsx");
}
```
{{< /tab >}}
{{< tab "rate-card.xlsx" >}}
{{< tab-text >}}
`rate-card.xlsx` is the sample file used in this example. Click [here](/total/net/_sample_files/rate-card.xlsx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "watermark-spreadsheet.xlsx" >}}  
```text
Binary file (XLSX, 12 KB)
```
[Download full output](/total/net/_output_files/developer-guide/watermark/WatermarkSpreadsheet/watermark-spreadsheet.xlsx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Watermark also searches for existing watermarks and removes or replaces them, adds watermarks to specific pages or sections, works with the images and attachments inside a document, and applies format-specific watermarks such as PDF annotations and Word shapes.

* [GroupDocs.Watermark for .NET documentation](https://docs.groupdocs.com/watermark/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/watermark/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/watermark/net/)
