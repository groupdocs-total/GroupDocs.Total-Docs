---
id: viewer
url: total/java/developer-guide/viewer
title: View and render documents with GroupDocs.Viewer
linkTitle: Viewer
weight: 2
description: "Render Word, Excel, PDF and 170+ other formats to HTML, PDF or PNG from GroupDocs.Total for Java, with runnable Java examples and downloadable input and output files."
keywords: GroupDocs.Viewer, render document, view document, DOCX to HTML, DOCX to PDF, DOCX to PNG, document viewer, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Viewer renders a document into something a browser can display — HTML, PDF, or one image per page — without Microsoft Office or any other external software. It is the API to reach for when you want to *show* a document rather than change it.

Every example below opens `contract.docx` and is ready to copy into a project once you have [installed the package]({{< ref "/total/java/getting-started/installation.md" >}}).

## Render a document to HTML

Rendering to HTML gives you one `.html` file per page. `forEmbeddedResources` inlines images, fonts and stylesheets into each page, so a page is self-contained and needs no companion files.

{{< tabs "viewer-render-to-html" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.viewer.Viewer;
import com.groupdocs.viewer.options.HtmlViewOptions;

try (Viewer viewer = new Viewer("contract.docx")) {
    // {0} is replaced with the page number, so page 1 becomes page_1.html
    HtmlViewOptions viewOptions = HtmlViewOptions.forEmbeddedResources(
        "viewer-render-to-html/page_{0}.html");

    viewer.view(viewOptions);
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "viewer-render-to-html.zip" >}}  
```text
viewer-render-to-html/page_1.html (147 KB)
viewer-render-to-html/page_2.html (74 KB)
viewer-render-to-html/page_3.html (828 bytes)
```
[Download full output](/total/java/_output_files/developer-guide/viewer/ViewerRenderToHtml/viewer-render-to-html.zip)
{{< /tab >}}
{{< /tabs >}}

To keep resources as separate files next to the HTML instead of inlining them, use `HtmlViewOptions.forExternalResources` — useful when several pages share the same images and you want them cached once.

## Render a document to PDF

Rendering to PDF produces a single file, which is the usual choice for printing or archiving.

{{< tabs "viewer-render-to-pdf" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.viewer.Viewer;
import com.groupdocs.viewer.options.PdfViewOptions;

try (Viewer viewer = new Viewer("contract.docx")) {
    PdfViewOptions viewOptions = new PdfViewOptions("viewer-render-to-pdf.pdf");

    viewer.view(viewOptions);
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "viewer-render-to-pdf.pdf" >}}  
```text
Binary file (PDF, 126 KB)
```
[Download full output](/total/java/_output_files/developer-guide/viewer/ViewerRenderToPdf/viewer-render-to-pdf.pdf)
{{< /tab >}}
{{< /tabs >}}

## Render a document to PNG

Rendering to images gives you one PNG per page — the right output for thumbnails and previews. `PngViewOptions` also accepts a width and height if you need a fixed size.

{{< tabs "viewer-render-to-png" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.viewer.Viewer;
import com.groupdocs.viewer.options.PngViewOptions;

try (Viewer viewer = new Viewer("contract.docx")) {
    PngViewOptions viewOptions = new PngViewOptions("viewer-render-to-png/page_{0}.png");

    // Render only the first two pages
    viewer.view(viewOptions, 1, 2);
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "viewer-render-to-png.zip" >}}  
```text
viewer-render-to-png/page_1.png (86 KB)
viewer-render-to-png/page_2.png (87 KB)
```
[Download full output](/total/java/_output_files/developer-guide/viewer/ViewerRenderToPng/viewer-render-to-png.zip)
{{< /tab >}}
{{< /tabs >}}

## Read document information

Before rendering you often want to know what you are dealing with — how many pages, what format, whether it is encrypted. `getViewInfo` answers that without rendering anything.

{{< tabs "viewer-document-info" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.viewer.Viewer;
import com.groupdocs.viewer.options.ViewInfoOptions;
import com.groupdocs.viewer.results.Page;
import com.groupdocs.viewer.results.ViewInfo;

try (Viewer viewer = new Viewer("contract.docx")) {
    ViewInfoOptions viewInfoOptions = ViewInfoOptions.forHtmlView();
    ViewInfo viewInfo = viewer.getViewInfo(viewInfoOptions);

    System.out.println("File type: " + viewInfo.getFileType());
    System.out.println("Pages: " + viewInfo.getPages().size());

    for (Page page : viewInfo.getPages()) {
        System.out.println("Page " + page.getNumber() + ": " + page.getWidth() + "x" + page.getHeight());
    }
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
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
[Download full output](/total/java/_output_files/developer-guide/viewer/ViewerDocumentInfo/viewer-document-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Learn more

The examples above cover the common cases. GroupDocs.Viewer also renders archives, CAD drawings, email messages, Outlook data files and Visio diagrams, caches rendered output, and processes attachments.

* [GroupDocs.Viewer for Java documentation](https://docs.groupdocs.com/viewer/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/viewer/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/viewer/java/)
