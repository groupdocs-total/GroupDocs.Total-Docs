---
id: redaction
url: total/net/developer-guide/redaction
title: Redact documents with GroupDocs.Redaction
linkTitle: Redaction
weight: 9
description: "Remove sensitive text and metadata from documents with GroupDocs.Total for .NET — runnable C# examples with downloadable input and output files."
keywords: GroupDocs.Redaction, redact document, remove sensitive data, redact PDF, GDPR, data privacy, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Redaction removes sensitive information from a document rather than merely hiding it — the redacted text is gone from the file, not covered by a black box you can drag away. It redacts text, metadata, annotations and image regions, and can rasterise the result to PDF so the original content cannot be recovered.

## Redact an exact phrase

`ExactPhraseRedaction` replaces every occurrence of a phrase. `ReplacementOptions` decides what takes its place. The contract names its engagement `Project Northlight` in the body — that codename is what a redacted copy has to lose.

{{< tabs "redaction-exact-phrase" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.IO;
using GroupDocs.Redaction;
using GroupDocs.Redaction.Options;
using GroupDocs.Redaction.Redactions;

using (Redactor redactor = new Redactor("contract-v1.docx"))
{
    RedactorChangeLog result = redactor.Apply(
        new ExactPhraseRedaction("Project Northlight", new ReplacementOptions("[REDACTED]")));

    Console.WriteLine("Status: " + result.Status);

    if (result.Status != RedactionStatus.Failed)
    {
        // Save() has no path overload: SaveOptions writes back over the source.
        // Write to a stream to keep the original intact.
        using (FileStream output = File.Create("redaction-exact-phrase.docx"))
        {
            redactor.Save(output, new RasterizationOptions { Enabled = false });
        }
    }
}
```
{{< /tab >}}
{{< tab "contract-v1.docx" >}}
{{< tab-text >}}
`contract-v1.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract-v1.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "redaction-exact-phrase.docx" >}}  
```text
Binary file (DOCX, 15 KB)
```
[Download full output](/total/net/_output_files/developer-guide/redaction/RedactionExactPhrase/redaction-exact-phrase.docx)
{{< /tab >}}
{{< /tabs >}}

## Redact by regular expression

A regex redaction catches patterns rather than literals — account numbers, amounts, email addresses — which is what most compliance rules are actually written against.

{{< tabs "redaction-regex" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.IO;
using GroupDocs.Redaction;
using GroupDocs.Redaction.Options;
using GroupDocs.Redaction.Redactions;

using (Redactor redactor = new Redactor("contract-v1.docx"))
{
    // Any currency amount such as "120,000 USD"
    RedactorChangeLog result = redactor.Apply(
        new RegexRedaction(@"\d{1,3}(,\d{3})*\s?USD", new ReplacementOptions("[AMOUNT]")));

    Console.WriteLine("Status: " + result.Status);

    if (result.Status != RedactionStatus.Failed)
    {
        // Save() has no path overload: SaveOptions writes back over the source.
        // Write to a stream to keep the original intact.
        using (FileStream output = File.Create("redaction-regex.docx"))
        {
            redactor.Save(output, new RasterizationOptions { Enabled = false });
        }
    }
}
```
{{< /tab >}}
{{< tab "contract-v1.docx" >}}
{{< tab-text >}}
`contract-v1.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract-v1.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "redaction-regex.docx" >}}  
```text
Binary file (DOCX, 15 KB)
```
[Download full output](/total/net/_output_files/developer-guide/redaction/RedactionRegex/redaction-regex.docx)
{{< /tab >}}
{{< /tabs >}}

## Erase metadata

Redacting the visible text is only half the job — the author, the revision history and the original filename usually live in the metadata. `EraseMetadataRedaction` clears them.

{{< tabs "redaction-metadata" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.IO;
using GroupDocs.Redaction;
using GroupDocs.Redaction.Options;
using GroupDocs.Redaction.Redactions;

using (Redactor redactor = new Redactor("contract-v1.docx"))
{
    RedactorChangeLog result = redactor.Apply(
        new EraseMetadataRedaction(MetadataFilters.All));

    Console.WriteLine("Status: " + result.Status);

    if (result.Status != RedactionStatus.Failed)
    {
        // Save() has no path overload: SaveOptions writes back over the source.
        // Write to a stream to keep the original intact.
        using (FileStream output = File.Create("redaction-metadata.docx"))
        {
            redactor.Save(output, new RasterizationOptions { Enabled = false });
        }
    }
}
```
{{< /tab >}}
{{< tab "contract-v1.docx" >}}
{{< tab-text >}}
`contract-v1.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract-v1.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "redaction-metadata.docx" >}}  
```text
Binary file (DOCX, 15 KB)
```
[Download full output](/total/net/_output_files/developer-guide/redaction/RedactionMetadata/redaction-metadata.docx)
{{< /tab >}}
{{< /tabs >}}

{{< alert style="tip" >}}
Setting `Enabled = true` on `RasterizationOptions` converts each page to an image inside a PDF. It is the strongest option — no text layer survives for anyone to recover — at the cost of the result no longer being searchable or editable. The `SaveOptions` overload spells the same thing `RasterizeToPDF`.
{{< /alert >}}

## Learn more

GroupDocs.Redaction also redacts image areas, deletes or rewrites annotations, removes whole pages, applies several redactions in one pass, and supports custom redaction policies loaded from configuration.

* [GroupDocs.Redaction for .NET documentation](https://docs.groupdocs.com/redaction/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/redaction/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/redaction/net/)
