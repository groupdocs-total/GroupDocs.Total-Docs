---
id: comparison
url: total/nodejs-java/developer-guide/comparison
title: Compare documents with GroupDocs.Comparison
linkTitle: Comparison
weight: 3
description: "Find the differences between two versions of a document from GroupDocs.Total for Node.js via Java, list every change, and accept or reject them — runnable JavaScript examples with downloadable files."
keywords: GroupDocs.Comparison, compare documents, document diff, track changes, accept reject changes, Node.js
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

GroupDocs.Comparison finds the differences between two versions of a document and writes a result file with the changes marked up — insertions, deletions and style changes, down to word and character level.

The examples below compare two revisions of the same contract. `contract-v1.docx` and `contract-v2.docx` differ in exactly three places: the delivery date, the contract value, and a late-delivery clause added in v2. Each example is ready to copy into a project once you have [installed the package]({{< ref "/total/nodejs-java/getting-started/installation.md" >}}).

The change count comes out higher than three, because GroupDocs.Comparison reports at word level and records a reworded sentence as a deletion plus an insertion rather than as one edit.

## Compare two documents

The source document goes to the constructor, the revision to `add`, and `compare` writes the marked-up result.

{{< tabs "comparison-compare-documents" >}}
{{< tab "JavaScript" >}}
```js
import { Comparer } from '@groupdocs/groupdocs.total';

const comparer = new Comparer('contract-v1.docx');
comparer.add('contract-v2.docx');

comparer.compare('comparison-compare-documents.docx');
comparer.close();
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`contract-v1.docx` and `contract-v2.docx` are the sample files used in this example. Download [contract-v1.docx](/total/nodejs-java/_sample_files/contract-v1.docx) and [contract-v2.docx](/total/nodejs-java/_sample_files/contract-v2.docx).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "comparison-compare-documents.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/comparison/ComparisonCompareDocuments/comparison-compare-documents.docx)
{{< /tab >}}
{{< /tabs >}}

In the result, inserted text is blue, deleted text is red and struck through, and style-only changes are green.

## List every change

`getChanges` returns the differences as data rather than a document, which is what you want when the comparison feeds a review UI or an audit log rather than a human reader.

{{< tabs "comparison-list-changes" >}}
{{< tab "JavaScript" >}}
```js
import { Comparer } from '@groupdocs/groupdocs.total';

const comparer = new Comparer('contract-v1.docx');
comparer.add('contract-v2.docx');
comparer.compare();

const changes = comparer.getChanges();

console.log('Changes found: ' + changes.length);

for (const change of changes) {
  console.log(change.getId() + '. ' + change.getType()
    + ' | source: \'' + change.getSourceText() + '\''
    + ' | target: \'' + change.getTargetText() + '\'');
}

comparer.close();
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`contract-v1.docx` and `contract-v2.docx` are the sample files used in this example. Download [contract-v1.docx](/total/nodejs-java/_sample_files/contract-v1.docx) and [contract-v2.docx](/total/nodejs-java/_sample_files/contract-v2.docx).
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
[Download full output](/total/nodejs-java/_output_files/developer-guide/comparison/ComparisonListChanges/comparison-list-changes.txt)
{{< /tab >}}
{{< /tabs >}}

## Accept or reject individual changes

Each change carries a `ComparisonAction`. Set it to `REJECT` and re-apply, and the result keeps the source wording for that change while accepting the rest — the API behind a review workflow.

{{< tabs "comparison-accept-reject" >}}
{{< tab "JavaScript" >}}
```js
import { Comparer } from '@groupdocs/groupdocs.total';
import java from 'java';

const ComparisonAction = java.import('com.groupdocs.comparison.result.ComparisonAction');
const ApplyChangeOptions = java.import('com.groupdocs.comparison.options.ApplyChangeOptions');

const comparer = new Comparer('contract-v1.docx');
comparer.add('contract-v2.docx');
comparer.compare();

const changes = comparer.getChanges();

// Accept everything except the first change, which we reject
for (const change of changes) {
  change.setComparisonAction(ComparisonAction.ACCEPT);
}
if (changes.length > 0) {
  changes[0].setComparisonAction(ComparisonAction.REJECT);
  console.log('Rejected: \'' + changes[0].getTargetText() + '\'');
}

const changeArray = java.newArray('com.groupdocs.comparison.result.ChangeInfo', changes);
const applyOptions = new ApplyChangeOptions(changeArray);

comparer.applyChanges('comparison-accept-reject.docx', applyOptions);
comparer.close();
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`contract-v1.docx` and `contract-v2.docx` are the sample files used in this example. Download [contract-v1.docx](/total/nodejs-java/_sample_files/contract-v1.docx) and [contract-v2.docx](/total/nodejs-java/_sample_files/contract-v2.docx).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "comparison-accept-reject.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/comparison/ComparisonAcceptReject/comparison-accept-reject.docx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Comparison also compares more than two revisions at once, compares whole directories, produces a summary page, compares password-protected documents, and lets you tune sensitivity and the styling of each change type.

* [GroupDocs.Comparison for Node.js via Java documentation](https://docs.groupdocs.com/comparison/nodejs-java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/comparison/nodejs-java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/comparison/java/)
