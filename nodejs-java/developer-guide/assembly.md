---
id: assembly
url: total/nodejs-java/developer-guide/assembly
title: Generate documents from templates with GroupDocs.Assembly
linkTitle: Assembly
weight: 8
description: "Fill a template from JSON, XML or a spreadsheet and generate a finished document with GroupDocs.Total for Node.js via Java — runnable JavaScript examples with downloadable templates and output."
keywords: GroupDocs.Assembly, document automation, report generation, Word template, mail merge, LINQ reporting, Node.js, JSON
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

GroupDocs.Assembly generates documents from a template and a data source. Unlike the rest of the suite it needs an input you have to author yourself: a **template** carrying `<<[...]>>` tags that say where the data goes.

`<<[expr]>>` inserts a value, `<<foreach [x in xs]>>…<</foreach>>` repeats a block, and expressions can compute. JSON, XML and spreadsheet fields are referred to by name, for example `Name` or `Client.Name`. The output format follows the output file's extension.

Import the package first, so the Total library is on the classpath, then load the Assembly classes with `java.import`.

{{< alert style="info" >}}
Plain JavaScript objects cannot be passed as data sources, because they are not Java objects. Where the Java documentation binds a custom class such as `Manager`, pass JSON, XML or CSV of the same shape, or a `DocumentTable`.
{{< /alert >}}

## Generate a document from JSON

`JsonDataSource` reads a JSON file. The name passed to `DataSourceInfo` is what the template iterates. `simple-dataset.docx` contains:

```text
<<foreach [in managers]>>Manager: <<[Name]>>
Contracts:
<<foreach [in Contract]>>- <<[Client.Name]>> ($<<[Price]>>)
<</foreach>>
<</foreach>>
```

The file's root is an array, so `foreach [in managers]` walks that array. Nested objects and arrays are reached by name: `Contract`, then `Client.Name`.

{{< tabs "assembly-from-json" >}}
{{< tab "JavaScript" >}}
```js
import '@groupdocs/groupdocs.total';
import java from 'java';

const DocumentAssembler = java.import('com.groupdocs.assembly.DocumentAssembler');
const JsonDataSource = java.import('com.groupdocs.assembly.JsonDataSource');
const DataSourceInfo = java.import('com.groupdocs.assembly.DataSourceInfo');

const managers = new JsonDataSource('manager-data.json');
const assembler = new DocumentAssembler();

assembler.assembleDocument(
  'simple-dataset.docx',
  'assembly-json.docx',
  new DataSourceInfo(managers, 'managers')
);
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`simple-dataset.docx` is the template and `manager-data.json` is the data. Download [simple-dataset.docx](/total/nodejs-java/_sample_files/simple-dataset.docx) and [manager-data.json](/total/nodejs-java/_sample_files/manager-data.json).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "assembly-json.docx" >}}
```text
Manager: John Smith
Contracts:
- A Company ($1200000)
- B Ltd. ($750000)
- C & D ($350000)
Manager: Tony Anderson
Contracts:
- E Corp. ($650000)
- F & Partners ($550000)
Manager: July James
Contracts:
- G & Co. ($350000)
- H Group ($250000)
- I & Sons ($100000)
- J Ent. ($100000)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/assembly/AssemblyAssembleJson/assembly-json.docx)
{{< /tab >}}
{{< /tabs >}}

The string argument of `JsonDataSource` is a file path. To assemble JSON held in memory, pass a Java `InputStream` instead.

## Generate a document from XML

`XmlDataSource` reads the same kind of structure from XML. The template above works unchanged when each manager is a `<Manager>` element and each contract is a nested `<Contract>`.

{{< tabs "assembly-from-xml" >}}
{{< tab "JavaScript" >}}
```js
import '@groupdocs/groupdocs.total';
import java from 'java';

const DocumentAssembler = java.import('com.groupdocs.assembly.DocumentAssembler');
const XmlDataSource = java.import('com.groupdocs.assembly.XmlDataSource');
const DataSourceInfo = java.import('com.groupdocs.assembly.DataSourceInfo');

const managers = new XmlDataSource('managers.xml');
const assembler = new DocumentAssembler();

assembler.assembleDocument(
  'simple-dataset.docx',
  'assembly-xml.docx',
  new DataSourceInfo(managers, 'managers')
);
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`simple-dataset.docx` is the template and `managers.xml` is the data. Download [simple-dataset.docx](/total/nodejs-java/_sample_files/simple-dataset.docx) and [managers.xml](/total/nodejs-java/_sample_files/managers.xml).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "assembly-xml.docx" >}}
```text
Manager: John Smith
Contracts:
- A Company ($1200000)
- B Ltd. ($750000)
- C & D ($350000)
Manager: Tony Anderson
Contracts:
- E Corp. ($650000)
- F & Partners ($550000)
Manager: July James
Contracts:
- G & Co. ($350000)
- H Group ($250000)
- I & Sons ($100000)
- J Ent. ($100000)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/assembly/AssemblyAssembleXml/assembly-xml.docx)
{{< /tab >}}
{{< /tabs >}}

## Generate a document from a spreadsheet

`DocumentTable` reads one worksheet as a table of rows. `setFirstRowContainsColumnNames(true)` takes the first row as the field names. A space in a heading becomes an underscore, so the column `Contract Price` is `Contract_Price` in the template.

`contracts-template.docx` groups those rows by manager and sums the prices:

```text
Total Contract Prices by Managers
Manager
Total Contract Price
<<foreach [group in contracts.groupBy(c => c.Manager).orderBy(g => g.key)]>><<[group.key]>>
<<[group.sum(c => c.Contract_Price)]>><</foreach>>
```

{{< tabs "assembly-from-spreadsheet" >}}
{{< tab "JavaScript" >}}
```js
import '@groupdocs/groupdocs.total';
import java from 'java';

const DocumentAssembler = java.import('com.groupdocs.assembly.DocumentAssembler');
const DocumentTable = java.import('com.groupdocs.assembly.DocumentTable');
const DocumentTableOptions = java.import('com.groupdocs.assembly.DocumentTableOptions');
const DataSourceInfo = java.import('com.groupdocs.assembly.DataSourceInfo');

const options = new DocumentTableOptions();
options.setFirstRowContainsColumnNames(true);

// First worksheet: Client, Manager, Contract Price
const contracts = new DocumentTable('contracts-data.xlsx', 0, options);
const assembler = new DocumentAssembler();

assembler.assembleDocument(
  'contracts-template.docx',
  'assembly-spreadsheet.docx',
  new DataSourceInfo(contracts, 'contracts')
);
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`contracts-template.docx` is the template and `contracts-data.xlsx` is the table. Download [contracts-template.docx](/total/nodejs-java/_sample_files/contracts-template.docx) and [contracts-data.xlsx](/total/nodejs-java/_sample_files/contracts-data.xlsx).
{{< /tab-text >}}
{{< /tab >}}
{{< tab "assembly-spreadsheet.docx" >}}
```text
Total Contract Prices by Managers
Manager
Total Contract Price
John Smith
2300000.0
July James
800000.0
Tony Anderson
1200000.0
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/assembly/AssemblyAssembleSpreadsheet/assembly-spreadsheet.docx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Assembly also reads CSV and database data sources, generates tables, lists and charts from collections, supports conditional blocks and master-detail reports, and can insert hyperlinks and images from the data.

* [GroupDocs.Assembly for Node.js via Java documentation](https://docs.groupdocs.com/assembly/nodejs-java/) — the full product guide
* [Template syntax](https://docs.groupdocs.com/assembly/nodejs-java/template-syntax-part-1-of-2/)
* [Supported file formats](https://docs.groupdocs.com/assembly/nodejs-java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/assembly/java/)
