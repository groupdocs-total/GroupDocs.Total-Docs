---
id: comparison
url: total/net/developer-guide/comparison
title: Compare documents with GroupDocs.Comparison
linkTitle: Comparison
weight: 3
description: "Find the differences between two versions of a document from GroupDocs.Total for .NET, list every change, and accept or reject them — runnable C# examples with downloadable files."
keywords: GroupDocs.Comparison, compare documents, document diff, track changes, accept reject changes, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Comparison finds the differences between two versions of a document and writes a result file with the changes marked up — insertions, deletions and style changes, down to word and character level.

The examples below compare two revisions of the same contract. `contract-v1.docx` and `contract-v2.docx` differ in exactly three places: the delivery date, the contract value, and a late-delivery clause added in v2.

The change count comes out higher than three, because GroupDocs.Comparison reports at word level and records a reworded sentence as a deletion plus an insertion rather than as one edit.

## Compare two documents

The source document goes to the constructor, the revision to `Add`, and `Compare` writes the marked-up result.

{{< tabs "comparison-compare-documents" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Comparison;

using (Comparer comparer = new Comparer("contract-v1.docx"))
{
    comparer.Add("contract-v2.docx");

    comparer.Compare("comparison-compare-documents.docx");
}
```
{{< /tab >}}
{{< tab "contract-v1.docx" >}}
{{< tab-text >}}
`contract-v1.docx` and `contract-v2.docx` are the sample files used in this example. Download [contract-v1.docx](/total/net/_sample_files/contract-v1.docx) and [contract-v2.docx](/total/net/_sample_files/contract-v2.docx).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "comparison-compare-documents.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/net/_output_files/developer-guide/comparison/ComparisonCompareDocuments/comparison-compare-documents.docx)
{{< /tab >}}
{{< /tabs >}}

In the result, inserted text is blue, deleted text is red and struck through, and style-only changes are green.

## List every change

`GetChanges` returns the differences as data rather than a document, which is what you want when the comparison feeds a review UI or an audit log rather than a human reader.

{{< tabs "comparison-list-changes" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Comparison;
using GroupDocs.Comparison.Result;

using (Comparer comparer = new Comparer("contract-v1.docx"))
{
    comparer.Add("contract-v2.docx");
    comparer.Compare();

    ChangeInfo[] changes = comparer.GetChanges();

    Console.WriteLine("Changes found: " + changes.Length);

    foreach (ChangeInfo change in changes)
    {
        Console.WriteLine(change.Id + ". " + change.Type
                          + " | source: '" + change.SourceText + "'"
                          + " | target: '" + change.TargetText + "'");
    }
}
```
{{< /tab >}}
{{< tab "contract-v1.docx" >}}
{{< tab-text >}}
`contract-v1.docx` and `contract-v2.docx` are the sample files used in this example. Download [contract-v1.docx](/total/net/_sample_files/contract-v1.docx) and [contract-v2.docx](/total/net/_sample_files/contract-v2.docx).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "comparison-list-changes.txt" >}}  
```text
Changes found: 7
0. Deleted | source: 'The vendor shall deliver the completed remediation plan by 30 June 2026.' | target: 'The vendor shall deliver the completed remediation plan by 31 August 2026.'
1. Inserted | source: 'The vendor shall deliver the completed remediation plan by 30 June 2026.' | target: 'The vendor shall deliver the completed remediation plan by 31 August 2026.'
2. Inserted | source: 'The vendor shall deliver the completed remediation plan by 30 June 2026.' | target: 'The vend
[TRUNCATED]
```
[Download full output](/total/net/_output_files/developer-guide/comparison/ComparisonListChanges/comparison-list-changes.txt)
{{< /tab >}}
{{< /tabs >}}

## Accept or reject individual changes

Each change carries a `ComparisonAction`. Set it to `Reject` and re-apply, and the result keeps the source wording for that change while accepting the rest — the API behind a review workflow.

{{< tabs "comparison-accept-reject" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Comparison;
using GroupDocs.Comparison.Result;

using (Comparer comparer = new Comparer("contract-v1.docx"))
{
    comparer.Add("contract-v2.docx");
    comparer.Compare();

    ChangeInfo[] changes = comparer.GetChanges();

    // Accept everything except the first change, which we reject
    foreach (ChangeInfo change in changes)
    {
        change.ComparisonAction = ComparisonAction.Accept;
    }
    if (changes.Length > 0)
    {
        changes[0].ComparisonAction = ComparisonAction.Reject;
        Console.WriteLine("Rejected: '" + changes[0].TargetText + "'");
    }

    comparer.ApplyChanges("comparison-accept-reject.docx", new ApplyChangeOptions
    {
        Changes = changes
    });
}
```
{{< /tab >}}
{{< tab "contract-v1.docx" >}}
{{< tab-text >}}
`contract-v1.docx` and `contract-v2.docx` are the sample files used in this example. Download [contract-v1.docx](/total/net/_sample_files/contract-v1.docx) and [contract-v2.docx](/total/net/_sample_files/contract-v2.docx).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "comparison-accept-reject.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/net/_output_files/developer-guide/comparison/ComparisonAcceptReject/comparison-accept-reject.docx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Comparison also compares more than two revisions at once, compares whole directories, produces a summary page, compares password-protected documents, and lets you tune sensitivity and the styling of each change type.

* [GroupDocs.Comparison for .NET documentation](https://docs.groupdocs.com/comparison/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/comparison/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/comparison/net/)
