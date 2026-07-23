---
id: parser
url: total/java/developer-guide/parser
title: Extract data with GroupDocs.Parser
linkTitle: Parser
weight: 6
description: "Extract plain text, single pages, formatted Markdown and document information from Word, PDF and 170+ other formats with GroupDocs.Total for Java, with runnable Java examples and downloadable input and output files."
keywords: GroupDocs.Parser, extract text, extract Markdown, text extraction, data extraction, RAG, document parsing, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Parser pulls content out of documents — plain text, formatted text, images, metadata, hyperlinks, tables and barcodes — across PDF, Word, spreadsheets, presentations, email, ebooks and archives. It is the usual first step when feeding documents to a search index or a language model.

Every example below opens `contract.docx` and is ready to copy into a project once you have [installed the package]({{< ref "/total/java/getting-started/installation.md" >}}).

## Extract text from a document

`getText` returns a `TextReader`. It returns `null` rather than throwing when a format does not support text extraction, so check the reader before you read from it.

{{< tabs "parser-extract-text" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.parser.Parser;
import com.groupdocs.parser.data.TextReader;

try (Parser parser = new Parser("contract.docx")) {
    try (TextReader reader = parser.getText()) {
        if (reader == null) {
            System.out.println("Text extraction is not supported for this format.");
        } else {
            System.out.println(reader.readToEnd());
        }
    }
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "parser-extract-text.txt" >}}  
```text
Consulting Services Agreement
Cascade Partners and Aldergrove Manufacturing
This agreement records the terms under which Cascade Partners will deliver the engagement known internally as Project Northlight. It is issued by Dana Whitfield, Engagement Lead, and countersigned by Marcus Oyelaran.

1. Scope of work
Cascade Partners will review the current order-to-cash process at Aldergrove Manufacturing, identify the constraints limiting throughput, and deliver a prioritised remediation plan with an 
[TRUNCATED]
```
[Download full output](/total/java/_output_files/developer-guide/parser/ParserExtractText/parser-extract-text.txt)
{{< /tab >}}
{{< /tabs >}}

## Extract text from a single page

`getText` also accepts a zero-based page index, so you can pull one page out of a long document instead of reading the whole thing.

{{< tabs "parser-extract-page" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.parser.Parser;
import com.groupdocs.parser.data.TextReader;

try (Parser parser = new Parser("contract.docx")) {
    // Read the first page only; the page index is zero-based
    try (TextReader reader = parser.getText(0)) {
        if (reader == null) {
            System.out.println("Text extraction is not supported for this format.");
        } else {
            System.out.println(reader.readToEnd());
        }
    }
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "parser-extract-page.txt" >}}  
```text
Consulting Services Agreement
Cascade Partners and Aldergrove Manufacturing
This agreement records the terms under which Cascade Partners will deliver the engagement known internally as Project Northlight. It is issued by Dana Whitfield, Engagement Lead, and countersigned by Marcus Oyelaran.
1. Scope of work
Cascade Partners will review the current order-to-cash process at Aldergrove Manufacturing, identify the constraints limiting throughput, and deliver a prioritised remediation plan with an i
[TRUNCATED]
```
[Download full output](/total/java/_output_files/developer-guide/parser/ParserExtractPage/parser-extract-page.txt)
{{< /tab >}}
{{< /tabs >}}

## Extract text as Markdown

Formatted extraction keeps the document's structure — headings, lists, emphasis — instead of flattening it. Markdown is the format to ask for when the text is destined for a language model.

{{< tabs "parser-extract-markdown" >}}
{{< tab "Java" >}}
```java
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import com.groupdocs.parser.Parser;
import com.groupdocs.parser.data.TextReader;
import com.groupdocs.parser.options.FormattedTextMode;
import com.groupdocs.parser.options.FormattedTextOptions;

try (Parser parser = new Parser("contract.docx")) {
    try (TextReader reader = parser.getFormattedText(
            new FormattedTextOptions(FormattedTextMode.Markdown))) {
        if (reader == null) {
            System.out.println("Formatted extraction is not supported for this format.");
        } else {
            Files.write(Paths.get("parser-extract-markdown.md"),
                reader.readToEnd().getBytes(StandardCharsets.UTF_8));
        }
    }
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
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
[Download full output](/total/java/_output_files/developer-guide/parser/ParserExtractMarkdown/parser-extract-markdown.md)
{{< /tab >}}
{{< /tabs >}}

Formatted extraction is not available for every format — PDF returns `null` from `getFormattedText`, where plain `getText` works fine — which is why the snippet checks the reader first. Word documents support Markdown, HTML and plain-text modes.

## Read document information

`getDocumentInfo` reports the format and page count before you commit to extracting anything.

{{< tabs "parser-document-info" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.parser.Parser;
import com.groupdocs.parser.options.IDocumentInfo;

try (Parser parser = new Parser("contract.docx")) {
    IDocumentInfo info = parser.getDocumentInfo();

    System.out.println("File type: " + info.getFileType().getFileFormat());
    System.out.println("Pages: " + info.getPageCount());
    System.out.println("Size: " + info.getSize() + " bytes");
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "parser-document-info.txt" >}}  
```text
File type: Microsoft Word Open XML Document
Pages: 3
Size: 15096 bytes
```
[Download full output](/total/java/_output_files/developer-guide/parser/ParserDocumentInfo/parser-document-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Parser also extracts images, hyperlinks, tables of contents and barcodes, parses structured data with user-defined templates, reads PDF form values, and reaches into email attachments and ZIP archives.

* [GroupDocs.Parser for Java documentation](https://docs.groupdocs.com/parser/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/parser/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/parser/java/)
