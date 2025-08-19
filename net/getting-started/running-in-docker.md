---
id: running-in-docker
url: total/net/running-in-docker
title: Running in Docker
weight: 5
description: "Learn how to run GroupDocs.Total for .NET in Docker containers with complete examples, troubleshooting tips, and best practices for document processing in containerized environments."
keywords: docker, dockerfile, linux
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

In this documentation topic you will learn how to run GroupDocs.Total for .NET in Docker container based on simple code examples.

## Limitations

If the target framework is .NET 6 or over, due to limitations in the System.Drawing.Common version 6.0.0 (see [Microsoft documentation](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only#new-behavior)), you need to add the following setting to the `.csproj` file.

```xml
<ItemGroup>
    <RuntimeHostConfigurationOption Include="System.Drawing.EnableUnixSupport" Value="true" />
</ItemGroup>
```

or you can also add `runtimeconfig.json` file to the root of you project 

```json
{
  "configProperties": {
    "System.Drawing.EnableUnixSupport": true
  }
}
```
## Dependencies

When using GroupDocs.Total in Linux environment, the following packages should be installed as they are required for the proper library work:

1. **libgdiplus** - is the Mono library that provides a GDI+-compatible API on non-Windows operating systems.
2. **libx11-dev** - Needed for drawing functions (image/font rendering).
3. **fontconfig** - Enables font lookup for text rendering with System.Drawing.
4. **ttf-mscorefonts-installer** - package with Microsoft compatible fonts, required for GroupDocs.Total.
 
To install packages on Debian-based Linux distributions use [apt-get](https://wiki.debian.org/apt-get) utility:

```bash
sudo apt-get update
sudo apt-get install -y libgdiplus libx11-dev fontconfig ttf-mscorefonts-installer
```

In case packages are not available, you can add the contrib repository:

```bash
RUN sed -i'.bak' 's/$/ contrib/' /etc/apt/sources.list
```

## Basic Example

This is the most basic example that shows how to run GroupDocs.Total for .NET in Docker. The example demonstrates document conversion functionality using a simple console application.

{{< alert style="info" >}}
You can download this sample application from [here](/total/net/_sample_files/getting-started/running-in-docker/basic-example.zip).
{{< /alert >}}

### Project Structure

The sample application has the following folder structure:

```
📂 basic-example/
├── 📂 output/                   # Output directory for converted files
├── 📄 .dockerignore             # Files to exclude from Docker build context
├── 📄 business-plan.docx        # Sample input document
├── 📄 Dockerfile                # Docker container definition
├── 📄 GroupDocs.Total.lic       # License file (optional)
├── 📄 Program.cs                # Main application code
├── 📄 BasicExample.csproj       # .NET project file
└── 📄 BasicExample.sln          # Visual Studio solution file
```

We're using the official Microsoft .NET 6 SDK image to build and run the application. This approach provides a complete development environment with all necessary tools. Here are the most essential parts:

{{< tabs "example1" >}}

{{< tab "Dockerfile" >}}  
{{< highlight dockerfile "" >}}
FROM mcr.microsoft.com/dotnet/sdk:6.0
WORKDIR /app

# Install dependencies
RUN sed -i'.bak' 's/$/ contrib/' /etc/apt/sources.list
RUN apt update && apt install -y \
    libgdiplus \
    libx11-dev \
    fontconfig \
    ttf-mscorefonts-installer

# Copy the app
COPY . .

# Run the app
ENTRYPOINT ["dotnet", "run", "--framework", "net6.0", "--verbosity", "normal"]
{{< /highlight >}}
{{< /tab >}}

{{< tab "Program.cs" >}}  
{{< highlight cs "" >}}
using System.IO;
using GroupDocs.Conversion;
using GroupDocs.Conversion.Options.Convert;

// Set the license (Optional)
string licensePath = Path.GetFullPath("./GroupDocs.Total.lic");
License license = new License();
license.SetLicense(licensePath);

// Initialize convert options and converter
PdfConvertOptions options = new PdfConvertOptions();
Converter converter = new Converter("./business-plan.docx");

// Convert and save file
converter.Convert("./output/business-plan.pdf", options);
{{< /highlight >}}
{{< /tab >}}

{{< tab "BasicExample.csproj" >}}  
{{< highlight xml "" >}}
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <RuntimeHostConfigurationOption Include="System.Drawing.EnableUnixSupport" Value="true" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="GroupDocs.Total" Version="25.7.0" />
  </ItemGroup>

</Project>
{{< /highlight >}}
{{< /tab >}}

{{< tab "business-plan.docx" >}}  
{{< tab-text >}}
Sample input file: [Download business-plan.docx](/total/net/_sample_files/getting-started/running-in-docker/business-plan.docx)
{{< /tab-text >}}
{{< /tab >}}

{{< /tabs >}}

### Building and Running the Application

To create the Docker image, run the following command in the directory containing the Dockerfile:

```bash
docker build -t groupdocs-total:basic-example .
```

To run the application and mount the output directory:

{{< tabs "run-commands" >}}
{{< tab "Windows (PowerShell)" >}}
```bash
docker run -it --rm -v ${PWD}/output:/app/output groupdocs-total:basic-example
```
{{< /tab >}}
{{< tab "Windows (Command Prompt)" >}}
```cmd
docker run -it --rm -v %cd%/output:/app/output groupdocs-total:basic-example
```
{{< /tab >}}
{{< tab "Linux/macOS" >}}
```bash
docker run -it --rm -v $(pwd)/output:/app/output groupdocs-total:basic-example
```
{{< /tab >}}
{{< /tabs >}}

The application creates the output `business-plan.pdf` file and places it into the `output` folder on your host machine. You can download expected output file from [here](/total/net/_sample_files/getting-started/running-in-docker/business-plan.pdf).

### Command Explanation

- `-it`: Runs the container in interactive mode
- `--rm`: Automatically removes the container when it exits
- `-v`: Mounts the host directory to the container directory for file output

## Troubleshooting

### Font Issues

If you encounter font-related errors:

```bash
# Install additional fonts
RUN apt-get update && apt-get install -y fonts-liberation fonts-dejavu-core
```

### Exceptions

In case you experience any other exeptions when running the application please contact us using [GroupDocs Free Support Forum](https://forum.groupdocs.com/) and we'll be happy to help.

