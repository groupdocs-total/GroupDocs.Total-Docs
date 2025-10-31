---
id: quick-start-guide
url: total/python-net/quick-start-guide
title: Quick Start Guide  
linkTitle: Quick Start Guide    
weight: 5
keywords: "groupdocs total, python via .net, quick start, conversion example, metadata example"
description: "A guide on how to get started using the groupdocs-total-net package for Python via .NET."
productName: GroupDocs.Total for Python via .NET
hideChildren: False
toc: True
---

This guide provides a quick overview of how to set up and start using GroupDocs.Total for Python via .NET.  
It shows three code examples that demonstrate how to use packages included in the suite.

## Prerequisites

To proceed, make sure you have:

1. **Configured** environment as described in the [System Requirements]({{< ref "/total/python-net/getting-started/system-requirements.md" >}}) topic.
2. **Optionally** you may [Get a Temporary License](https://purchase.groupdocs.com/temporary-license/) to test all the product features. 

## Set Up Your Development Environment

For best practices, use a virtual environment to manage dependencies in Python applications. Learn more about virtual environment at [Create and Use Virtual Environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments) documentation topic.

### Create and Activate a Virtual Environment

Create a virtual environment:

{{< tabs "create_virtual_environment">}}
{{< tab "Windows" >}}
```ps
py -3.11 -m venv .venv
```
{{< /tab >}}
{{< /tabs >}}

Activate a virtual environment:

{{< tabs "activate_virtual_environment">}}
{{< tab "Windows" >}}
```ps
.venv\Scripts\activate
```
{{< /tab >}}
{{< /tabs >}}

### Install `groupdocs-total-net` Package

After activating the virtual environment, run the following command in your terminal to install the latest version of the package:

{{< tabs "install_package">}}
{{< tab "Windows" >}}
```ps
py -m pip install groupdocs-total-net
```
{{< /tab >}}
{{< /tabs >}}

Ensure the package is installed successfully. You should see the message 

```bash
Successfully installed groupdocs-total-net-*
```

## Example 1: Convert a document

This example shows how to convert a DOCX document to PDF using GroupDocs.Conversion.
You can download the demo app [here](/total/python-net/_sample_files/getting-started/quick-start-guide/convert_docx_to_pdf.zip).

{{< tabs "example_convert_docx_to_pdf">}}
{{< tab "convert_docx_to_pdf.py" >}}  
```python
import os
from groupdocs.conversion import License, Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def convert_docx_to_pdf():
    # Get license file absolute path
    license_path = os.path.abspath("./GroupDocs.Total.lic")

    if os.path.exists(license_path):
        # Create License and set the path
        license = License()
        license.set_license(license_path)

    # Load DOCX file
    with Converter("./business-plan.docx") as converter:
        # Create convert options
        pdf_convert_options = PdfConvertOptions()

        # Convert DOCX to PDF
        converter.convert("./business-plan.pdf", pdf_convert_options)

if __name__ == "__main__":
    convert_docx_to_pdf()
```
{{< /tab >}}
{{< tab "business-plan.docx" >}}  
{{< tab-text >}}
`business-plan.docx` is sample file used in this example. Click [here](/total/python-net/_sample_files/getting-started/quick-start-guide/business-plan.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "business-plan.pdf" >}}  
{{< tab-text >}}
`business-plan.pdf` is expected output PDF file. Click [here](/total/python-net/_sample_files/getting-started/quick-start-guide/business-plan.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< /tabs >}}

Your folder tree should look similar to the following directory structure:

```text
📂 demo-app
 ├──convert_docx_to_pdf.py
 ├──business-plan.docx
 └──GroupDocs.Total.lic (Optionally)
```

### Run the App

{{< tabs "run_convert_docx_to_pdf">}}
{{< tab "Windows" >}}
```ps
py convert_docx_to_pdf.py
```
{{< /tab >}}
{{< /tabs >}}

After running the app you can deactivate virtual environment by executing `deactivate` or closing your shell.

### Explanation
- `Converter("./business-plan.docx")`: Initializes the converter with the DOCX file.
- `PdfConvertOptions()`: Specifies the output format as PDF.
- `converter.convert("./business-plan.pdf", pdf_convert_options)`: Converts the DOCX file to PDF and saves it as `business-plan.pdf`.

## Example 2: Remove document metadata

This code example shows how to remove PDF document metadata and save the output to a file with GroupDocs.Metadata. You can download the app that we're going to buid [here](/total/python-net/_sample_files/getting-started/quick-start-guide/remove_pdf_metadata.zip).

{{< tabs "example_remove_pdf_document_metadata">}}
{{< tab "remove_pdf_document_metadata.py" >}}  
```python
import os
from groupdocs.metadata import License, Metadata

def remove_pdf_metadata():
    # Get license file absolute path
    license_path = os.path.abspath("./GroupDocs.Total.lic")

    if os.path.exists(license_path):
        # Create License and set the path
        license = License()
        license.set_license(license_path)

    # Load the PDF file
    with Metadata("./business-plan.pdf") as metadata:
      # Remove metadata
      metadata.sanitize()
     
      # Save the file with no metadata
      metadata.save("./no-metadata.pdf")

if __name__ == "__main__":
    remove_pdf_metadata()
```
{{< /tab >}}
{{< tab "business-plan.pdf" >}}  
{{< tab-text >}}
`business-plan.pdf` is sample file used in this example. Click [here](/total/python-net/_sample_files/getting-started/quick-start-guide/business-plan.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "no-metadata.pdf" >}}  
{{< tab-text >}}
`no-metadata.pdf` is expected output PDF file without metadata. Click [here](/total/python-net/_sample_files/getting-started/quick-start-guide/no-metadata.pdf) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< /tabs >}}

Your folder tree should look similar to the following directory structure:

```text
📂 demo-app
 ├──business-plan.pdf
 ├──remove_pdf_metadata.py
 └──GroupDocs.Total.lic (Optionally)
```

### Run the App

{{< tabs "run_remove_pdf_metadata">}}
{{< tab "Windows" >}}
```ps
py remove_pdf_metadata.py
```
{{< /tab >}}
{{< /tabs >}}

After running the app you can deactivate virtual environment by executing `deactivate` or closing your shell.

### Explanation
- `Metadata("./business-plan.pdf")`: Initializes metadata object with the source PDF file.
- `metadata.sanitize()`: Removes the metadata.
- `metadata.save("./no-metadata.pdf")`: Saves the output document without metadata.

## Example 3: Convert and remove metadata

This example converts a DOCX file to PDF and removes metadata in a single workflow.
You can download the demo app [here](/total/python-net/_sample_files/getting-started/quick-start-guide/convert_and_remove_metadata.zip).

{{< tabs "example_convert_and_remove_metadata">}}
{{< tab "convert_and_remove_metadata.py" >}}  
```python
import os
from groupdocs.conversion import License as ConversionLicense, Converter
from groupdocs.conversion.options.convert import PdfConvertOptions
from groupdocs.metadata import License as MetadataLicense, Metadata

def convert_and_remove_metadata():
    # Get license file absolute path
    license_path = os.path.abspath("./GroupDocs.Total.lic")

    if os.path.exists(license_path):
        # License GroupDocs.Conversion
        conversion_license = ConversionLicense()
        conversion_license.set_license(license_path)

        # License GroupDocs.Metadata
        metadata_license = MetadataLicense()
        metadata_license.set_license(license_path)

    # Load DOCX file
    with Converter("./business-plan.docx") as converter:
        # Create convert options
        pdf_convert_options = PdfConvertOptions()

        # Convert DOCX to PDF
        converter.convert("./business-plan.pdf", pdf_convert_options)

    # Load created PDF file
    with Metadata("./business-plan.pdf") as metadata:
      # Remove the metadata
      metadata.sanitize()
     
      # Save the file with no metadata
      metadata.save("./converted-no-metadata.pdf")

if __name__ == "__main__":
    convert_and_remove_metadata()
```
{{< /tab >}}
{{< tab "business-plan.docx" >}}  
{{< tab-text >}}
`business-plan.docx` is sample file used in this example. Click [here](/total/python-net/_sample_files/getting-started/quick-start-guide/business-plan.docx) to download it.
{{< /tab-text >}}
{{< /tab >}}
{{< tab "converted-no-metadata.pdf" >}}  
{{< tab-text >}}
`converted-no-metadata.pdf` is output PDF file without metadata. Click [here](/total/python-net/_sample_files/getting-started/quick-start-guide/converted-no-metadata.pdf) to download the output PDF file.
{{< /tab-text >}}
{{< /tab >}}
{{< /tabs >}}

Your folder tree should look similar to the following directory structure:

```text
📂 demo-app
 ├──business-plan.docx
 ├──convert_and_remove_metadata.py
 └──GroupDocs.Total.lic (Optionally)
```

### Run the App

{{< tabs "run_convert_and_remove_metadata">}}
{{< tab "Windows" >}}
```ps
py convert_and_remove_metadata.py
```
{{< /tab >}}
{{< /tabs >}}

After running the app you can deactivate virtual environment by executing `deactivate` or closing your shell.

### Explanation
- `Converter("./business-plan.docx")`: Initializes the converter with the DOCX file.
- `converter.convert("./business-plan.pdf", pdf_convert_options)`: Converts the DOCX file to PDF and saves it as `business-plan.pdf`.
- `Metadata("./business-plan.pdf")`: Reads converted PDF file.
- `metadata.sanitize()`: Removes the metadata.
- `metadata.save("./converted-no-metadata.pdf")`: Saves the output document without metadata.

## Learn More

- [Supported File Formats]({{< ref "/total/python-net/getting-started/supported-document-formats.md" >}}): Review the full list of supported file types.
- [Licensing and Evaluation]({{< ref "/total/python-net/getting-started/licensing-and-evaluation.md" >}}): Check details on licening and evaluation.
- [Technical Support]({{< ref "/total/python-net/technical-support.md" >}}): Contact support for assistance if you encounter issues.
