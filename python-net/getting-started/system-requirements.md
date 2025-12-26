---
id: system-requirements
url: total/python-net/system-requirements
title: System requirements
weight: 2
description: "GroupDocs.Total for Python via .NET does not require any external software to be installed such as Microsoft Word, Microsoft Excel or Microsoft PowerPoint for file rendering."
keywords: file rendering
productName: GroupDocs.Total for Python via .NET
hideChildren: False
toc: True
---

## General Requirements

- [Python](https://www.python.org/downloads/) versions **3.9–3.11** are supported

## Supported Operating Systems

### Windows

* Microsoft Windows 11 (x64)
* Microsoft Windows 10 (x64, x86)
* Microsoft Windows 7, 8, 8.1, Vista, XP (x64, x86)
* Microsoft Windows Server 2003 and later

### Linux and macOS (partial support)

Some of the supported packages in GroupDocs.Total include macOS support for Intel and/or Apple Silicon (M-series) processors.

The following table shows the platform support matrix:

| Package | Windows 32-bit | Windows 64-bit | Linux x86_64 | macOS 10.14 x86 | macOS 11.0 Apple Silicon |
|---|---|---|---|---|---|
| [groupdocs‑assembly‑net](https://pypi.org/project/groupdocs-assembly-net/) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |  |  |  |
| [groupdocs‑comparison‑net](https://pypi.org/project/groupdocs-comparison-net/) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |
| [groupdocs‑conversion‑net](https://pypi.org/project/groupdocs-conversion-net/) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |
| [groupdocs‑merger‑net](https://pypi.org/project/groupdocs-merger-net/) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |  |
| [groupdocs‑metadata‑net](https://pypi.org/project/groupdocs-metadata-net/) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |
| [groupdocs‑redaction‑net](https://pypi.org/project/groupdocs-redaction-net/) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |  | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |
| [groupdocs‑signature‑net](https://pypi.org/project/groupdocs-signature-net/) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |  | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |
| [groupdocs‑viewer‑net](https://pypi.org/project/groupdocs-viewer-net/) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |
| [groupdocs‑watermark‑net](https://pypi.org/project/groupdocs-watermark-net/) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) | ![(tick)](/total/python-net/_images/check-blue.png) |


You can install individual packages based on your requirements and the platforms you are targeting.

## Additional System Libraries

### Linux and macOS System Requirements

GroupDocs.Total for Python via .NET relies on `libgdiplus` for processing images or documents that contain images. 

#### Linux installation

When using GroupDocs.Total in a Linux environment, the following packages should be installed for proper library operation:

1. **libgdiplus** - Mono library providing a GDI+-compatible API on non-Windows operating systems.  
2. **libx11-dev** - Required for drawing functions (image/font rendering).  
3. **fontconfig** - Enables font lookup for text rendering with System.Drawing.  
4. **ttf-mscorefonts-installer** - Provides Microsoft-compatible fonts required by GroupDocs.Total.

To install packages on Debian-based Linux distributions, use [apt-get](https://wiki.debian.org/apt-get):

```bash
sudo apt-get update
sudo apt-get install -y libgdiplus libx11-dev fontconfig ttf-mscorefonts-installer
```

If some packages are not available, you can add the contrib repository:

```bash
RUN sed -i'.bak' 's/$/ contrib/' /etc/apt/sources.list
```

#### macOS installation

The library is required and can be installed using the [Homebrew](https://brew.sh/) package manager:

```ps
brew install mono-libgdiplus
```

Ensure `libgdiplus` is installed if you encounter issues with processing images or documents that contain images.