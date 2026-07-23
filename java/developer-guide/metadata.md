---
id: metadata
url: total/java/developer-guide/metadata
title: Read and edit metadata with GroupDocs.Metadata
linkTitle: Metadata
weight: 5
description: "Read, search and strip document metadata from GroupDocs.Total for Java — runnable Java examples with downloadable input and output files."
keywords: GroupDocs.Metadata, document metadata, EXIF, XMP, read metadata, remove metadata, strip metadata, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Metadata reads and edits the metadata inside a document — authors, timestamps, EXIF and XMP tags, ID3 audio tags — without touching its visible content. Stripping metadata before a document leaves your organisation is the most common reason to reach for it.

Each example below is ready to copy into a project once you have [installed the package]({{< ref "/total/java/getting-started/installation.md" >}}).

## Read document information

`getDocumentInfo` gives you the basics without loading the whole metadata tree.

{{< tabs "metadata-read-info" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.metadata.Metadata;
import com.groupdocs.metadata.core.IDocumentInfo;

try (Metadata metadata = new Metadata("contract.docx")) {
    IDocumentInfo info = metadata.getDocumentInfo();

    System.out.println("File format: " + info.getFileType().getFileFormat());
    System.out.println("Extension: " + info.getFileType().getExtension());
    System.out.println("MIME type: " + info.getFileType().getMimeType());
    System.out.println("Pages: " + info.getPageCount());
    System.out.println("Size: " + info.getSize() + " bytes");
    System.out.println("Encrypted: " + info.isEncrypted());
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "metadata-read-info.txt" >}}  
```text
File format: WordProcessing
Extension: .docx
MIME type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
Pages: 3
Size: 15096 bytes
Encrypted: false
```
[Download full output](/total/java/_output_files/developer-guide/metadata/MetadataReadInfo/metadata-read-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Find metadata properties

Properties are searched with a specification rather than by name, because the same idea is spelled differently in every format. Tags describe what a property *means*, so `Tags.getPerson().getCreator()` finds the author whether the file calls it `Author`, `Creator` or `dc:creator`.

{{< tabs "metadata-find-properties" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.metadata.Metadata;
import com.groupdocs.metadata.core.MetadataProperty;
import com.groupdocs.metadata.search.ContainsTagSpecification;
import com.groupdocs.metadata.tagging.Tags;

try (Metadata metadata = new Metadata("contract.docx")) {
    // Every property tagged as identifying the person who created the document
    Iterable<MetadataProperty> properties = metadata.findProperties(
        new ContainsTagSpecification(Tags.getPerson().getCreator()));

    for (MetadataProperty property : properties) {
        System.out.println(property.getName() + " = " + property.getValue());
    }
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "metadata-find-properties.txt" >}}  
```text
Author = Dana Whitfield
dc:creator = Dana Whitfield
```
[Download full output](/total/java/_output_files/developer-guide/metadata/MetadataFindProperties/metadata-find-properties.txt)
{{< /tab >}}
{{< /tabs >}}

## Strip metadata before sharing

`sanitize` removes every metadata property the format allows to be removed. This is the sanitising step to run before publishing a document externally.

{{< tabs "metadata-sanitize" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.metadata.Metadata;

try (Metadata metadata = new Metadata("contract.docx")) {
    int removed = metadata.sanitize();
    System.out.println("Properties removed: " + removed);

    metadata.save("metadata-sanitize.docx");
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "metadata-sanitize.docx" >}}  
```text
Binary file (DOCX, 14 KB)
```
[Download full output](/total/java/_output_files/developer-guide/metadata/MetadataSanitize/metadata-sanitize.docx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Metadata also adds and updates properties, removes only the properties matching a specification, and works with format-specific standards — EXIF, XMP and IPTC in images, ID3 and APE in audio, and the built-in and custom property sets of Office documents.

* [GroupDocs.Metadata for Java documentation](https://docs.groupdocs.com/metadata/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/metadata/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/metadata/java/)
