---
id: installation
url: total/python-net/installation
title: Installation
linkTitle: Installation
weight: 3
description: "This guide explains how to install GroupDocs.Total for Python via .NET in your environment."
productName: GroupDocs.Total for Python via .NET
hideChildren: False
toc: True
---

## Install Package from PyPI

PyPI (Python Package Index) is a repository of software packages for the Python programming language. Visit the [groupdocs-total-net](https://pypi.org/project/groupdocs-total-net/) package page for more details. 

### Installing the Package

`groupdocs-total-net` is a metapackage: it installs the 14 GroupDocs for Python via .NET products, about 2.2 GB to download and 3.2 GB on disk. To install it, open a terminal and run the following command:

{{< tabs "example1">}}
{{< tab "Windows" >}}
```bash
py -m pip install groupdocs-total-net
```
{{< /tab >}}
{{< tab "Linux and macOS" >}}
```bash
python3 -m pip install groupdocs-total-net
```
{{< /tab >}}
{{< /tabs >}}

When running the command on Windows, you can expect an output similar to the following:

```bash
Collecting groupdocs-total-net
  Downloading groupdocs_total_net-26.11.0-py3-none-any.whl.metadata (9.7 kB)
Collecting groupdocs-conversion-net==26.9.0 (from groupdocs-total-net)
...
Successfully installed groupdocs-annotation-net-26.6.0 groupdocs-assembly-net-26.11.0 groupdocs-comparison-net-26.5.0 groupdocs-conversion-net-26.9.0 groupdocs-editor-net-26.5.0 groupdocs-markdown-net-26.3.0 groupdocs-merger-net-26.6.0 groupdocs-metadata-net-26.9.0 groupdocs-parser-net-26.10.0 groupdocs-redaction-net-26.6.0 groupdocs-search-net-26.10.0 groupdocs-signature-net-26.10.0 groupdocs-total-net-26.11.0 groupdocs-viewer-net-26.9.0 groupdocs-watermark-net-26.10.0
```

### Adding the Package to requirements.txt

You can add the dependency to your `requirements.txt` file by including the following line:

```bash
groupdocs-total-net==26.11.0
```

Then, install the package using this command:

```bash
pip install -r requirements.txt
```

### Installing Only the Products You Use

Each product is also a package of its own, so you can install just the ones your application uses, for example:

```bash
pip install groupdocs-conversion-net groupdocs-watermark-net
```

## Install Without Internet Access

On a machine with internet access and the same operating system and Python version, download the metapackage and all 14 product wheels into a folder:

```bash
pip download groupdocs-total-net==26.11.0 -d wheels
```

Copy the `wheels` folder to the target machine and install from it:

```bash
pip install --no-index --find-links wheels groupdocs-total-net==26.11.0
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
* [groupdocs-parser-net](https://releases.groupdocs.com/parser/python-net/#direct-download)
* [groupdocs-search-net](https://releases.groupdocs.com/search/python-net/#direct-download)
* [groupdocs-annotation-net](https://releases.groupdocs.com/annotation/python-net/#direct-download)
* [groupdocs-editor-net](https://releases.groupdocs.com/editor/python-net/#direct-download)
* [groupdocs-markdown-net](https://releases.groupdocs.com/markdown/python-net/#direct-download)

Make sure to select the package that matches your system’s architecture.

### Copy the Downloaded File

After downloading, copy the package file into your project folder.

#### Install the groupdocs-total-net Metapackage

The metapackage file only lists the 14 products; pip downloads them from PyPI when you install it. To install from downloaded files only, put the metapackage file and the 14 product wheels for your platform in one folder, and run this command in it:

{{< tabs "example2">}}
{{< tab "Windows" >}}
```powershell
py -m pip install --no-index --find-links . groupdocs-total-net==26.11.0
```
{{< /tab >}}
{{< tab "Linux and macOS" >}}
```bash
python3 -m pip install --no-index --find-links . groupdocs-total-net==26.11.0
```
{{< /tab >}}
{{< /tabs >}}

#### Install an Individual Package File

The following examples show how to install **GroupDocs.Conversion for Python via .NET** depending on your operating system:

{{< tabs "example3">}}
{{< tab "Windows (64-bit)" >}}
```powershell
py -m pip install groupdocs_conversion_net-26.9.0-py3-none-win_amd64.whl
```
{{< /tab >}}
{{< tab "Linux" >}}
```bash
python3 -m pip install groupdocs_conversion_net-26.9.0-py3-none-manylinux1_x86_64.whl
```
{{< /tab >}}
{{< tab "macOS (Apple Silicon)" >}}
```bash
python3 -m pip install groupdocs_conversion_net-26.9.0-py3-none-macosx_11_0_arm64.whl
```
{{< /tab >}}
{{< tab "macOS (Intel)" >}}
```bash
python3 -m pip install groupdocs_conversion_net-26.9.0-py3-none-macosx_10_14_x86_64.whl
```
{{< /tab >}}
{{< /tabs >}}

Expected output:

```bash
Processing groupdocs_conversion_net-26.9.0-py3-none-win_amd64.whl
...
Successfully installed groupdocs-conversion-net-26.9.0
```

## Troubleshooting

If you encounter issues during installation, try the following steps:

* Ensure that the proper Python version is installed — see the [System Requirements]({{< ref "/total/python-net/getting-started/system-requirements.md" >}}) page for details.
* Use pip 20.3 or later: `python -m pip install --upgrade pip`.
* Contact us using any of the channels listed in the [Technical Support]({{< ref "/total/python-net/technical-support" >}}) section.
