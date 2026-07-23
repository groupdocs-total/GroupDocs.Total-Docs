---
id: redaction
url: total/java/developer-guide/redaction
title: Redact documents with GroupDocs.Redaction
linkTitle: Redaction
weight: 8
description: "Remove sensitive text, patterns and metadata from documents with GroupDocs.Total for Java, with runnable Java examples and downloadable input and output files."
keywords: GroupDocs.Redaction, redact document, remove sensitive data, redact Word, GDPR, data privacy, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Redaction removes sensitive information from a document rather than merely hiding it — the redacted text is gone from the file, not covered by a black box you can drag away. It redacts text, metadata, annotations and image regions, and can rasterise the result to PDF so the original content cannot be recovered.

Every example below opens `contract.docx` and is ready to copy into a project once you have [installed the package]({{< ref "/total/java/getting-started/installation.md" >}}).

## Redact an exact phrase

`ExactPhraseRedaction` replaces every occurrence of a phrase, and `ReplacementOptions` decides what takes its place. The contract names its engagement `Project Northlight` in the body — that codename is what a redacted copy has to lose.

{{< tabs "redaction-exact-phrase" >}}
{{< tab "Java" >}}
```java
import java.io.FileOutputStream;
import com.groupdocs.redaction.RedactionStatus;
import com.groupdocs.redaction.Redactor;
import com.groupdocs.redaction.RedactorChangeLog;
import com.groupdocs.redaction.options.RasterizationOptions;
import com.groupdocs.redaction.redactions.ExactPhraseRedaction;
import com.groupdocs.redaction.redactions.ReplacementOptions;

try (Redactor redactor = new Redactor("contract.docx")) {
    RedactorChangeLog result = redactor.apply(
        new ExactPhraseRedaction("Project Northlight", new ReplacementOptions("[REDACTED]")));

    System.out.println("Status: " + result.getStatus());

    if (result.getStatus() != RedactionStatus.Failed) {
        // save() with no path overwrites the source, so write to a new file via a stream.
        // Rasterization stays off to keep the result an editable DOCX.
        RasterizationOptions rasterizationOptions = new RasterizationOptions();
        rasterizationOptions.setEnabled(false);
        try (FileOutputStream output = new FileOutputStream("redaction-exact-phrase.docx")) {
            redactor.save(output, rasterizationOptions);
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
{{< tab "redaction-exact-phrase.docx" >}}  
```text
Binary file (DOCX, 15 KB)
```
[Download full output](/total/java/_output_files/developer-guide/redaction/RedactionExactPhrase/redaction-exact-phrase.docx)
{{< /tab >}}
{{< /tabs >}}

## Redact by regular expression

A regex redaction catches patterns rather than literals — account numbers, amounts, email addresses — which is what most compliance rules are actually written against. The contract's fee, `120,000 USD`, is exactly the kind of figure to strip.

{{< tabs "redaction-regex" >}}
{{< tab "Java" >}}
```java
import java.io.FileOutputStream;
import com.groupdocs.redaction.RedactionStatus;
import com.groupdocs.redaction.Redactor;
import com.groupdocs.redaction.RedactorChangeLog;
import com.groupdocs.redaction.options.RasterizationOptions;
import com.groupdocs.redaction.redactions.RegexRedaction;
import com.groupdocs.redaction.redactions.ReplacementOptions;

try (Redactor redactor = new Redactor("contract.docx")) {
    // Any currency amount such as "120,000 USD"
    RedactorChangeLog result = redactor.apply(
        new RegexRedaction("\\d{1,3}(,\\d{3})*\\s?USD", new ReplacementOptions("[AMOUNT]")));

    System.out.println("Status: " + result.getStatus());

    if (result.getStatus() != RedactionStatus.Failed) {
        RasterizationOptions rasterizationOptions = new RasterizationOptions();
        rasterizationOptions.setEnabled(false);
        try (FileOutputStream output = new FileOutputStream("redaction-regex.docx")) {
            redactor.save(output, rasterizationOptions);
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
{{< tab "redaction-regex.docx" >}}  
```text
Binary file (DOCX, 15 KB)
```
[Download full output](/total/java/_output_files/developer-guide/redaction/RedactionRegex/redaction-regex.docx)
{{< /tab >}}
{{< /tabs >}}

## Erase metadata

Redacting the visible text is only half the job — the author, the revision history and the original filename usually live in the metadata. `EraseMetadataRedaction` clears them.

{{< tabs "redaction-metadata" >}}
{{< tab "Java" >}}
```java
import java.io.FileOutputStream;
import com.groupdocs.redaction.RedactionStatus;
import com.groupdocs.redaction.Redactor;
import com.groupdocs.redaction.RedactorChangeLog;
import com.groupdocs.redaction.options.RasterizationOptions;
import com.groupdocs.redaction.redactions.EraseMetadataRedaction;
import com.groupdocs.redaction.redactions.MetadataFilters;

try (Redactor redactor = new Redactor("contract.docx")) {
    RedactorChangeLog result = redactor.apply(
        new EraseMetadataRedaction(MetadataFilters.All));

    System.out.println("Status: " + result.getStatus());

    if (result.getStatus() != RedactionStatus.Failed) {
        RasterizationOptions rasterizationOptions = new RasterizationOptions();
        rasterizationOptions.setEnabled(false);
        try (FileOutputStream output = new FileOutputStream("redaction-metadata.docx")) {
            redactor.save(output, rasterizationOptions);
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
{{< tab "redaction-metadata.docx" >}}  
```text
Binary file (DOCX, 14 KB)
```
[Download full output](/total/java/_output_files/developer-guide/redaction/RedactionMetadata/redaction-metadata.docx)
{{< /tab >}}
{{< /tabs >}}

Turning rasterization on with `rasterizationOptions.setEnabled(true)` converts each page to an image inside a PDF. It is the strongest option — no text layer survives for anyone to recover — at the cost of a result that is no longer searchable or editable.

## Learn more

GroupDocs.Redaction also redacts image areas, deletes or rewrites annotations, removes whole pages, applies several redactions in one pass, and supports custom redaction policies loaded from configuration.

* [GroupDocs.Redaction for Java documentation](https://docs.groupdocs.com/redaction/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/redaction/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/redaction/java/)
