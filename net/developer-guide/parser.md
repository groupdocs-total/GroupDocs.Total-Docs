---
id: parser
url: total/net/developer-guide/parser
title: Extract data with GroupDocs.Parser
linkTitle: Parser
weight: 6
description: "Extract text, images and metadata from documents with GroupDocs.Total for .NET — runnable C# examples with downloadable input and output files."
keywords: GroupDocs.Parser, extract text, extract images, parse PDF, text extraction, data extraction, RAG, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Parser pulls content out of documents — plain text, formatted text, images, metadata, hyperlinks, tables and barcodes — across PDF, Word, spreadsheets, presentations, email, ebooks and archives. It is the usual first step when feeding documents to a search index or a language model.

## Extract text from a document

`GetText` returns a `TextReader`. It returns `null` rather than throwing when the format does not support text extraction, so check it.

{{< tabs "parser-extract-text" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.IO;
using GroupDocs.Parser;

using (Parser parser = new Parser("contract.pdf"))
{
    using (TextReader reader = parser.GetText())
    {
        if (reader == null)
        {
            Console.WriteLine("Text extraction is not supported for this format.");
        }
        else
        {
            Console.WriteLine(reader.ReadToEnd());
        }
    }
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "parser-extract-text.txt" >}}  
```text
Consulting Services Agreement
Cascade Partners and Aldergrove Manufacturing
This agreement records the terms under which Cascade Partners will deliver the engagement
known internally as Project Northlight. It is issued by Dana Whitfield, Engagement Lead, and
countersigned by Marcus Oyelaran.

1. Scope of work
Cascade Partners will review the current order-to-cash process at Aldergrove Manufacturing,
identify the constraints limiting throughput, and deliver a prioritised remediation plan with an

[TRUNCATED]
```
[Download full output](/total/net/_output_files/developer-guide/parser/ParserExtractText/parser-extract-text.txt)
{{< /tab >}}
{{< /tabs >}}

## Extract text as Markdown

Formatted extraction keeps the document's structure — headings, lists, emphasis — instead of flattening it. Markdown is the format to ask for when the text is destined for a language model.

{{< tabs "parser-extract-markdown" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.IO;
using GroupDocs.Parser;
using GroupDocs.Parser.Options;

using (Parser parser = new Parser("contract.docx"))
{
    using (TextReader reader = parser.GetFormattedText(
        new FormattedTextOptions(FormattedTextMode.Markdown)))
    {
        if (reader == null)
        {
            Console.WriteLine("Formatted extraction is not supported for this format.");
        }
        else
        {
            File.WriteAllText("parser-extract-markdown.md", reader.ReadToEnd());
        }
    }
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "parser-extract-markdown.md" >}}  
```text
**Consulting Services Agreement**

Cascade Partners and Aldergrove Manufacturing

This agreement records the terms under which Cascade Partners will deliver the engagement known internally as Project Northlight. It is issued by Dana Whitfield, Engagement Lead, and countersigned by Marcus Oyelaran.

# **1. Scope of work**

Cascade Partners will review the current order-to-cash process at Aldergrove Manufacturing, identify the constraints limiting throughput, and deliver a prioritised remediation 
[TRUNCATED]
```
[Download full output](/total/net/_output_files/developer-guide/parser/ParserExtractMarkdown/parser-extract-markdown.md)
{{< /tab >}}
{{< /tabs >}}

{{< alert style="info" >}}
Formatted extraction is not available for every format — **PDF returns `null`** from `GetFormattedText`, where plain `GetText` works fine. That is why the snippet checks the reader instead of assuming it. Word documents support Markdown, HTML and plain-text modes.
{{< /alert >}}

## Read document information

`GetDocumentInfo` reports the page count and format before you commit to extracting anything.

{{< tabs "parser-document-info" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Parser;
using GroupDocs.Parser.Options;

using (Parser parser = new Parser("contract.pdf"))
{
    IDocumentInfo info = parser.GetDocumentInfo();

    Console.WriteLine("File type: " + info.FileType);
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
{{< tab "parser-document-info.txt" >}}  
```text
File type: Portable Document Format File(.pdf)
Pages: 3
Size: 130412 bytes
```
[Download full output](/total/net/_output_files/developer-guide/parser/ParserDocumentInfo/parser-document-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Parser also extracts images, hyperlinks, tables of contents and barcodes, parses structured data with user-defined templates, reads PDF form values, and reaches into email attachments and ZIP archives.

* [GroupDocs.Parser for .NET documentation](https://docs.groupdocs.com/parser/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/parser/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/parser/net/)
