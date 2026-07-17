---
id: signature
url: total/net/developer-guide/signature
title: Sign and verify documents with GroupDocs.Signature
linkTitle: Signature
weight: 10
description: "Add text, QR-code and barcode signatures to documents from GroupDocs.Total for .NET, then search and verify them — runnable C# examples with downloadable input and output files."
keywords: GroupDocs.Signature, electronic signature, esign, sign PDF, QR code signature, verify signature, .NET, C#
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

GroupDocs.Signature applies electronic signatures to a document and finds them again afterwards. It supports text, image, digital certificate, barcode, QR-code, stamp, metadata and form-field signature types across PDF, Word, Excel, PowerPoint and image formats.

The three examples below cover the full lifecycle: sign, verify, search.

## Sign a document with a text signature

A text signature draws text onto the page at a position you choose. `Left`/`Top` place it, `Width`/`Height` bound it.

{{< tabs "signature-sign-with-text" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Signature;
using GroupDocs.Signature.Options;

using (Signature signature = new Signature("contract.pdf"))
{
    TextSignOptions signOptions = new TextSignOptions("John Smith")
    {
        Left = 100,
        Top = 100,
        Width = 200,
        Height = 40
    };

    signature.Sign("signature-sign-with-text.pdf", signOptions);
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "signature-sign-with-text.pdf" >}}  
```text
Binary file (PDF, 216 KB)
```
[Download full output](/total/net/_output_files/developer-guide/signature/SignatureSignWithText/signature-sign-with-text.pdf)
{{< /tab >}}
{{< /tabs >}}

## Sign a document with a QR code

A QR-code signature encodes arbitrary text — an approval id, a verification URL — into a scannable code placed on the page.

{{< tabs "signature-sign-with-qr-code" >}}
{{< tab "C#" >}}
```csharp
using GroupDocs.Signature;
using GroupDocs.Signature.Domain;
using GroupDocs.Signature.Options;

using (Signature signature = new Signature("contract.pdf"))
{
    QrCodeSignOptions signOptions = new QrCodeSignOptions("Approved by John Smith")
    {
        EncodeType = QrCodeTypes.QR,
        Left = 100,
        Top = 100,
        Width = 120,
        Height = 120
    };

    signature.Sign("signature-sign-with-qr-code.pdf", signOptions);
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "signature-sign-with-qr-code.pdf" >}}  
```text
Binary file (PDF, 159 KB)
```
[Download full output](/total/net/_output_files/developer-guide/signature/SignatureSignWithQrCode/signature-sign-with-qr-code.pdf)
{{< /tab >}}
{{< /tabs >}}

## Search a document for signatures

Searching answers "what is on this document?". It returns every signature of the type you ask for, with its page and position.

{{< tabs "signature-search" >}}
{{< tab "C#" >}}
```csharp
using System;
using System.Collections.Generic;
using GroupDocs.Signature;
using GroupDocs.Signature.Domain;
using GroupDocs.Signature.Options;

// Sign first, so there is something to find
using (Signature signature = new Signature("contract.pdf"))
{
    QrCodeSignOptions signOptions = new QrCodeSignOptions("Approved by John Smith")
    {
        Left = 100,
        Top = 100
    };
    signature.Sign("signature-search.pdf", signOptions);
}

using (Signature signature = new Signature("signature-search.pdf"))
{
    QrCodeSearchOptions searchOptions = new QrCodeSearchOptions();
    List<QrCodeSignature> signatures = signature.Search<QrCodeSignature>(searchOptions);

    Console.WriteLine("Signatures found: " + signatures.Count);

    foreach (QrCodeSignature qrSignature in signatures)
    {
        Console.WriteLine("Type: " + qrSignature.EncodeType.TypeName
                          + ", text: " + qrSignature.Text
                          + ", page: " + qrSignature.PageNumber);
    }
}
```
{{< /tab >}}
{{< tab "contract.pdf" >}}
{{< tab-text >}}
`contract.pdf` is the sample file used in this example. Click [here](/total/net/_sample_files/contract.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "signature-search.pdf" >}}  
```text
Binary file (PDF, 159 KB)
```
[Download full output](/total/net/_output_files/developer-guide/signature/SignatureSearch/signature-search.pdf)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Signature also applies digital certificate signatures, image and stamp signatures, metadata and form-field signatures; verifies a document against expected signature values; and updates or deletes signatures already present.

* [GroupDocs.Signature for .NET documentation](https://docs.groupdocs.com/signature/net/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/signature/net/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/signature/net/)
