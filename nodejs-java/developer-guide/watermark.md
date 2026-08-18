---
id: watermark
url: total/nodejs-java/developer-guide/watermark
title: Add watermarks with GroupDocs.Watermark
linkTitle: Watermark
weight: 4
description: "Add text and image watermarks to documents from GroupDocs.Total for Node.js via Java, across Word, PDF and spreadsheets — runnable JavaScript examples with downloadable input and output files."
keywords: GroupDocs.Watermark, add watermark, text watermark, image watermark, protect documents, Node.js
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

GroupDocs.Watermark stamps text or images onto documents — Word, PDF, spreadsheets, presentations, images and more — and can find and remove watermarks that are already there.

Each example below is ready to copy into a project once you have [installed the package]({{< ref "/total/nodejs-java/getting-started/installation.md" >}}).

## Add a text watermark

A `TextWatermark` takes the text and a font. Everything else — rotation, opacity, colour, alignment — is a property you set before adding it.

{{< tabs "watermark-add-text" >}}
{{< tab "JavaScript" >}}
```js
import { Watermarker } from '@groupdocs/groupdocs.total';
import java from 'java';

const TextWatermark = java.import('com.groupdocs.watermark.watermarks.TextWatermark');
const Font = java.import('com.groupdocs.watermark.watermarks.Font');
const FontStyle = java.import('com.groupdocs.watermark.watermarks.FontStyle');
const Color = java.import('com.groupdocs.watermark.watermarks.Color');
const HorizontalAlignment = java.import('com.groupdocs.watermark.common.HorizontalAlignment');
const VerticalAlignment = java.import('com.groupdocs.watermark.common.VerticalAlignment');

const watermarker = new Watermarker('contract.docx');

const watermark = new TextWatermark(
  'CONFIDENTIAL',
  new Font('Arial', 42, FontStyle.Bold)
);

watermark.setForegroundColor(Color.getRed());
watermark.setOpacity(0.4);
watermark.setRotateAngle(-45);
watermark.setHorizontalAlignment(HorizontalAlignment.Center);
watermark.setVerticalAlignment(VerticalAlignment.Center);

watermarker.add(watermark);
watermarker.save('watermark-add-text.docx');
watermarker.close();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "watermark-add-text.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/watermark/WatermarkAddText/watermark-add-text.docx)
{{< /tab >}}
{{< /tabs >}}

## Add an image watermark

An `ImageWatermark` places a picture instead of text — a logo, a stamp, a QR code. It supports the same alignment and opacity properties.

{{< tabs "watermark-add-image" >}}
{{< tab "JavaScript" >}}
```js
import { Watermarker } from '@groupdocs/groupdocs.total';
import java from 'java';

const ImageWatermark = java.import('com.groupdocs.watermark.watermarks.ImageWatermark');
const HorizontalAlignment = java.import('com.groupdocs.watermark.common.HorizontalAlignment');
const VerticalAlignment = java.import('com.groupdocs.watermark.common.VerticalAlignment');

const watermarker = new Watermarker('contract.pdf');
const watermark = new ImageWatermark('logo.png');

watermark.setOpacity(0.5);
watermark.setHorizontalAlignment(HorizontalAlignment.Center);
watermark.setVerticalAlignment(VerticalAlignment.Center);

watermarker.add(watermark);
watermark.close();

watermarker.save('watermark-add-image.pdf');
watermarker.close();
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`contract.pdf` and `logo.png` are the sample files used in this example. Download [contract.pdf](/total/nodejs-java/_sample_files/contract.pdf) and [logo.png](/total/nodejs-java/_sample_files/logo.png).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "watermark-add-image.pdf" >}}  
```text
Binary file (PDF, 153 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/watermark/WatermarkAddImage/watermark-add-image.pdf)
{{< /tab >}}
{{< /tabs >}}

## Watermark a spreadsheet

The same two calls work on any supported format. Only the file you open changes.

{{< tabs "watermark-spreadsheet" >}}
{{< tab "JavaScript" >}}
```js
import { Watermarker } from '@groupdocs/groupdocs.total';
import java from 'java';

const TextWatermark = java.import('com.groupdocs.watermark.watermarks.TextWatermark');
const Font = java.import('com.groupdocs.watermark.watermarks.Font');
const FontStyle = java.import('com.groupdocs.watermark.watermarks.FontStyle');

const watermarker = new Watermarker('rate-card.xlsx');

const watermark = new TextWatermark(
  'DRAFT',
  new Font('Calibri', 36, FontStyle.Bold)
);

watermark.setOpacity(0.3);
watermark.setRotateAngle(-30);

watermarker.add(watermark);
watermarker.save('watermark-spreadsheet.xlsx');
watermarker.close();
```
{{< /tab >}}
{{< tab "rate-card.xlsx" >}}
{{< tab-text >}}
`rate-card.xlsx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/rate-card.xlsx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "watermark-spreadsheet.xlsx" >}}  
```text
Binary file (XLSX, 12 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/watermark/WatermarkSpreadsheet/watermark-spreadsheet.xlsx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Watermark also searches for existing watermarks and removes or replaces them, adds watermarks to specific pages or sections, works with the images and attachments inside a document, and applies format-specific watermarks such as PDF annotations and Word shapes.

* [GroupDocs.Watermark for Node.js via Java documentation](https://docs.groupdocs.com/watermark/nodejs-java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/watermark/nodejs-java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/watermark/java/)
