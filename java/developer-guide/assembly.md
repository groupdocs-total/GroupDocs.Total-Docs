---
id: assembly
url: total/java/developer-guide/assembly
title: Generate documents from templates with GroupDocs.Assembly
linkTitle: Assembly
weight: 8
description: "Fill a template from Java objects, JSON or a spreadsheet and generate a finished document with GroupDocs.Total for Java — runnable examples with downloadable templates and output."
keywords: GroupDocs.Assembly, document automation, report generation, Word template, mail merge, LINQ reporting, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Assembly generates documents from a template and a data source. Unlike the rest of the suite it needs an input you have to author yourself: a **template** carrying `<<[...]>>` tags that say where the data goes.

`<<[expr]>>` inserts a value, `<<foreach [x in xs]>>…<</foreach>>` repeats a block, and expressions can compute. On a Java object the expression calls a public getter, for example `manager.getName()`. JSON, XML and spreadsheet fields are referred to by name, for example `Name` or `Client.Name`. The output format follows the output file's extension.

## Generate a document from a Java object

Pass any object as a data source and name it. The name is what the template's tags refer to — here `manager`. The template `single-row.txt` contains:

```text
Name:	<<[manager.getName()]>>
Age:	<<[manager.getAge()]>>
```

{{< tabs "assembly-from-object" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.assembly.DataSourceInfo;
import com.groupdocs.assembly.DocumentAssembler;

public class Manager {
    private final String name;
    private final int age;

    public Manager(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

Manager manager = new Manager("John Smith", 37);

DocumentAssembler assembler = new DocumentAssembler();

// "manager" must match the name the template's tags use
assembler.assembleDocument(
        "single-row.txt",
        "assembly-object.txt",
        new DataSourceInfo(manager, "manager"));
```
{{< /tab >}}
{{< tab "single-row.txt" >}}
{{< tab-text >}}
`single-row.txt` is the template used in this example. Click [here](/total/java/_sample_files/single-row.txt) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "assembly-object.txt" >}}
```text
Name:	John Smith
Age:	37
```
[Download full output](/total/java/_output_files/developer-guide/assembly/AssemblyAssembleObject/assembly-object.txt)
{{< /tab >}}
{{< /tabs >}}

{{< alert style="warning" >}}
Data source classes must be **public**, and the template can only call **public** methods or read **public** fields. The engine reflects over the object at generation time, so a non-public class fails at run time rather than compile time. The same applies to the item type inside a collection.
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
{{< tab "Java" >}}
```java
import com.groupdocs.assembly.DataSourceInfo;
import com.groupdocs.assembly.DocumentAssembler;
import com.groupdocs.assembly.JsonDataSource;

JsonDataSource managers = new JsonDataSource("manager-data.json");

DocumentAssembler assembler = new DocumentAssembler();
assembler.assembleDocument(
        "simple-dataset.docx",
        "assembly-json.docx",
        new DataSourceInfo(managers, "managers"));
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`simple-dataset.docx` is the template and `manager-data.json` is the data. Download [simple-dataset.docx](/total/java/_sample_files/simple-dataset.docx) and [manager-data.json](/total/java/_sample_files/manager-data.json).
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
[Download full output](/total/java/_output_files/developer-guide/assembly/AssemblyAssembleJson/assembly-json.docx)
{{< /tab >}}
{{< /tabs >}}

The `String` argument of `JsonDataSource` is a file path. To assemble JSON held in memory, pass an `InputStream` instead.

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
{{< tab "Java" >}}
```java
import com.groupdocs.assembly.DataSourceInfo;
import com.groupdocs.assembly.DocumentAssembler;
import com.groupdocs.assembly.DocumentTable;
import com.groupdocs.assembly.DocumentTableOptions;

DocumentTableOptions options = new DocumentTableOptions();
options.setFirstRowContainsColumnNames(true);

// First worksheet: Client, Manager, Contract Price
DocumentTable contracts = new DocumentTable("contracts-data.xlsx", 0, options);

DocumentAssembler assembler = new DocumentAssembler();
assembler.assembleDocument(
        "contracts-template.docx",
        "assembly-spreadsheet.docx",
        new DataSourceInfo(contracts, "contracts"));
```
{{< /tab >}}
{{< tab "Sample files" >}}
{{< tab-text >}}
`contracts-template.docx` is the template and `contracts-data.xlsx` is the table. Download [contracts-template.docx](/total/java/_sample_files/contracts-template.docx) and [contracts-data.xlsx](/total/java/_sample_files/contracts-data.xlsx).
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
[Download full output](/total/java/_output_files/developer-guide/assembly/AssemblyAssembleSpreadsheet/assembly-spreadsheet.docx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Assembly also reads XML, CSV and database data sources, generates tables, lists and charts from collections, supports conditional blocks and master-detail reports, and can insert hyperlinks and images from the data.

* [GroupDocs.Assembly for Java documentation](https://docs.groupdocs.com/assembly/java/) — the full product guide
* [Template syntax](https://docs.groupdocs.com/assembly/java/basic-usage-template-syntax-basics/)
* [Supported file formats](https://docs.groupdocs.com/assembly/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/assembly/java/)
