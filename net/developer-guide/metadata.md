---
id: metadata
url: total/net/developer-guide/metadata
title: Read and edit metadata with GroupDocs.Metadata
linkTitle: Metadata
weight: 5
description: "Read, search and strip document metadata from GroupDocs.Total for .NET — runnable C# examples with downloadable input and output files."
keywords: GroupDocs.Metadata, document metadata, EXIF, XMP, read metadata, remove metadata, strip metadata, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Metadata reads and edits the metadata inside a document — authors, timestamps, EXIF and XMP tags, ID3 audio tags — without touching its visible content. Stripping metadata before a document leaves your organisation is the most common reason to reach for it.

## Read document information

`GetDocumentInfo` gives you the basics without loading the whole metadata tree.

{{< tabs "metadata-read-info" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Metadata;
using GroupDocs.Metadata.Common;

using (Metadata metadata = new Metadata("contract.docx"))
{
    IDocumentInfo info = metadata.GetDocumentInfo();

    Console.WriteLine("File format: " + info.FileType.FileFormat);
    Console.WriteLine("Extension: " + info.FileType.Extension);
    Console.WriteLine("MIME type: " + info.FileType.MimeType);
    Console.WriteLine("Pages: " + info.PageCount);
    Console.WriteLine("Size: " + info.Size + " bytes");
    Console.WriteLine("Encrypted: " + info.IsEncrypted);
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "metadata-read-info.txt" >}}  
```text
File format: WordProcessing
Extension: .docx
MIME type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
Pages: 3
Size: 15096 bytes
Encrypted: False
```
[Download full output](/total/net/_output_files/developer-guide/metadata/MetadataReadInfo/metadata-read-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Find metadata properties

Properties are searched with a predicate rather than by name, because the same idea is spelled differently in every format. Tags describe what a property *means*, so `Tags.Person.Creator` finds the author whether the file calls it `Author`, `Creator` or `dc:creator`.

{{< tabs "metadata-find-properties" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Metadata;
using GroupDocs.Metadata.Common;
using GroupDocs.Metadata.Tagging;

using (Metadata metadata = new Metadata("contract.docx"))
{
    // Every property tagged as identifying a person
    IEnumerable<MetadataProperty> properties = metadata.FindProperties(
        p => p.Tags.Contains(Tags.Person.Creator));

    foreach (MetadataProperty property in properties)
    {
        Console.WriteLine(property.Name + " = " + property.Value);
    }
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "metadata-find-properties.txt" >}}  
```text
Author = Dana Whitfield
dc:creator = Dana Whitfield
```
[Download full output](/total/net/_output_files/developer-guide/metadata/MetadataFindProperties/metadata-find-properties.txt)
{{< /tab >}}
{{< /tabs >}}

## Strip metadata before sharing

`Sanitize` removes every metadata property the format allows to be removed. This is the sanitising step to run before publishing a document externally.

{{< tabs "metadata-sanitize" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Metadata;

using (Metadata metadata = new Metadata("contract.docx"))
{
    int removed = metadata.Sanitize();
    Console.WriteLine("Properties removed: " + removed);

    metadata.Save("metadata-sanitize.docx");
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "metadata-sanitize.docx" >}}  
```text
Binary file (DOCX, 15 KB)
```
[Download full output](/total/net/_output_files/developer-guide/metadata/MetadataSanitize/metadata-sanitize.docx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Metadata also adds and updates properties, removes only the properties matching a predicate, and works with format-specific standards — EXIF, XMP and IPTC in images, ID3 and APE in audio, and the built-in and custom property sets of Office documents.

* [GroupDocs.Metadata for .NET documentation](https://docs.groupdocs.com/metadata/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/metadata/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/metadata/net/)
