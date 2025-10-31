---
id: installation
url: total/python-net/installation
title: Installation
linkTitle: Installation
weight: 3
description: "This guide explains how to install GroupDocs.Total for Python via .NET in your environment."
productName: GroupDocs.Conversion for Python via .NET
hideChildren: False
toc: True
---

## Install Package from PyPI

PyPI (Python Package Index) is a repository of software packages for the Python programming language. Visit the [groupdocs-total-net](https://pypi.org/project/groupdocs-total-net/) package page for more details. 

### Installing the Package

To install the package, open a terminal and run the following command:

{{< tabs "example1">}}
{{< tab "Windows" >}}
```bash
py -m pip install groupdocs-total-net
```
{{< /tab >}}
{{< tab "macOS" >}}
```bash
python3 -m pip install groupdocs-total-net
```
{{< /tab >}}
{{< /tabs >}}

When running the command on Windows, you can expect an output similar to the following:

```bash
Collecting groupdocs-total-net
  Using cached groupdocs_total_net-25.10.0-py3-none-any.whl.metadata (5.2 kB)
Collecting groupdocs-conversion-net==24.12 (from groupdocs-total-net)
...
Successfully installed groupdocs-assembly-net-25.5.1 groupdocs-comparison-net-25.6 groupdocs-conversion-net-24.12 groupdocs-merger-net-25.3 groupdocs-metadata-net-25.4 groupdocs-redaction-net-25.10 groupdocs-signature-net-25.4 groupdocs-total-net-25.10.0 groupdocs-viewer-net-24.9 groupdocs-watermark-net-25.3
```

### Adding the Package to requirements.txt

You can add the dependency to your `requirements.txt` file by including the following line:

```bash
groupdocs-total-net==25.10
```

Then, install the package using this command:

```bash
pip install -r requirements.txt
```

## Download Package from Official Website

To download the GroupDocs.Total metapackage, please visit the official [GroupDocs Releases website](https://releases.groupdocs.com/total/python-net/).  
You can also download individual packages from their respective product pages:

* [groupdocs-conversion-net](https://releases.groupdocs.com/conversion/python-net/#direct-download)
* [groupdocs-viewer-net](https://releases.groupdocs.com/viewer/python-net/#direct-download)
* [groupdocs-comparison-net](https://releases.groupdocs.com/comparison/python-net/#direct-download)
* [groupdocs-watermark-net](https://releases.groupdocs.com/watermark/python-net/#direct-download)
* [groupdocs-metadata-net](https://releases.groupdocs.com/metadata/python-net/#direct-download)
* [groupdocs-merger-net](https://releases.groupdocs.com/merger/python-net/#direct-download)
* [groupdocs-assembly-net](https://releases.groupdocs.com/assembly/python-net/#direct-download)
* [groupdocs-redaction-net](https://releases.groupdocs.com/redaction/python-net/#direct-download)
* [groupdocs-signature-net](https://releases.groupdocs.com/signature/python-net/#direct-download)

Make sure to select the package that matches your system’s architecture.

### Copy the Downloaded File

After downloading, copy the package file into your project folder.

#### Install the groupdocs-total-net Metapackage

The following example shows how to install **GroupDocs.Total for Python via .NET** after downloading the `.whl` file:

{{< tabs "example2">}}
{{< tab "Windows" >}}
```powershell
py -m pip install groupdocs_total_net-25.10.0-py3-none-any.whl
```
{{< /tab >}}
{{< /tabs >}}

Expected output:

```bash
Processing groupdocs_total_net-25.10.0-py3-none-any.whl
...
Successfully installed groupdocs-assembly-net-25.5.1 groupdocs-comparison-net-25.6 groupdocs-conversion-net-24.12 groupdocs-merger-net-25.3 groupdocs-metadata-net-25.4 groupdocs-redaction-net-25.10 groupdocs-signature-net-25.4 groupdocs-total-net-25.10.0 groupdocs-viewer-net-24.9 groupdocs-watermark-net-25.3
```

#### Install an Individual Package File

The following examples show how to install **GroupDocs.Conversion for Python via .NET** depending on your operating system:

{{< tabs "example3">}}
{{< tab "Windows (64-bit)" >}}
```powershell
py -m pip install groupdocs_conversion_net-24.12-py3-none-win_amd64.whl
```
{{< /tab >}}
{{< tab "Windows (32-bit)" >}}
```powershell
py -m pip install groupdocs_conversion_net-24.12-py3-none-win32.whl
```
{{< /tab >}}
{{< tab "macOS (Apple Silicon)" >}}
```bash
python3 -m pip install groupdocs_conversion_net-24.12-py3-none-macosx_11_0_arm64.whl
```
{{< /tab >}}
{{< tab "macOS (Intel)" >}}
```bash
python3 -m pip install groupdocs_conversion_net-24.12-py3-none-macosx_10_14_x86_64.whl
```
{{< /tab >}}
{{< /tabs >}}

Expected output:

```bash
Processing groupdocs_conversion_net-24.12-py3-none-win_amd64.whl
...
Successfully installed groupdocs-conversion-net-24.12
```

## Troubleshooting

If you encounter issues during installation, try the following steps:

* Ensure that the proper Python version is installed — see the [System Requirements]({{< ref "/total/python-net/getting-started/system-requirements.md" >}}) page for details.
* Contact us using any of the channels listed in the [Technical Support]({{< ref "/total/python-net/technical-support" >}}) section.
