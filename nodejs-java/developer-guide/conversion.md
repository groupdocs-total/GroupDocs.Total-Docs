---
id: conversion
url: total/nodejs-java/developer-guide/conversion
title: Convert documents with GroupDocs.Conversion
linkTitle: Conversion
weight: 1
description: "Convert between 170+ formats from GroupDocs.Total for Node.js via Java — PDF to Word, Word to PDF, and more — with runnable JavaScript examples and downloadable input and output files."
keywords: GroupDocs.Conversion, convert document, PDF to DOCX, DOCX to PDF, file conversion, document converter, Node.js
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

GroupDocs.Conversion turns a document of one format into another — over 170 formats in total, covering word processing, spreadsheets, presentations, PDF, email, images, CAD and more. The API is the same regardless of the direction: open the source with `Converter`, pick the convert options for the target format, call `convert`.

## Convert PDF to Word

`WordProcessingConvertOptions` targets the Word family. With no format specified it produces DOCX.

{{< tabs "conversion-pdf-to-word" >}}
{{< tab "JavaScript" >}}
```js
import { Converter } from '@groupdocs/groupdocs.total';
import java from 'java';

const WordProcessingConvertOptions = java.import(
  'com.groupdocs.conversion.options.convert.WordProcessingConvertOptions'
);

const converter = new Converter('contract.pdf');
const convertOptions = new WordProcessingConvertOptions();

converter.convert('conversion-pdf-to-word.docx', convertOptions);
converter.close();
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "conversion-pdf-to-word.docx" >}}  
```text
Binary file (DOCX, 19 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/conversion/ConversionPdfToWord/conversion-pdf-to-word.docx)
{{< /tab >}}
{{< /tabs >}}

## Convert Word to PDF

The reverse direction swaps the options type. Nothing else changes — that symmetry holds for every format pair.

{{< tabs "conversion-word-to-pdf" >}}
{{< tab "JavaScript" >}}
```js
import { Converter } from '@groupdocs/groupdocs.total';
import java from 'java';

const PdfConvertOptions = java.import(
  'com.groupdocs.conversion.options.convert.PdfConvertOptions'
);

const converter = new Converter('contract.docx');
const convertOptions = new PdfConvertOptions();

converter.convert('conversion-word-to-pdf.pdf', convertOptions);
converter.close();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "conversion-word-to-pdf.pdf" >}}  
```text
Binary file (PDF, 123 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/conversion/ConversionWordToPdf/conversion-word-to-pdf.pdf)
{{< /tab >}}
{{< /tabs >}}

## Read source document information

`getDocumentInfo` reports what the source actually is, which is worth checking before you convert a file you did not produce.

{{< tabs "conversion-document-info" >}}
{{< tab "JavaScript" >}}
```js
import { Converter } from '@groupdocs/groupdocs.total';

const converter = new Converter('contract.pdf');
const info = converter.getDocumentInfo();

console.log('Format: ' + info.getFormat());
console.log('Pages: ' + info.getPagesCount());
console.log('Size: ' + info.getSize() + ' bytes');

converter.close();
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "conversion-document-info.txt" >}}  
```text
Format: pdf
Pages: 3
Size: 130412 bytes
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/conversion/ConversionDocumentInfo/conversion-document-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Learn more

Beyond the basics, GroupDocs.Conversion loads sources from streams, URLs and cloud storage, converts to and from spreadsheets, presentations, images, ebooks and CAD drawings, applies watermarks during conversion, and offers a fluent API for chained operations.

* [GroupDocs.Conversion for Node.js via Java documentation](https://docs.groupdocs.com/conversion/nodejs-java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/conversion/nodejs-java/supported-file-formats/)
* [API reference](https://reference.groupdocs.com/conversion/java/)
