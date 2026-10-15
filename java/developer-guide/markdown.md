---
id: markdown
url: total/java/developer-guide/markdown
title: Convert documents to Markdown with GroupDocs.Markdown
linkTitle: Markdown
weight: 9
description: "Convert Word, PDF and other documents to structured Markdown with GroupDocs.Total for Java, and read format, page count and metadata before converting — runnable Java examples with downloadable files."
keywords: GroupDocs.Markdown, convert to Markdown, DOCX to MD, PDF to Markdown, document to markdown, RAG, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Markdown converts documents into structured Markdown — headings, lists, tables and images — that you can hand to a static site or a language model. `MarkdownConverter` reads the source and either returns a string or writes a `.md` file.

Every example below is ready to copy into a project once you have [installed the package]({{< ref "/total/java/getting-started/installation.md" >}}).

## Convert Word to Markdown

`toFile` writes the Markdown next to the name you give it. `toMarkdown` returns the same result as a string when you want to keep it in memory.

{{< tabs "markdown-word" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.markdown.MarkdownConverter;

MarkdownConverter.toFile("business-plan.docx", "markdown-word.md");
```
{{< /tab >}}
{{< tab "business-plan.docx" >}}
{{< tab-text >}}
`business-plan.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/business-plan.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "markdown-word.md" >}}
```text
![](data:...;base64,[elided])

**Meridian Outdoor Co. — Business Plan**

FY2026 Strategic Plan


# **Table of Contents**

FY2026 Strategic Plan	1
[TRUNCATED]
```
[Download full output](/total/java/_output_files/developer-guide/markdown/MarkdownWordToFile/markdown-word.md)
{{< /tab >}}
{{< /tabs >}}

Images are embedded in the Markdown as Base64. The product guide shows how to write them to a folder instead, and how to pick GitHub Flavored Markdown or CommonMark.

## Convert PDF to Markdown

The same call works for PDF. Only the source file changes.

{{< tabs "markdown-pdf" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.markdown.MarkdownConverter;

MarkdownConverter.toFile("business-plan.pdf", "markdown-pdf.md");
```
{{< /tab >}}
{{< tab "business-plan.pdf" >}}
{{< tab-text >}}
`business-plan.pdf` is the sample file used in this example. Click [here](/total/java/_sample_files/business-plan.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "markdown-pdf.md" >}}
```text
**Meridian Outdoor Co. — Business Plan**

FY2026 Strategic Plan

![](data:...;base64,[elided])


**Table of Contents**

MeridianOutdoorCo.—BusinessPlan.........................................................................................1
[TRUNCATED]
```
[Download full output](/total/java/_output_files/developer-guide/markdown/MarkdownPdfToFile/markdown-pdf.md)
{{< /tab >}}
{{< /tabs >}}

## Read document information

`getInfo` reports the format, page count and metadata without converting the file.

{{< tabs "markdown-document-info" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.markdown.DocumentInfo;
import com.groupdocs.markdown.MarkdownConverter;

DocumentInfo info = MarkdownConverter.getInfo("business-plan.docx");

System.out.println("Format:    " + info.getFileFormat());
System.out.println("Pages:     " + info.getPageCount());
System.out.println("Title:     " + info.getTitle());
System.out.println("Author:    " + info.getAuthor());
System.out.println("Encrypted: " + info.isEncrypted());
```
{{< /tab >}}
{{< tab "business-plan.docx" >}}
{{< tab-text >}}
`business-plan.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/business-plan.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "markdown-document-info.txt" >}}
```text
Format:    DOCX
Pages:     5
Title:     Meridian Outdoor Co. — Business Plan
Author:    Meridian Outdoor Co.
Encrypted: false
```
[Download full output](/total/java/_output_files/developer-guide/markdown/MarkdownDocumentInfo/markdown-document-info.txt)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Markdown also converts spreadsheets, presentations, email, ebooks and plain text, limits how many spreadsheet rows and columns are exported, shifts heading levels, and can add YAML front matter from the document metadata.

* [GroupDocs.Markdown for Java documentation](https://docs.groupdocs.com/markdown/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/markdown/java/supported-file-formats/)
* [API reference](https://reference.groupdocs.com/markdown/java/)
