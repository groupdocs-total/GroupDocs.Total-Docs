---
id: viewer
url: total/nodejs-java/developer-guide/viewer
title: View and render documents with GroupDocs.Viewer
linkTitle: Viewer
weight: 2
description: "Render Word, Excel, PDF and 170+ other formats to HTML, PDF or PNG from GroupDocs.Total for Node.js via Java, with runnable JavaScript examples and downloadable input and output files."
keywords: GroupDocs.Viewer, render document, view document, DOCX to HTML, DOCX to PDF, DOCX to PNG, document viewer, Node.js
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

GroupDocs.Viewer renders a document into something a browser can display — HTML, PDF, or one image per page — without Microsoft Office or any other external software. It is the API to reach for when you want to *show* a document rather than change it.

Every example below opens `contract.docx` and is ready to copy into a project once you have [installed the package]({{< ref "/total/nodejs-java/getting-started/installation.md" >}}).

## Render a document to HTML

Rendering to HTML gives you one `.html` file per page. `forEmbeddedResources` inlines images, fonts and stylesheets into each page, so a page is self-contained and needs no companion files.

{{< tabs "viewer-render-to-html" >}}
{{< tab "JavaScript" >}}
```js
import { Viewer } from '@groupdocs/groupdocs.total';
import java from 'java';

const HtmlViewOptions = java.import('com.groupdocs.viewer.options.HtmlViewOptions');

const viewer = new Viewer('contract.docx');
// {0} is replaced with the page number, so page 1 becomes page_1.html
const viewOptions = HtmlViewOptions.forEmbeddedResources(
  'viewer-render-to-html/page_{0}.html'
);

viewer.view(viewOptions);
viewer.close();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "viewer-render-to-html.zip" >}}  
```text
viewer-render-to-html/page_1.html (147 KB)
viewer-render-to-html/page_2.html (74 KB)
viewer-render-to-html/page_3.html (828 bytes)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/viewer/ViewerRenderToHtml/viewer-render-to-html.zip)
{{< /tab >}}
{{< /tabs >}}

To keep resources as separate files next to the HTML instead of inlining them, use `HtmlViewOptions.forExternalResources` — useful when several pages share the same images and you want them cached once.

## Render a document to PDF

Rendering to PDF produces a single file, which is the usual choice for printing or archiving.

{{< tabs "viewer-render-to-pdf" >}}
{{< tab "JavaScript" >}}
```js
import { Viewer } from '@groupdocs/groupdocs.total';
import java from 'java';

const PdfViewOptions = java.import('com.groupdocs.viewer.options.PdfViewOptions');

const viewer = new Viewer('contract.docx');
const viewOptions = new PdfViewOptions('viewer-render-to-pdf.pdf');

viewer.view(viewOptions);
viewer.close();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "viewer-render-to-pdf.pdf" >}}  
```text
Binary file (PDF, 126 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/viewer/ViewerRenderToPdf/viewer-render-to-pdf.pdf)
{{< /tab >}}
{{< /tabs >}}

## Render a document to PNG

Rendering to images gives you one PNG per page — the right output for thumbnails and previews. `PngViewOptions` also accepts a width and height if you need a fixed size.

{{< tabs "viewer-render-to-png" >}}
{{< tab "JavaScript" >}}
```js
import { Viewer } from '@groupdocs/groupdocs.total';
import java from 'java';

const PngViewOptions = java.import('com.groupdocs.viewer.options.PngViewOptions');

const viewer = new Viewer('contract.docx');
const viewOptions = new PngViewOptions('viewer-render-to-png/page_{0}.png');

// Render only the first two pages
viewer.view(viewOptions, 1, 2);
viewer.close();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "viewer-render-to-png.zip" >}}  
```text
viewer-render-to-png/page_1.png (86 KB)
viewer-render-to-png/page_2.png (87 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/viewer/ViewerRenderToPng/viewer-render-to-png.zip)
{{< /tab >}}
{{< /tabs >}}

## Read document information

Before rendering you often want to know what you are dealing with — how many pages, what format, whether it is encrypted. `getViewInfo` answers that without rendering anything.

{{< tabs "viewer-document-info" >}}
{{< tab "JavaScript" >}}
```js
import { Viewer } from '@groupdocs/groupdocs.total';
import java from 'java';

const ViewInfoOptions = java.import('com.groupdocs.viewer.options.ViewInfoOptions');

const viewer = new Viewer('contract.docx');
const viewInfoOptions = ViewInfoOptions.forHtmlView();
const viewInfo = viewer.getViewInfo(viewInfoOptions);

console.log('File type: ' + viewInfo.getFileType());
console.log('Pages: ' + viewInfo.getPages().size());

const pages = viewInfo.getPages();
for (let i = 0; i < pages.size(); i++) {
  const page = pages.get(i);
  console.log('Page ' + page.getNumber() + ': ' + page.getWidth() + 'x' + page.getHeight());
}

viewer.close();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "viewer-document-info.txt" >}}  
```text
File type: Microsoft Word Open XML Document (.docx)
Pages: 3
Page 1: 612x792
Page 2: 612x792
Page 3: 612x792
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/viewer/ViewerDocumentInfo/viewer-document-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Learn more

The examples above cover the common cases. GroupDocs.Viewer also renders archives, CAD drawings, email messages, Outlook data files and Visio diagrams, caches rendered output, and processes attachments.

* [GroupDocs.Viewer for Node.js via Java documentation](https://docs.groupdocs.com/viewer/nodejs-java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/viewer/nodejs-java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/viewer/nodejs-java/)
