---
id: assembly
url: total/net/developer-guide/assembly
title: Generate documents from templates with GroupDocs.Assembly
linkTitle: Assembly
weight: 8
description: "Fill a Word template from .NET objects or JSON and generate a finished document with GroupDocs.Total for .NET — runnable C# examples with downloadable template and output."
keywords: GroupDocs.Assembly, document automation, report generation, Word template, mail merge, LINQ reporting, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Assembly generates documents from a template and a data source. Unlike the rest of the suite it needs an input you have to author yourself: a **template** carrying `<<[...]>>` tags that say where the data goes.

Every example below uses `invoice-template.docx`, which contains:

```text
Invoice <<[invoice.Number]>>

Bill to: <<[invoice.CustomerName]>>
Date: <<[invoice.Date]:"dd MMMM yyyy">>

Items
<<foreach [item in invoice.Items]>><<[item.Description]>> - qty <<[item.Quantity]>> - <<[item.Price]>> USD<</foreach>>

Total: <<[invoice.Items.Sum(i => i.Quantity * i.Price)]>> USD
```

The tag syntax is the LINQ Reporting Engine: `<<[expr]>>` inserts a value, `<<foreach [x in xs]>>…<</foreach>>` repeats a block, and expressions can compute — note the `Sum` in the total.

## Generate a document from .NET objects

Pass any object as a data source and name it. The name is what the template's tags refer to — here `invoice`.

{{< tabs "assembly-from-objects" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.Collections.Generic;
using GroupDocs.Assembly;

public class InvoiceItem
{
    public string Description { get; set; } = "";
    public int Quantity { get; set; }
    public decimal Price { get; set; }
}

public class Invoice
{
    public string Number { get; set; } = "";
    public string CustomerName { get; set; } = "";
    public DateTime Date { get; set; }
    public List<InvoiceItem> Items { get; set; } = new();
}

var invoice = new Invoice
{
    Number = "INV-2026-0042",
    CustomerName = "Northwind Trading Ltd",
    Date = new DateTime(2026, 7, 16),
    Items = new List<InvoiceItem>
    {
        new InvoiceItem { Description = "Document processing licence", Quantity = 3, Price = 1200m },
        new InvoiceItem { Description = "Priority support",            Quantity = 1, Price = 800m },
        new InvoiceItem { Description = "Onboarding workshop",         Quantity = 2, Price = 450m }
    }
};

DocumentAssembler assembler = new DocumentAssembler();

// "invoice" must match the name the template's tags use
assembler.AssembleDocument(
    "invoice-template.docx",
    "assembly-from-objects.docx",
    new DataSourceInfo(invoice, "invoice"));

Console.WriteLine("Generated assembly-from-objects.docx");
```
{{< /tab >}}
{{< tab "invoice-template.docx" >}}
{{< tab-text >}}
`invoice-template.docx` is the template used in this example. Click [here](/total/net/_sample_files/invoice-template.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "assembly-from-objects.docx" >}}  
```text
Binary file (DOCX, 12 KB)
```
[Download full output](/total/net/_output_files/developer-guide/assembly/AssemblyFromObjects/assembly-from-objects.docx)
{{< /tab >}}
{{< /tabs >}}

## Generate a PDF from the same template

The output format follows the output file's extension. The same template and the same data produce a PDF instead of a Word file with no other change.

{{< tabs "assembly-to-pdf" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.Collections.Generic;
using GroupDocs.Assembly;

// Data classes must be public — see the note below
public class LineItem
{
    public string Description { get; set; } = "";
    public int Quantity { get; set; }
    public decimal Price { get; set; }
}

public class Order
{
    public string Number { get; set; } = "";
    public string CustomerName { get; set; } = "";
    public DateTime Date { get; set; }
    public List<LineItem> Items { get; set; } = new();
}

var invoice = new Order
{
    Number = "INV-2026-0043",
    CustomerName = "Contoso Manufacturing",
    Date = new DateTime(2026, 7, 16),
    Items = new List<LineItem>
    {
        new LineItem { Description = "Annual subscription", Quantity = 1, Price = 9600m },
        new LineItem { Description = "Additional seats",    Quantity = 5, Price = 240m }
    }
};

DocumentAssembler assembler = new DocumentAssembler();

assembler.AssembleDocument(
    "invoice-template.docx",
    "assembly-to-pdf.pdf",
    new DataSourceInfo(invoice, "invoice"));

Console.WriteLine("Generated assembly-to-pdf.pdf");
```
{{< /tab >}}
{{< tab "invoice-template.docx" >}}
{{< tab-text >}}
`invoice-template.docx` is the template used in this example. Click [here](/total/net/_sample_files/invoice-template.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "assembly-to-pdf.pdf" >}}  
```text
Binary file (PDF, 91 KB)
```
[Download full output](/total/net/_output_files/developer-guide/assembly/AssemblyToPdf/assembly-to-pdf.pdf)
{{< /tab >}}
{{< /tabs >}}

{{< alert style="warning" >}}
Data source classes must be **public**. The engine reflects over the object at generation time, so an anonymous type or an `internal` class fails at run time rather than compile time:

```text
System.InvalidOperationException: A data source object must be of a visible type
or implement 'System.Collections.IEnumerable'. (Parameter 'dataSource')
```

The same applies to the item type inside a collection — `List<LineItem>` needs `LineItem` public too.
{{< /alert >}}

## Learn more

GroupDocs.Assembly also reads JSON, XML, CSV, DataTable and database data sources, generates tables and charts from collections, supports conditional blocks, master-detail reports, hyperlinks and images in templates, and can produce output in any format the suite supports.

* [GroupDocs.Assembly for .NET documentation](https://docs.groupdocs.com/assembly/net/) — the full product guide
* [Template syntax](https://docs.groupdocs.com/assembly/net/template-syntax/)
* [API reference](https://reference.groupdocs.com/assembly/net/)
