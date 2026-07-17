---
id: merger
url: total/net/developer-guide/merger
title: Merge and split documents with GroupDocs.Merger
linkTitle: Merger
weight: 7
description: "Join documents, extract pages and read document information from GroupDocs.Total for .NET — runnable C# examples with downloadable input and output files."
keywords: GroupDocs.Merger, merge documents, join PDF, split document, extract pages, combine files, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Merger combines documents and rearranges their pages — join, split, extract, remove, reorder, rotate — and manages document passwords. It works on Word, PDF, spreadsheets, presentations, images and archives.

{{< alert style="warning" >}}
**`Save` needs an absolute output path.** Given a relative one it does nothing at all — no file, no exception, no error code:

```csharp
merger.Save("merged.docx");                    // returns cleanly, writes nothing
merger.Save(Path.GetFullPath("merged.docx"));  // writes the file
```

Input paths passed to the constructor and to `Join` may be relative. Only the output path must be absolute, which is why every example below wraps it in `Path.GetFullPath`.
{{< /alert >}}

## Join two documents

`Join` appends another document to the one you opened. Call it repeatedly to combine several, then `Save`.

{{< tabs "merger-join-documents" >}}
{{< tab "C#" >}}
```csharp
using System.IO;
using GroupDocs.Merger;

using (Merger merger = new Merger("contract.docx"))
{
    merger.Join("statement-of-work.docx");

    merger.Save(Path.GetFullPath("merger-join-documents.docx"));
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` and `statement-of-work.docx` are the sample files used in this example. Download [contract.docx](/total/net/_sample_files/contract.docx) and [statement-of-work.docx](/total/net/_sample_files/statement-of-work.docx).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "merger-join-documents.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/net/_output_files/developer-guide/merger/MergerJoinDocuments/merger-join-documents.docx)
{{< /tab >}}
{{< /tabs >}}

## Extract a page range

`ExtractPages` keeps only the pages you name and discards the rest — useful for pulling a signed section or an appendix out of a long document.

{{< tabs "merger-extract-pages" >}}
{{< tab "C#" >}}
```csharp
using System.IO;
using GroupDocs.Merger;
using GroupDocs.Merger.Domain.Options;

using (Merger merger = new Merger("contract.pdf"))
{
    // Keep pages 1 to 3
    ExtractOptions extractOptions = new ExtractOptions(1, 3);

    merger.ExtractPages(extractOptions);
    merger.Save(Path.GetFullPath("merger-extract-pages.pdf"));
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "merger-extract-pages.pdf" >}}  
```text
Binary file (PDF, 127 KB)
```
[Download full output](/total/net/_output_files/developer-guide/merger/MergerExtractPages/merger-extract-pages.pdf)
{{< /tab >}}
{{< /tabs >}}

## Read document information

`GetDocumentInfo` reports the format, page count and page dimensions — worth checking before you extract a range that may not exist.

{{< tabs "merger-document-info" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Merger;
using GroupDocs.Merger.Domain.Result;

using (Merger merger = new Merger("contract.pdf"))
{
    IDocumentInfo info = merger.GetDocumentInfo();

    Console.WriteLine("File type: " + info.Type.FileFormat);
    Console.WriteLine("Pages: " + info.PageCount);
    Console.WriteLine("Size: " + info.Size + " bytes");
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "merger-document-info.txt" >}}  
```text
File type: Portable Document Format File
Pages: 3
Size: 130412 bytes
```
[Download full output](/total/net/_output_files/developer-guide/merger/MergerDocumentInfo/merger-document-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Merger also splits one document into several, removes, moves, swaps and rotates pages, changes page orientation, adds, updates and removes document passwords, generates page previews, and offers a fluent API for chaining operations.

* [GroupDocs.Merger for .NET documentation](https://docs.groupdocs.com/merger/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/merger/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/merger/net/)
