---
id: running-in-docker
url: total/python-net/running-in-docker
title: Running in Docker
weight: 5
description: "Learn how to run GroupDocs.Total for Python via .NET inside Docker containers with examples, troubleshooting tips, and best practices."
keywords: docker, dockerfile, linux
productName: GroupDocs.Total for Python via .NET
hideChildren: False
toc: True
---

In this guide, you’ll learn how to run GroupDocs.Total for Python via .NET inside a Docker container using simple code examples.

## Limitations

Currently, not all GroupDocs Python APIs support Linux. This limitation will be addressed in upcoming releases.

APIs that support Linux are the following:

* [groupdocs‑comparison‑net](https://pypi.org/project/groupdocs-comparison-net/)
* [groupdocs‑watermark‑net](https://pypi.org/project/groupdocs-watermark-net/)
* [groupdocs‑metadata‑net](https://pypi.org/project/groupdocs-metadata-net/)
* [groupdocs‑merger‑net](https://pypi.org/project/groupdocs-merger-net/)

This guide will show how to use GroupDocs.Merger for Python via .NET in Docker container.

## Dependencies

When using the GroupDocs Python SDK in a Linux environment, make sure the following packages are installed, as they are required for proper library operation:

* `libicu` — ICU library (must not exceed version 70)
* `libssl1.1` — OpenSSL library required by .NET Core 3.1

## Basic Example

This is the most basic example that shows how to run GroupDocs Python APIs in Docker. The example demonstrates how to merge tow DOCX files using GroupDocs.Merger in Docker container.

{{< alert style="info" >}}
You can download this sample application from [here](/total/net/_sample_files/getting-started/running-in-docker/basic-example.zip).
{{< /alert >}}

### Project Structure

The sample application has the following folder structure:

```
📂 basic-example/
├── 📂 output/                   # Output directory for converted files
├── 📄 .dockerignore             # Files to exclude from Docker build context
├── 📄 appendix.docx             # Sample input document to merge
├── 📄 beginning.docx            # Sample input document to merge
├── 📄 Dockerfile                # Docker container definition
├── 📄 GroupDocs.Total.lic       # License file (optional)
├── 📄 merge_docx_files.py       # Main application code
├── 📄 README.md                 # Build and run instructions
└── 📄 requirements.txt          # Application dependencies
```

We’re using a Python 3.11 slim image and installing required .NET dependencies `libicu` and `libssl1.1` manually.
Here are the most essential parts:

{{< tabs "example_run_in_docker" >}}

{{< tab "Dockerfile" >}}  
{{< highlight dockerfile "" >}}
# Use Python 3.11 slim base image which is smaller than the default base image
FROM python:3.11-slim

# Install prerequisites from a reliable source
ENV SNAPSHOT_DATE=20220328T000000Z
RUN echo "deb [trusted=yes] http://snapshot.debian.org/archive/debian/${SNAPSHOT_DATE} bullseye main" \
        > /etc/apt/sources.list.d/debian-archive.list && \
    apt-get -o Acquire::Check-Valid-Until=false update && \
    apt-get install -y --no-install-recommends \
        libicu67 \
        libssl1.1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set workdir 
WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the app
CMD ["python", "merge_docx_files.py"]
{{< /highlight >}}
{{< /tab >}}

{{< tab "merge_docx_files.py" >}}  
{{< highlight python "" >}}
import os
from groupdocs.merger import License, Merger

def merge_docx_files():
    # Get license file absolute path
    license_path = os.path.abspath("./GroupDocs.Total.lic")

    if os.path.exists(license_path):
        # Create License and set the path
        license = License()
        license.set_license(license_path)

    # Ensure output directory exists
    os.makedirs("./output", exist_ok=True)

    # Initialize the merger
    with Merger("./beginning.docx") as merger:
        # Append appendix.docx to beginning.docx
        merger.join("./appendix.docx")
        # Save the merged document
        merger.save("./output/merged.docx")

if __name__ == "__main__":
    merge_docx_files()
{{< /highlight >}}
{{< /tab >}}

{{< tab "requirements.txt" >}}  
{{< highlight text "" >}}
groupdocs-merger-net>=25.3
{{< /highlight >}}
{{< /tab >}}

{{< tab "Input files" >}}  
{{< tab-text >}}
Sample input files [beginning.docx](/total/python-net/_sample_files/getting-started/running-in-docker/beginning.docx) and [appendix.docx](/total/python-net/_sample_files/getting-started/running-in-docker/appendix.docx).
{{< /tab-text >}}
{{< /tab >}}

{{< /tabs >}}

### Building and Running the Application

To create the Docker image, run the following command in the directory containing the Dockerfile:

```bash
docker build -t groupdocs-merger-net:basic-example .
```

To run the application and mount the output directory:

```bash
docker run -it --rm -v ${PWD}/output:/app/output groupdocs-merger-net:basic-example
```

### Command Explanation

- `-it`: Runs the container in interactive mode
- `--rm`: Automatically removes the container when it exits
- `-v`: Mounts the host directory to the container directory for file output


### App Output

The app creates the merged DOCX file [merged.docx](/total/python-net/_sample_files/getting-started/running-in-docker/merged.docx) in the `output` folder.


## Troubleshooting

### Font Issues

If you encounter font-related errors:

```bash
# Install additional fonts
RUN apt-get update && apt-get install -y fonts-liberation fonts-dejavu-core
```

### Exceptions

In case you experience any other exeptions when running the application please contact us using the [GroupDocs Free Support Forum](https://forum.groupdocs.com/) and we'll be happy to help.
