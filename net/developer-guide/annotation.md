---
id: annotation
url: total/net/developer-guide/annotation
title: Annotate documents with GroupDocs.Annotation
linkTitle: Annotation
weight: 13
description: "Add area and text annotations to documents with GroupDocs.Total for .NET, and read back the annotations already on a file — runnable C# examples with downloadable files."
keywords: GroupDocs.Annotation, annotate document, PDF annotation, highlight text, document review, collaboration, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Annotation adds review markup to documents — areas, arrows, highlights, strikeouts, text fields, watermarks and threaded replies — and reads back the annotations already on a file. It is the API behind a document review or collaboration feature.

## Add an area annotation

An area annotation boxes a region of a page and attaches a comment to it. `Box` is the rectangle in points, and `PageNumber` is zero-based.

{{< tabs "annotation-add-area" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Annotation;
using GroupDocs.Annotation.Models;
using GroupDocs.Annotation.Models.AnnotationModels;

using (Annotator annotator = new Annotator("contract.pdf"))
{
    AreaAnnotation area = new AreaAnnotation
    {
        Box = new Rectangle(100, 100, 200, 100),
        BackgroundColor = 65535,
        Message = "Please confirm these figures",
        PageNumber = 0,
        Opacity = 0.7
    };

    annotator.Add(area);
    annotator.Save("annotation-add-area.pdf");
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "annotation-add-area.pdf" >}}  
```text
Binary file (PDF, 130 KB)
```
[Download full output](/total/net/_output_files/developer-guide/annotation/AnnotationAddArea/annotation-add-area.pdf)
{{< /tab >}}
{{< /tabs >}}

{{< alert style="info" >}}
Colours are 32-bit integers, not `Color` values — `65535` is yellow. `PageNumber` counts from zero, so the first page is `0`.
{{< /alert >}}

## Highlight text

A highlight annotation is bounded by four corner `Points` rather than a rectangle, because a highlight can follow text that wraps across lines and is not always a neat box.

{{< tabs "annotation-highlight" >}}
{{< tab "C#" >}}
```csharp
using System.Collections.Generic;
using GroupDocs.Annotation;
using GroupDocs.Annotation.Models;
using GroupDocs.Annotation.Models.AnnotationModels;

using (Annotator annotator = new Annotator("contract.pdf"))
{
    HighlightAnnotation highlight = new HighlightAnnotation
    {
        // Corner points of the region to highlight
        Points = new List<Point>
        {
            new Point(80, 730),
            new Point(240, 730),
            new Point(80, 710),
            new Point(240, 710)
        },
        BackgroundColor = 65535,
        Message = "Check this clause against the contract",
        PageNumber = 0,
        Opacity = 0.5
    };

    annotator.Add(highlight);
    annotator.Save("annotation-highlight.pdf");
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "annotation-highlight.pdf" >}}  
```text
Binary file (PDF, 132 KB)
```
[Download full output](/total/net/_output_files/developer-guide/annotation/AnnotationHighlight/annotation-highlight.pdf)
{{< /tab >}}
{{< /tabs >}}

## Read annotations back

`Get` returns the annotations already on a document — how you load an existing review into your own UI.

{{< tabs "annotation-extract" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.Collections.Generic;
using GroupDocs.Annotation;
using GroupDocs.Annotation.Models;
using GroupDocs.Annotation.Models.AnnotationModels;

// Annotate first, so there is something to read back
using (Annotator annotator = new Annotator("contract.pdf"))
{
    annotator.Add(new AreaAnnotation
    {
        Box = new Rectangle(100, 100, 200, 100),
        Message = "Please confirm these figures",
        PageNumber = 0
    });
    annotator.Save("annotation-extract.pdf");
}

using (Annotator annotator = new Annotator("annotation-extract.pdf"))
{
    List<AnnotationBase> annotations = annotator.Get();

    Console.WriteLine("Annotations found: " + annotations.Count);

    foreach (AnnotationBase annotation in annotations)
    {
        Console.WriteLine(annotation.GetType().Name
                          + " on page " + annotation.PageNumber
                          + ": " + annotation.Message);
    }
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "annotation-extract.pdf" >}}  
```text
Binary file (PDF, 130 KB)
```
[Download full output](/total/net/_output_files/developer-guide/annotation/AnnotationExtract/annotation-extract.pdf)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Annotation supports eighteen annotation types, threaded replies for multi-round review, updating and removing existing annotations, importing and exporting annotations as XML, page previews, and document version history.

* [GroupDocs.Annotation for .NET documentation](https://docs.groupdocs.com/annotation/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/annotation/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/annotation/net/)
