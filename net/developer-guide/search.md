---
id: search
url: total/net/developer-guide/search
title: Search document collections with GroupDocs.Search
linkTitle: Search
weight: 11
description: "Build a full-text index over a folder of documents and query it with GroupDocs.Total for .NET — runnable C# examples with downloadable input and output files."
keywords: GroupDocs.Search, full text search, document search, search index, fuzzy search, boolean query, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Search is the one API in the suite that works on a **collection** rather than a single file. You build an index over a folder of documents once, then query it as often as you like — the index does the reading, so queries stay fast no matter how large the corpus grows.

That makes it a two-phase API: **index**, then **search**. The entry point is `Index`, not a "searcher".

{{< alert style="warning" >}}
`GroupDocs.Search.Index` clashes with **`System.Index`**, the type behind C# range syntax. In any file that has `using System;` — which is almost any file — a bare `Index` fails to compile:

```text
error CS0104: 'Index' is an ambiguous reference between 'GroupDocs.Search.Index' and 'System.Index'
```

The examples below open with `using Index = GroupDocs.Search.Index;`, which resolves it for the whole file. Fully qualifying every use works too, but reads badly.
{{< /alert >}}

## Build an index and search it

The index lives in a folder of its own, separate from the documents. `Add` reads a folder of documents into it; `Search` queries what has been indexed.

{{< tabs "search-build-index" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.IO;
using GroupDocs.Search;
using GroupDocs.Search.Results;
using Index = GroupDocs.Search.Index;

// The index is a folder the library owns; keep it out of your documents folder
string indexFolder = "search-build-index/index";
string documentsFolder = "archive";

Index index = new Index(indexFolder);

// Index every supported document in the folder
index.Add(documentsFolder);

SearchResult result = index.Search("throughput");

Console.WriteLine("Documents found: " + result.DocumentCount);
Console.WriteLine("Total occurrences: " + result.OccurrenceCount);

for (int i = 0; i < result.DocumentCount; i++)
{
    FoundDocument document = result.GetFoundDocument(i);
    // FilePath is absolute; the file name is the useful part here
    Console.WriteLine("  " + Path.GetFileName(document.DocumentInfo.FilePath)
                      + " (" + document.OccurrenceCount + " occurrences)");
}
```
{{< /tab >}}
{{< tab "documents/" >}}
{{< tab-text >}}
This example indexes the `archive` folder — three working documents from the engagement: [discovery-findings.docx](/total/net/_sample_files/archive/discovery-findings.docx), [steering-minutes.docx](/total/net/_sample_files/archive/steering-minutes.docx) and [phase-two-proposal.pdf](/total/net/_sample_files/archive/phase-two-proposal.pdf). Put them in a folder named `archive` next to your executable.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "search-build-index.txt" >}}  
```text
Documents found: 3
Total occurrences: 7
  discovery-findings.docx (4 occurrences)
  phase-two-proposal.pdf (2 occurrences)
  steering-minutes.docx (1 occurrences)
```
[Download full output](/total/net/_output_files/developer-guide/search/SearchBuildIndex/search-build-index.txt)
{{< /tab >}}
{{< /tabs >}}

## Search with a fuzzy query

Exact matching fails on scanned documents and typos. Fuzzy search accepts a similarity level — how many character edits away a word may be and still count as a hit.

{{< tabs "search-fuzzy" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Search;
using GroupDocs.Search.Options;
using GroupDocs.Search.Results;
using Index = GroupDocs.Search.Index;

string indexFolder = "search-fuzzy/index";
string documentsFolder = "archive";

Index index = new Index(indexFolder);
index.Add(documentsFolder);

SearchOptions options = new SearchOptions();
options.FuzzySearch.Enabled = true;
options.FuzzySearch.FuzzyAlgorithm = new TableDiscreteFunction(3);

// Matches "throughput" even when spelled "througput" or "throughtput"
SearchResult result = index.Search("throughput", options);

Console.WriteLine("Documents found: " + result.DocumentCount);
Console.WriteLine("Total occurrences: " + result.OccurrenceCount);
```
{{< /tab >}}
{{< tab "documents/" >}}
{{< tab-text >}}
This example indexes the `archive` folder — three working documents from the engagement: [discovery-findings.docx](/total/net/_sample_files/archive/discovery-findings.docx), [steering-minutes.docx](/total/net/_sample_files/archive/steering-minutes.docx) and [phase-two-proposal.pdf](/total/net/_sample_files/archive/phase-two-proposal.pdf). Put them in a folder named `archive` next to your executable.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "search-fuzzy.txt" >}}  
```text
Documents found: 3
Total occurrences: 7
```
[Download full output](/total/net/_output_files/developer-guide/search/SearchFuzzy/search-fuzzy.txt)
{{< /tab >}}
{{< /tabs >}}

## Search with a boolean query

Query text supports `AND`, `OR` and `NOT`, so you can express the same conditions a user would type into a search box. All three archived documents mention throughput; only the phase-two proposal mentions a forecast, so this query returns the other two.

{{< tabs "search-boolean" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.IO;
using GroupDocs.Search;
using GroupDocs.Search.Results;
using Index = GroupDocs.Search.Index;

string indexFolder = "search-boolean/index";
string documentsFolder = "archive";

Index index = new Index(indexFolder);
index.Add(documentsFolder);

SearchResult result = index.Search("throughput AND NOT forecast");

Console.WriteLine("Documents found: " + result.DocumentCount);

for (int i = 0; i < result.DocumentCount; i++)
{
    FoundDocument document = result.GetFoundDocument(i);
    Console.WriteLine("  " + Path.GetFileName(document.DocumentInfo.FilePath));
}
```
{{< /tab >}}
{{< tab "documents/" >}}
{{< tab-text >}}
This example indexes the `archive` folder — three working documents from the engagement: [discovery-findings.docx](/total/net/_sample_files/archive/discovery-findings.docx), [steering-minutes.docx](/total/net/_sample_files/archive/steering-minutes.docx) and [phase-two-proposal.pdf](/total/net/_sample_files/archive/phase-two-proposal.pdf). Put them in a folder named `archive` next to your executable.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "search-boolean.txt" >}}  
```text
Documents found: 2
  discovery-findings.docx
  steering-minutes.docx
```
[Download full output](/total/net/_output_files/developer-guide/search/SearchBoolean/search-boolean.txt)
{{< /tab >}}
{{< /tabs >}}

{{< alert style="info" >}}
An index is durable. Point `Index` at an existing index folder and it reopens what is already there rather than rebuilding — call `Add` again only when documents change, and `Update` to refresh ones that were modified.
{{< /alert >}}

## Learn more

GroupDocs.Search also offers phrase, wildcard, regex, faceted and date-range queries, highlights matches in the source document, indexes asynchronously with progress events, runs OCR over scanned pages, supports synonyms, homophones and stop words, and can distribute an index across a search network.

* [GroupDocs.Search for .NET documentation](https://docs.groupdocs.com/search/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/search/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/search/net/)
