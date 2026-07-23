---
id: search
url: total/java/developer-guide/search
title: Search document collections with GroupDocs.Search
linkTitle: Search
weight: 10
description: "Build a full-text index over a folder of documents and query it with GroupDocs.Total for Java — runnable Java examples with downloadable input and output files."
keywords: GroupDocs.Search, full text search, document search, search index, fuzzy search, boolean query, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Search is the one API in the suite that works on a **collection** rather than a single file. You build an index over a folder of documents once, then query it as often as you like — the index does the reading, so queries stay fast no matter how large the corpus grows.

That makes it a two-phase API: **index**, then **search**. The entry point is `Index`, not a "searcher".

{{< alert style="info" >}}
The code on this page is complete and ready to run against GroupDocs.Total for Java. Downloadable output samples for these examples are being added — in the meantime, the [GroupDocs.Search for Java documentation](https://docs.groupdocs.com/search/java/) carries the full set of runnable examples.
{{< /alert >}}

## Build an index and search it

The index lives in a folder of its own, separate from the documents. `add` reads a folder of documents into it; `search` queries what has been indexed.

{{< tabs "search-build-index" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.search.Index;
import com.groupdocs.search.results.FoundDocument;
import com.groupdocs.search.results.SearchResult;
import java.io.File;

// The index is a folder the library owns; keep it out of your documents folder
try (Index index = new Index("search-build-index/index")) {
    // Index every supported document in the folder
    index.add("archive");

    SearchResult result = index.search("throughput");

    System.out.println("Documents found: " + result.getDocumentCount());
    System.out.println("Total occurrences: " + result.getOccurrenceCount());

    for (int i = 0; i < result.getDocumentCount(); i++) {
        FoundDocument document = result.getFoundDocument(i);
        // getFilePath() is absolute; the file name is the useful part here
        String fileName = new File(document.getDocumentInfo().getFilePath()).getName();
        System.out.println("  " + fileName + " (" + document.getOccurrenceCount() + " occurrences)");
    }
}
```
{{< /tab >}}
{{< tab "documents/" >}}
{{< tab-text >}}
This example indexes the `archive` folder — three working documents from the engagement: [discovery-findings.docx](/total/java/_sample_files/archive/discovery-findings.docx), [steering-minutes.docx](/total/java/_sample_files/archive/steering-minutes.docx) and [phase-two-proposal.pdf](/total/java/_sample_files/archive/phase-two-proposal.pdf). Put them in a folder named `archive` next to your program.
{{< /tab-text >}}
{{< /tab >}}
{{< /tabs >}}

## Search with a fuzzy query

Exact matching fails on scanned documents and typos. Fuzzy search accepts a similarity level — how many character edits away a word may be and still count as a hit.

{{< tabs "search-fuzzy" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.search.Index;
import com.groupdocs.search.options.SearchOptions;
import com.groupdocs.search.options.TableDiscreteFunction;
import com.groupdocs.search.results.SearchResult;

try (Index index = new Index("search-fuzzy/index")) {
    index.add("archive");

    SearchOptions options = new SearchOptions();
    options.getFuzzySearch().setEnabled(true);
    options.getFuzzySearch().setFuzzyAlgorithm(new TableDiscreteFunction(3));

    // Matches "throughput" even when spelled "througput" or "throughtput"
    SearchResult result = index.search("throughput", options);

    System.out.println("Documents found: " + result.getDocumentCount());
    System.out.println("Total occurrences: " + result.getOccurrenceCount());
}
```
{{< /tab >}}
{{< tab "documents/" >}}
{{< tab-text >}}
This example indexes the `archive` folder — three working documents from the engagement: [discovery-findings.docx](/total/java/_sample_files/archive/discovery-findings.docx), [steering-minutes.docx](/total/java/_sample_files/archive/steering-minutes.docx) and [phase-two-proposal.pdf](/total/java/_sample_files/archive/phase-two-proposal.pdf). Put them in a folder named `archive` next to your program.
{{< /tab-text >}}
{{< /tab >}}
{{< /tabs >}}

## Search with a boolean query

Query text supports `AND`, `OR` and `NOT`, so you can express the same conditions a user would type into a search box. All three archived documents mention throughput; only the phase-two proposal mentions a forecast, so this query returns the other two.

{{< tabs "search-boolean" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.search.Index;
import com.groupdocs.search.results.FoundDocument;
import com.groupdocs.search.results.SearchResult;
import java.io.File;

try (Index index = new Index("search-boolean/index")) {
    index.add("archive");

    SearchResult result = index.search("throughput AND NOT forecast");

    System.out.println("Documents found: " + result.getDocumentCount());

    for (int i = 0; i < result.getDocumentCount(); i++) {
        FoundDocument document = result.getFoundDocument(i);
        System.out.println("  " + new File(document.getDocumentInfo().getFilePath()).getName());
    }
}
```
{{< /tab >}}
{{< tab "documents/" >}}
{{< tab-text >}}
This example indexes the `archive` folder — three working documents from the engagement: [discovery-findings.docx](/total/java/_sample_files/archive/discovery-findings.docx), [steering-minutes.docx](/total/java/_sample_files/archive/steering-minutes.docx) and [phase-two-proposal.pdf](/total/java/_sample_files/archive/phase-two-proposal.pdf). Put them in a folder named `archive` next to your program.
{{< /tab-text >}}
{{< /tab >}}
{{< /tabs >}}

{{< alert style="info" >}}
An index is durable. Point `Index` at an existing index folder and it reopens what is already there rather than rebuilding — call `add` again only when documents change, and `update` to refresh ones that were modified.
{{< /alert >}}

## Learn more

GroupDocs.Search also offers phrase, wildcard, regex, faceted and date-range queries, highlights matches in the source document, indexes asynchronously with progress events, runs OCR over scanned pages, supports synonyms, homophones and stop words, and can distribute an index across a search network.

* [GroupDocs.Search for Java documentation](https://docs.groupdocs.com/search/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/search/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/search/java/)
