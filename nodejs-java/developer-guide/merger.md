---
id: merger
url: total/nodejs-java/developer-guide/merger
title: Merge and split documents with GroupDocs.Merger
linkTitle: Merger
weight: 7
description: "Join documents, split them into single pages and read document information with GroupDocs.Total for Node.js via Java, with runnable JavaScript examples and downloadable input and output files."
keywords: GroupDocs.Merger, merge documents, join Word, split document, extract pages, combine files, Node.js
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

GroupDocs.Merger combines documents and rearranges their pages — join, split, extract, remove, reorder, rotate — and manages document passwords. It works on Word, PDF, spreadsheets, presentations, images and archives.

Every example below opens `contract.docx` and is ready to copy into a project once you have [installed the package]({{< ref "/total/nodejs-java/getting-started/installation.md" >}}).

## Join two documents

`join` appends another document to the one you opened. Call it repeatedly to combine several, then `save` the result.

{{< tabs "merger-join-documents" >}}
{{< tab "JavaScript" >}}
```js
import { Merger } from '@groupdocs/groupdocs.total';
import { resolve } from 'path';

const merger = new Merger('contract.docx');

merger.join('statement-of-work.docx');

// Merger.save resolves a bare relative name oddly, so pass an absolute path
merger.save(resolve('merger-join-documents.docx'));
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`contract.docx` and `statement-of-work.docx` are the sample files used in this example. Download [contract.docx](/total/nodejs-java/_sample_files/contract.docx) and [statement-of-work.docx](/total/nodejs-java/_sample_files/statement-of-work.docx).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "merger-join-documents.docx" >}}  
```text
Binary file (DOCX, 15 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/merger/MergerJoinDocuments/merger-join-documents.docx)
{{< /tab >}}
{{< /tabs >}}

## Split a document into pages

`split` breaks one document into several. With `SplitMode.Pages` and a list of page numbers, each listed page is written out as its own file — here every page of the three-page contract lands separately in the `merger-split-pages` folder.

{{< tabs "merger-split-pages" >}}
{{< tab "JavaScript" >}}
```js
import { Merger } from '@groupdocs/groupdocs.total';
import java from 'java';

const SplitOptions = java.import('com.groupdocs.merger.domain.options.SplitOptions');
const SplitMode = java.import('com.groupdocs.merger.domain.options.SplitMode');

const merger = new Merger('contract.docx');

// {0} is replaced with the page number, so page 1 becomes page_1.docx
const pageNumbers = java.newArray('int', [1, 2, 3]);
const splitOptions = new SplitOptions(
  'merger-split-pages/page_{0}.docx',
  pageNumbers,
  SplitMode.Pages
);

merger.split(splitOptions);
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "merger-split-pages.zip" >}}  
```text
merger-split-pages/page_1.docx (14 KB)
merger-split-pages/page_2.docx (10 KB)
merger-split-pages/page_3.docx (8 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/merger/MergerSplitPages/merger-split-pages.zip)
{{< /tab >}}
{{< /tabs >}}

## Read document information

`getDocumentInfo` reports the format, page count and size — worth checking before you split a document into pages that may not exist.

{{< tabs "merger-document-info" >}}
{{< tab "JavaScript" >}}
```js
import { Merger } from '@groupdocs/groupdocs.total';

const merger = new Merger('contract.docx');
const info = merger.getDocumentInfo();

console.log('File type: ' + info.getType().getFileFormat());
console.log('Pages: ' + info.getPageCount());
console.log('Size: ' + info.getSize() + ' bytes');
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "merger-document-info.txt" >}}  
```text
File type: Microsoft Word Open XML Document
Pages: 3
Size: 15096 bytes
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/merger/MergerDocumentInfo/merger-document-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Merger also removes, moves, swaps and rotates pages, changes page orientation, adds, updates and removes document passwords, generates page previews, and offers a page builder for chaining operations.

* [GroupDocs.Merger for Node.js via Java documentation](https://docs.groupdocs.com/merger/nodejs-java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/merger/nodejs-java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/merger/java/)
