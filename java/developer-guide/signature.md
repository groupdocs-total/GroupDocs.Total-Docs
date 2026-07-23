---
id: signature
url: total/java/developer-guide/signature
title: Sign and verify documents with GroupDocs.Signature
linkTitle: Signature
weight: 9
description: "Add text, QR-code and barcode signatures to documents from GroupDocs.Total for Java, then search and verify them — runnable Java examples with downloadable input and output files."
keywords: GroupDocs.Signature, electronic signature, esign, sign document, QR code signature, verify signature, Java
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

GroupDocs.Signature applies electronic signatures to a document and finds them again afterwards. It supports text, image, digital certificate, barcode, QR-code, stamp, metadata and form-field signature types across Word, PDF, Excel, PowerPoint and image formats.

The three examples below cover the full lifecycle: sign, sign again, search.

## Sign a document with a text signature

A text signature draws text onto the page at a position you choose. `setLeft`/`setTop` place it, `setWidth`/`setHeight` bound it.

{{< tabs "signature-sign-with-text" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.signature.Signature;
import com.groupdocs.signature.options.sign.TextSignOptions;

Signature signature = new Signature("contract.docx");

TextSignOptions signOptions = new TextSignOptions("John Smith");
signOptions.setLeft(100);
signOptions.setTop(100);
signOptions.setWidth(200);
signOptions.setHeight(40);

signature.sign("signature-sign-with-text.docx", signOptions);
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "signature-sign-with-text.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/java/_output_files/developer-guide/signature/SignatureSignWithText/signature-sign-with-text.docx)
{{< /tab >}}
{{< /tabs >}}

## Sign a document with a QR code

A QR-code signature encodes arbitrary text — an approval id, a verification URL — into a scannable code placed on the page. Set `setEncodeType` to the encoding you want; `QrCodeTypes.QR` is the standard one.

{{< tabs "signature-sign-with-qr-code" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.signature.Signature;
import com.groupdocs.signature.domain.qrcodes.QrCodeTypes;
import com.groupdocs.signature.options.sign.QrCodeSignOptions;

Signature signature = new Signature("contract.docx");

QrCodeSignOptions signOptions = new QrCodeSignOptions("Approved by John Smith");
signOptions.setEncodeType(QrCodeTypes.QR);
signOptions.setLeft(100);
signOptions.setTop(100);
signOptions.setWidth(120);
signOptions.setHeight(120);

signature.sign("signature-sign-with-qr-code.docx", signOptions);
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "signature-sign-with-qr-code.docx" >}}  
```text
Binary file (DOCX, 20 KB)
```
[Download full output](/total/java/_output_files/developer-guide/signature/SignatureSignWithQrCode/signature-sign-with-qr-code.docx)
{{< /tab >}}
{{< /tabs >}}

## Search a document for signatures

Searching answers "what is on this document?". It returns every signature of the type you ask for, with its text and encoding.

{{< tabs "signature-search" >}}
{{< tab "Java" >}}
```java
import com.groupdocs.signature.Signature;
import com.groupdocs.signature.domain.qrcodes.QrCodeTypes;
import com.groupdocs.signature.domain.signatures.QrCodeSignature;
import com.groupdocs.signature.options.search.QrCodeSearchOptions;
import com.groupdocs.signature.options.sign.QrCodeSignOptions;
import java.util.List;

// Sign first, so there is something to find
Signature signature = new Signature("contract.docx");
QrCodeSignOptions signOptions = new QrCodeSignOptions("Approved by John Smith");
signOptions.setEncodeType(QrCodeTypes.QR);
signOptions.setLeft(100);
signOptions.setTop(100);
signature.sign("signature-search.docx", signOptions);

// Now search the signed document
Signature searcher = new Signature("signature-search.docx");
QrCodeSearchOptions searchOptions = new QrCodeSearchOptions();
List<QrCodeSignature> signatures = searcher.search(QrCodeSignature.class, searchOptions);

System.out.println("Signatures found: " + signatures.size());

for (QrCodeSignature qrSignature : signatures) {
    System.out.println("Text: " + qrSignature.getText());
}
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "signature-search.docx" >}}  
```text
Binary file (DOCX, 20 KB)
```
[Download full output](/total/java/_output_files/developer-guide/signature/SignatureSearch/signature-search.docx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Signature also applies digital certificate signatures, image and stamp signatures, metadata and form-field signatures; verifies a document against expected signature values; and updates or deletes signatures already present.

* [GroupDocs.Signature for Java documentation](https://docs.groupdocs.com/signature/java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/signature/java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/signature/java/)
