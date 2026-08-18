---
id: signature
url: total/nodejs-java/developer-guide/signature
title: Sign and verify documents with GroupDocs.Signature
linkTitle: Signature
weight: 9
description: "Add text, QR-code and barcode signatures to documents from GroupDocs.Total for Node.js via Java, then search and verify them — runnable JavaScript examples with downloadable input and output files."
keywords: GroupDocs.Signature, electronic signature, esign, sign document, QR code signature, verify signature, Node.js
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

GroupDocs.Signature applies electronic signatures to a document and finds them again afterwards. It supports text, image, digital certificate, barcode, QR-code, stamp, metadata and form-field signature types across Word, PDF, Excel, PowerPoint and image formats.

The three examples below cover the full lifecycle: sign, sign again, search.

## Sign a document with a text signature

A text signature draws text onto the page at a position you choose. `setLeft`/`setTop` place it, `setWidth`/`setHeight` bound it.

{{< tabs "signature-sign-with-text" >}}
{{< tab "JavaScript" >}}
```js
import { Signature } from '@groupdocs/groupdocs.total';
import java from 'java';

const TextSignOptions = java.import('com.groupdocs.signature.options.sign.TextSignOptions');

const signer = new Signature('contract.docx');

const signOptions = new TextSignOptions('John Smith');
signOptions.setLeft(100);
signOptions.setTop(100);
signOptions.setWidth(200);
signOptions.setHeight(40);

signer.sign('signature-sign-with-text.docx', signOptions);
signer.dispose();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "signature-sign-with-text.docx" >}}  
```text
Binary file (DOCX, 16 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/signature/SignatureSignWithText/signature-sign-with-text.docx)
{{< /tab >}}
{{< /tabs >}}

## Sign a document with a QR code

A QR-code signature encodes arbitrary text — an approval id, a verification URL — into a scannable code placed on the page. Set `setEncodeType` to the encoding you want; `QrCodeTypes.QR` is the standard one.

{{< tabs "signature-sign-with-qr-code" >}}
{{< tab "JavaScript" >}}
```js
import { Signature } from '@groupdocs/groupdocs.total';
import java from 'java';

const QrCodeSignOptions = java.import('com.groupdocs.signature.options.sign.QrCodeSignOptions');
const QrCodeTypes = java.import('com.groupdocs.signature.domain.qrcodes.QrCodeTypes');

const signer = new Signature('contract.docx');

const signOptions = new QrCodeSignOptions('Approved by John Smith');
signOptions.setEncodeType(QrCodeTypes.QR);
signOptions.setLeft(100);
signOptions.setTop(100);
signOptions.setWidth(120);
signOptions.setHeight(120);

signer.sign('signature-sign-with-qr-code.docx', signOptions);
signer.dispose();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "signature-sign-with-qr-code.docx" >}}  
```text
Binary file (DOCX, 20 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/signature/SignatureSignWithQrCode/signature-sign-with-qr-code.docx)
{{< /tab >}}
{{< /tabs >}}

## Search a document for signatures

Searching answers "what is on this document?". It returns every signature of the type you ask for, with its text and encoding.

{{< tabs "signature-search" >}}
{{< tab "JavaScript" >}}
```js
import { Signature } from '@groupdocs/groupdocs.total';
import java from 'java';

const QrCodeSignOptions = java.import('com.groupdocs.signature.options.sign.QrCodeSignOptions');
const QrCodeTypes = java.import('com.groupdocs.signature.domain.qrcodes.QrCodeTypes');
const QrCodeSearchOptions = java.import(
  'com.groupdocs.signature.options.search.QrCodeSearchOptions'
);
const QrCodeSignature = java.import(
  'com.groupdocs.signature.domain.signatures.QrCodeSignature'
);

// Sign first, so there is something to find
const signer = new Signature('contract.docx');
const signOptions = new QrCodeSignOptions('Approved by John Smith');
signOptions.setEncodeType(QrCodeTypes.QR);
signOptions.setLeft(100);
signOptions.setTop(100);
signer.sign('signature-search.docx', signOptions);
signer.dispose();

// Now search the signed document
const searcher = new Signature('signature-search.docx');
const searchOptions = new QrCodeSearchOptions();
const signatures = searcher.search(QrCodeSignature.class, searchOptions);

console.log('Signatures found: ' + signatures.size());

for (let i = 0; i < signatures.size(); i++) {
  const qrSignature = signatures.get(i);
  console.log('Text: ' + qrSignature.getText());
}

searcher.dispose();
```
{{< /tab >}}
{{< tab "contract.docx" >}}
{{< tab-text >}}
`contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "signature-search.docx" >}}  
```text
Binary file (DOCX, 20 KB)
```
[Download full output](/total/nodejs-java/_output_files/developer-guide/signature/SignatureSearch/signature-search.docx)
{{< /tab >}}
{{< /tabs >}}

## Learn more

GroupDocs.Signature also applies digital certificate signatures, image and stamp signatures, metadata and form-field signatures; verifies a document against expected signature values; and updates or deletes signatures already present.

* [GroupDocs.Signature for Node.js via Java documentation](https://docs.groupdocs.com/signature/nodejs-java/) — the full product guide
* [Supported file formats](https://docs.groupdocs.com/signature/nodejs-java/supported-document-formats/)
* [API reference](https://reference.groupdocs.com/signature/java/)
