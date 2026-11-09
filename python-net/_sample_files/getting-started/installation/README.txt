# This is example installation process

## Create and Activate a Virtual Environment

Create a virtual environment:

{{< tabs "example1">}}
{{< tab "Windows" >}}
```ps
py -3.11 -m venv .venv
```
{{< /tab >}}
{{< tab "Linux and macOS" >}}
```bash
python3 -m venv .venv
```
{{< /tab >}}
{{< /tabs >}}

Activate a virtual environment:

{{< tabs "example2">}}
{{< tab "Windows" >}}
```ps
.venv\Scripts\activate
```
{{< /tab >}}
{{< tab "Linux and macOS" >}}
```bash
source .venv/bin/activate
```
{{< /tab >}}
{{< /tabs >}}

## Install `groupdocs-total-net` Package from PyPI

```bash
py -m pip install groupdocs-total-net
```

### Install `groupdocs-total-net` from releases

Put the metapackage file and the 14 product wheels for your platform in one folder, then run in it:

```bash
py -m pip install --no-index --find-links . groupdocs-total-net==26.11.0
```
