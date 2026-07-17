---
id: editor
url: total/net/developer-guide/editor
title: Edit documents with GroupDocs.Editor
linkTitle: Editor
weight: 12
description: "Round-trip a document through HTML so a web editor can change it, then save it back with GroupDocs.Total for .NET — runnable C# examples with downloadable files."
keywords: GroupDocs.Editor, edit document, WYSIWYG, document to HTML, HTML to DOCX, web editor, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Editor has no user interface of its own, and that is the thing to understand before reading the code. It converts a document **to HTML** so that a third-party WYSIWYG editor — TinyMCE, CKEditor, anything that edits HTML — can display and change it, then converts the edited HTML **back** into the original format.

So the shape is a three-stage round trip rather than a single call:

```text
   Editor.Edit()                  your web editor              Editor.Save()
document ──────────► EditableDocument ──► HTML ──► edited HTML ──────────► document
```

The examples below follow those three stages in order.

## Stage 1 and 2: open a document and get its HTML

`Edit` returns an `EditableDocument`. `GetBodyContent` gives you the markup to hand to the browser; `GetEmbeddedHtml` gives a self-contained page with images and styles inlined.

{{< tabs "editor-document-to-html" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.IO;
using GroupDocs.Editor;
using GroupDocs.Editor.Options;

using (Editor editor = new Editor("contract.docx"))
{
    // Stage 1: parse the document into an editable form
    using (EditableDocument document = editor.Edit(new WordProcessingEditOptions()))
    {
        // Stage 2: the HTML your web editor would load
        string bodyHtml = document.GetBodyContent();

        File.WriteAllText("editor-document-to-html.html", document.GetEmbeddedHtml());

        Console.WriteLine("Body HTML length: " + bodyHtml.Length + " characters");
    }
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "editor-document-to-html.html" >}}  
```text
<HTML><HEAD><META charset="utf-8" /><TITLE>Consulting Services Agreement - Aldergrove Manufacturing</TITLE><META name="author" content="Dana Whitfield" /><STYLE type="text/css">@page Section1 { 
	margin: 72pt; 
	size: 612pt 792pt; 
}
a { 
	text-decoration: none; 
}
.Default_Paragraph_Font, .BuiltIn-style, .Character-style { 
	-aw-style-name: defaultparagraphfont; 
	-gd-style-name: 'Default Paragraph Font'; 
[TRUNCATED]
```
[Download full output](/total/net/_output_files/developer-guide/editor/EditorDocumentToHtml/editor-document-to-html.html)
{{< /tab >}}
{{< /tabs >}}

## Stage 3: save edited HTML back to Word

`EditableDocument.FromMarkup` takes the HTML your editor returned. `Save` writes it back in whatever format the save options name.

{{< tabs "editor-html-to-document" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Editor;
using GroupDocs.Editor.Formats;
using GroupDocs.Editor.Options;

using (Editor editor = new Editor("contract.docx"))
{
    using (EditableDocument original = editor.Edit(new WordProcessingEditOptions()))
    {
        // Stand in for the user's edit in a web editor
        string editedHtml = original.GetBodyContent()
            .Replace("Consulting Services Agreement", "Consulting Services Agreement (revised)");

        using (EditableDocument edited = EditableDocument.FromMarkup(editedHtml, null))
        {
            editor.Save(edited, "editor-html-to-document.docx",
                new WordProcessingSaveOptions(WordProcessingFormats.Docx));
        }
    }
}

Console.WriteLine("Saved editor-html-to-document.docx");
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "editor-html-to-document.docx" >}}  
```text
Binary file (DOCX, 13 KB)
```
[Download full output](/total/net/_output_files/developer-guide/editor/EditorHtmlToDocument/editor-html-to-document.docx)
{{< /tab >}}
{{< /tabs >}}

## Convert format on the way out

Because saving is a separate stage with its own options, the document can come back in a different format from the one it went in as — edit a DOCX, save RTF.

{{< tabs "editor-save-as-rtf" >}}
{{< tab "C#" >}}
```csharp
using System;
using GroupDocs.Editor;
using GroupDocs.Editor.Formats;
using GroupDocs.Editor.Options;

using (Editor editor = new Editor("contract.docx"))
{
    using (EditableDocument document = editor.Edit(new WordProcessingEditOptions()))
    {
        editor.Save(document, "editor-save-as-rtf.rtf",
            new WordProcessingSaveOptions(WordProcessingFormats.Rtf));
    }
}

Console.WriteLine("Saved editor-save-as-rtf.rtf");
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "editor-save-as-rtf.rtf" >}}  
```text
Binary file (RTF, 694 KB)
```
[Download full output](/total/net/_output_files/developer-guide/editor/EditorSaveAsRtf/editor-save-as-rtf.rtf)
{{< /tab >}}
{{< /tabs >}}

{{< alert style="info" >}}
Save options are mandatory — they carry the target format. There is no "save as it came in" overload that infers it.
{{< /alert >}}

## Learn more

GroupDocs.Editor also edits spreadsheets, presentations, PDF, email, ebooks, Markdown, XML and CSV; manages the images and stylesheets a document references as separate HTML resources; reads document metainfo without a full parse; and handles Word form fields.

* [GroupDocs.Editor for .NET documentation](https://docs.groupdocs.com/editor/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/editor/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/editor/net/)
