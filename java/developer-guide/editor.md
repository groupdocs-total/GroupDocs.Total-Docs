---
id: editor
url: total/java/developer-guide/editor
title: Edit documents with GroupDocs.Editor
linkTitle: Editor
weight: 11
description: "Round-trip a document through HTML so a web editor can change it, then save it back with GroupDocs.Total for Java — runnable Java examples with downloadable files."
keywords: GroupDocs.Editor, edit document, WYSIWYG, document to HTML, HTML to DOCX, web editor, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Editor has no user interface of its own, and that is the thing to understand before reading the code. It converts a document **to HTML** so that a third-party WYSIWYG editor — TinyMCE, CKEditor, anything that edits HTML — can display and change it, then converts the edited HTML **back** into the original format.

So the shape is a three-stage round trip rather than a single call:

```text
   editor.edit()                  your web editor              editor.save()
document ──────────► EditableDocument ──► HTML ──► edited HTML ──────────► document
```

The examples below follow those three stages in order.

## Stage 1 and 2: open a document and get its HTML

`edit` returns an `EditableDocument`. `getBodyContent` gives you the markup to hand to the browser; `getEmbeddedHtml` gives a self-contained page with images and styles inlined.

{{< tabs "editor-document-to-html" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.editor.EditableDocument;
import com.groupdocs.editor.Editor;
import com.groupdocs.editor.options.WordProcessingEditOptions;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

Editor editor = new Editor("contract.docx");

// Stage 1: parse the document into an editable form
EditableDocument document = editor.edit(new WordProcessingEditOptions());

// Stage 2: the HTML your web editor would load
String bodyHtml = document.getBodyContent();

// getEmbeddedHtml() is a self-contained page with images and styles inlined
Files.write(Paths.get("editor-document-to-html.html"),
    document.getEmbeddedHtml().getBytes(StandardCharsets.UTF_8));

System.out.println("Body HTML length: " + bodyHtml.length() + " characters");
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "editor-document-to-html.html" >}}  
```text
<!DOCTYPE html>
<html><head><meta charset = "utf-8" /><title>Consulting Services Agreement - Aldergrove Manufacturing</title><meta name = "author" content = "Dana Whitfield" /><style type = "text/css">@page Section1 { margin: 72pt; size: 612pt; }
a { text-decoration: none; }
.Default_Paragraph_Font, .BuiltIn-style, .Character-style { -aw-style-name: defaultparagraphfont; -gd-style-name: 'Default Paragraph Font'; font-family: 'Times New Roman'; font-size: 10pt; font-weight: normal; font-style: no
[TRUNCATED]
```
[Download full output](/total/java/_output_files/developer-guide/editor/EditorDocumentToHtml/editor-document-to-html.html)
{{< /tab >}}
{{< /tabs >}}

## Stage 3: save edited HTML back to Word

`EditableDocument.fromMarkup` takes the HTML your editor returned. `save` writes it back in whatever format the save options name.

{{< tabs "editor-html-to-document" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.editor.EditableDocument;
import com.groupdocs.editor.Editor;
import com.groupdocs.editor.formats.WordProcessingFormats;
import com.groupdocs.editor.options.WordProcessingEditOptions;
import com.groupdocs.editor.options.WordProcessingSaveOptions;

Editor editor = new Editor("contract.docx");

EditableDocument original = editor.edit(new WordProcessingEditOptions());

// Stand in for the user's edit in a web editor
String editedHtml = original.getBodyContent()
    .replace("Consulting Services Agreement", "Consulting Services Agreement (revised)");

EditableDocument edited = EditableDocument.fromMarkup(editedHtml, null);

editor.save(edited, "editor-html-to-document.docx",
    new WordProcessingSaveOptions(WordProcessingFormats.Docx));

System.out.println("Saved editor-html-to-document.docx");
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "editor-html-to-document.docx" >}}  
```text
Binary file (DOCX, 12 KB)
```
[Download full output](/total/java/_output_files/developer-guide/editor/EditorHtmlToDocument/editor-html-to-document.docx)
{{< /tab >}}
{{< /tabs >}}

## Convert format on the way out

Because saving is a separate stage with its own options, the document can come back in a different format from the one it went in as — edit a DOCX, save RTF.

{{< tabs "editor-save-as-rtf" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.editor.EditableDocument;
import com.groupdocs.editor.Editor;
import com.groupdocs.editor.formats.WordProcessingFormats;
import com.groupdocs.editor.options.WordProcessingEditOptions;
import com.groupdocs.editor.options.WordProcessingSaveOptions;

Editor editor = new Editor("contract.docx");

EditableDocument document = editor.edit(new WordProcessingEditOptions());

editor.save(document, "editor-save-as-rtf.rtf",
    new WordProcessingSaveOptions(WordProcessingFormats.Rtf));

System.out.println("Saved editor-save-as-rtf.rtf");
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "editor-save-as-rtf.rtf" >}}  
```text
Binary file (RTF, 693 KB)
```
[Download full output](/total/java/_output_files/developer-guide/editor/EditorSaveAsRtf/editor-save-as-rtf.rtf)
{{< /tab >}}
{{< /tabs >}}

{{< alert style="info" >}}
Saving is a separate stage from editing, and the save options carry the target format. Passing `WordProcessingSaveOptions` with an explicit format is what lets the document come back as something other than it went in as.
{{< /alert >}}

## Learn more

GroupDocs.Editor also edits spreadsheets, presentations, PDF, email, ebooks, Markdown, XML and CSV; manages the images and stylesheets a document references as separate HTML resources; reads document metainfo without a full parse; and handles Word form fields.

* [GroupDocs.Editor for Java documentation](https://docs.groupdocs.com/editor/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/editor/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/editor/java/)
