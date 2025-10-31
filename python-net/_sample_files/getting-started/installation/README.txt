# This is example installation process

## Create and Activate a Virtual Environment

Create a virtual environment:

{{< tabs "example1">}}
{{< tab "Windows" >}}
```ps
py -3.11 -m venv .venv
```
{{< /tab >}}
{{< tab "macOS" >}}
```bash
python3 -3.11 -m venv .venv
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
{{< tab "macOS" >}}
```bash
source .venv/bin/activate
```
{{< /tab >}}
{{< /tabs >}}

## Install `groupdocs-total-net` Package from PyPI

```python
py -m pip install groupdocs-total-net
```

### Install `groupdocs-total-net` from releases

```python
py -m pip install groupdocs_total_net-25.10.0-py3-none-any.whl
```
