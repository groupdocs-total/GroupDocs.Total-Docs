---
id: watermark
url: total/java/developer-guide/watermark
title: Add watermarks with GroupDocs.Watermark
linkTitle: Watermark
weight: 4
description: "Add text and image watermarks to documents from GroupDocs.Total for Java, across Word, PDF and spreadsheets — runnable Java examples with downloadable input and output files."
keywords: GroupDocs.Watermark, add watermark, text watermark, image watermark, protect documents, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Watermark stamps text or images onto documents — Word, PDF, spreadsheets, presentations, images and more — and can find and remove watermarks that are already there.

Each example below is ready to copy into a project once you have [installed the package]({{< ref "/total/java/getting-started/installation.md" >}}).

## Add a text watermark

A `TextWatermark` takes the text and a font. Everything else — rotation, opacity, colour, alignment — is a property you set before adding it.

{{< tabs "watermark-add-text" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.watermark.Watermarker;
import com.groupdocs.watermark.common.HorizontalAlignment;
import com.groupdocs.watermark.common.VerticalAlignment;
import com.groupdocs.watermark.watermarks.Color;
import com.groupdocs.watermark.watermarks.Font;
import com.groupdocs.watermark.watermarks.FontStyle;
import com.groupdocs.watermark.watermarks.TextWatermark;

try (Watermarker watermarker = new Watermarker("contract.docx")) {
    TextWatermark watermark = new TextWatermark(
        "CONFIDENTIAL", new Font("Arial", 42, FontStyle.Bold));

    watermark.setForegroundColor(Color.getRed());
    watermark.setOpacity(0.4);
    watermark.setRotateAngle(-45);
    watermark.setHorizontalAlignment(HorizontalAlignment.Center);
    watermark.setVerticalAlignment(VerticalAlignment.Center);

    watermarker.add(watermark);
    watermarker.save("watermark-add-text.docx");
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "watermark-add-text.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/java/_output_files/developer-guide/watermark/WatermarkAddText/watermark-add-text.docx)
{{< /tab >}}
{{< /tabs >}}

## Add an image watermark

An `ImageWatermark` places a picture instead of text — a logo, a stamp, a QR code. It supports the same alignment and opacity properties.

{{< tabs "watermark-add-image" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.watermark.Watermarker;
import com.groupdocs.watermark.common.HorizontalAlignment;
import com.groupdocs.watermark.common.VerticalAlignment;
import com.groupdocs.watermark.watermarks.ImageWatermark;

try (Watermarker watermarker = new Watermarker("contract.pdf")) {
    try (ImageWatermark watermark = new ImageWatermark("logo.png")) {
        watermark.setOpacity(0.5);
        watermark.setHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setVerticalAlignment(VerticalAlignment.Center);

        watermarker.add(watermark);
    }

    watermarker.save("watermark-add-image.pdf");
}
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`contract.pdf` and `logo.png` are the sample files used in this example. Download [contract.pdf](/total/java/_sample_files/contract.pdf) and [logo.png](/total/java/_sample_files/logo.png).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "watermark-add-image.pdf" >}}  
```text
Binary file (PDF, 153 KB)
```
[Download full output](/total/java/_output_files/developer-guide/watermark/WatermarkAddImage/watermark-add-image.pdf)
{{< /tab >}}
{{< /tabs >}}

## Watermark a spreadsheet

The same two calls work on any supported format. Only the file you open changes.

{{< tabs "watermark-spreadsheet" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.watermark.Watermarker;
import com.groupdocs.watermark.watermarks.Font;
import com.groupdocs.watermark.watermarks.FontStyle;
import com.groupdocs.watermark.watermarks.TextWatermark;

try (Watermarker watermarker = new Watermarker("rate-card.xlsx")) {
    TextWatermark watermark = new TextWatermark(
        "DRAFT", new Font("Calibri", 36, FontStyle.Bold));

    watermark.setOpacity(0.3);
    watermark.setRotateAngle(-30);

    watermarker.add(watermark);
    watermarker.save("watermark-spreadsheet.xlsx");
}
```
{{< /tab >}}
{{< tab "rate-card.xlsx" >}}
{{< tab-text >}}
`rate-card.xlsx` is the sample file used in this example. Click [here](/total/java/_sample_files/rate-card.xlsx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "watermark-spreadsheet.xlsx" >}}  
```text
Binary file (XLSX, 12 KB)
```
[Download full output](/total/java/_output_files/developer-guide/watermark/WatermarkSpreadsheet/watermark-spreadsheet.xlsx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Watermark also searches for existing watermarks and removes or replaces them, adds watermarks to specific pages or sections, works with the images and attachments inside a document, and applies format-specific watermarks such as PDF annotations and Word shapes.

* [GroupDocs.Watermark for Java documentation](https://docs.groupdocs.com/watermark/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/watermark/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/watermark/java/)
