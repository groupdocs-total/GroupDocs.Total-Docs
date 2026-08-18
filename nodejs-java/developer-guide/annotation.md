---
id: annotation
url: total/nodejs-java/developer-guide/annotation
title: Annotate documents with GroupDocs.Annotation
linkTitle: Annotation
weight: 12
description: "Add area and highlight annotations to documents with GroupDocs.Total for Node.js via Java, and read back the annotations already on a file — runnable JavaScript examples with downloadable files."
keywords: GroupDocs.Annotation, annotate document, PDF annotation, highlight text, document review, collaboration, Node.js
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

GroupDocs.Annotation adds review markup to documents — areas, arrows, highlights, strikeouts, text fields, watermarks and threaded replies — and reads back the annotations already on a file. It is the API behind a document review or collaboration feature.

## Add an area annotation

An area annotation boxes a region of a page and attaches a comment to it. `setBox` takes the rectangle in points, and `setPageNumber` is zero-based.

{{< tabs "annotation-add-area" >}}
{{< tab "JavaScript" >}}
```js
import { Annotator } from '@groupdocs/groupdocs.total';
import java from 'java';

const AreaAnnotation = java.import(
  'com.groupdocs.annotation.models.annotationmodels.AreaAnnotation'
);
const Rectangle = java.import('com.groupdocs.annotation.models.Rectangle');

const annotator = new Annotator('contract.docx');

const area = new AreaAnnotation();
area.setBox(new Rectangle(100, 100, 200, 100));
area.setBackgroundColor(65535);
area.setMessage('Please confirm these figures');
area.setPageNumber(0);
area.setOpacity(0.7);

annotator.add(area);
annotator.save('annotation-add-area.pdf');
annotator.close();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "annotation-add-area.pdf" >}}  
```text
Binary file (PDF, 16 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/annotation/AnnotationAddArea/annotation-add-area.pdf)
{{< /tab >}}
{{< /tabs >}}

{{< alert style="info" >}}
Colours are 32-bit integers rather than `Color` objects — `65535` is yellow. `setPageNumber` counts from zero, so the first page is `0`.
{{< /alert >}}

## Highlight text

A highlight annotation is bounded by four corner points rather than a rectangle, because a highlight can follow text that wraps across lines and is not always a neat box.

{{< tabs "annotation-highlight" >}}
{{< tab "JavaScript" >}}
```js
import { Annotator } from '@groupdocs/groupdocs.total';
import java from 'java';

const HighlightAnnotation = java.import(
  'com.groupdocs.annotation.models.annotationmodels.HighlightAnnotation'
);
const Point = java.import('com.groupdocs.annotation.models.Point');
const ArrayList = java.import('java.util.ArrayList');

const annotator = new Annotator('contract.docx');

// Corner points of the region to highlight
const points = new ArrayList();
points.add(new Point(80, 730));
points.add(new Point(240, 730));
points.add(new Point(80, 710));
points.add(new Point(240, 710));

const highlight = new HighlightAnnotation();
highlight.setPoints(points);
highlight.setBackgroundColor(65535);
highlight.setMessage('Check this clause against the contract');
highlight.setPageNumber(0);
highlight.setOpacity(0.5);

annotator.add(highlight);
annotator.save('annotation-highlight.pdf');
annotator.close();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "annotation-highlight.pdf" >}}  
```text
Binary file (PDF, 15 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/annotation/AnnotationHighlight/annotation-highlight.pdf)
{{< /tab >}}
{{< /tabs >}}

## Read annotations back

`get` returns the annotations already on a document — how you load an existing review into your own UI.

{{< tabs "annotation-extract" >}}
{{< tab "JavaScript" >}}
```js
import { Annotator } from '@groupdocs/groupdocs.total';
import java from 'java';

const AreaAnnotation = java.import(
  'com.groupdocs.annotation.models.annotationmodels.AreaAnnotation'
);
const Rectangle = java.import('com.groupdocs.annotation.models.Rectangle');

// Annotate first, so there is something to read back
const annotator = new Annotator('contract.docx');
const area = new AreaAnnotation();
area.setBox(new Rectangle(100, 100, 200, 100));
area.setMessage('Please confirm these figures');
area.setPageNumber(0);

annotator.add(area);
annotator.save('annotation-extract.pdf');
annotator.close();

const reader = new Annotator('annotation-extract.pdf');
const annotations = reader.get();

console.log('Annotations found: ' + annotations.size());

for (let i = 0; i < annotations.size(); i++) {
  const item = annotations.get(i);
  console.log(item.getClass().getSimpleName()
    + ' on page ' + item.getPageNumber()
    + ': ' + item.getMessage());
}

reader.close();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "annotation-extract.pdf" >}}  
```text
Binary file (PDF, 16 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/annotation/AnnotationExtract/annotation-extract.pdf)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Annotation supports eighteen annotation types, threaded replies for multi-round review, updating and removing existing annotations, importing and exporting annotations as XML, page previews, and document version history.

* [GroupDocs.Annotation for Java documentation](https://docs.groupdocs.com/annotation/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/annotation/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/annotation/java/)
