---
id: system-requirements
url: total/java/system-requirements
title: System requirements
weight: 3
description: "GroupDocs.Total for Java does not require any external software to be installed such as Microsoft Word, Microsoft Excel or Microsoft PowerPoint for document manipulation."
keywords: document manipulation, file manipulation
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---
{{< alert style="info" >}}

GroupDocs.Total for Java does not require any external software to be installed such as Microsoft Word, Microsoft Excel or Microsoft PowerPoint. To install GroupDocs.Total for Java just follow one of the ways as described in the [Installation]({{< ref "installation" >}}) section.

{{< /alert >}}

## Supported Java Versions

GroupDocs.Total for Java supports the following Java versions:

- Java 8
- Java 11
- Java 17 (LTS)
- Java 21 (LTS)

{{< alert style="info" >}}

Make sure you are using an up-to-date JDK from a supported vendor (e.g., Oracle, Eclipse Temurin, Amazon Corretto).

{{< /alert >}}
## Supported Operating Systems

GroupDocs.Total for Java is platform-independent and can be used on any OS where Java is supported. Officially tested and supported operating systems include:

- Windows 10/11 (x64)
- Windows Server 2016/2019/2022
- Linux (Ubuntu, CentOS, Debian, etc. – x64)
- macOS (Intel and Apple Silicon, via Rosetta or natively on Java 17+)

{{< alert style="info" >}}

Ensure the file system and permissions allow your application to read/write files and create temporary directories if needed.

{{< /alert >}}

## Development Environments

You can develop with GroupDocs.Total for Java using any Java-supporting IDE:

- IntelliJ IDEA (recommended)
- Eclipse
- NetBeans
- Visual Studio Code (with Java plugin)

Supported build tools:

- **Maven** – Recommended for managing dependencies.
- **Gradle** – Supported with official artifacts.
- Ant – Manually configurable.

## Memory and Performance Recommendations

- **Minimum RAM:** 2 GB  
- **Recommended RAM:** 4 GB or more for processing large documents  
- **Disk Space:** At least 500 MB free disk space for libraries, logs, and temp files  
- **Temporary Storage:** Ensure the system has access to a temporary directory (`java.io.tmpdir`)
- **JVM heap size:**  For large document processing (e.g., big PDFs, Excel files), consider increasing the heap size:

```sh
java -Xms512m -Xmx2048m -jar your-app.jar
```

## Additional Notes

- **JVM Language Compatibility:** Works with Kotlin, Scala, Groovy, and any language running on the JVM
- **Headless Environments:** Supported (e.g., Linux server without GUI)
- **Docker:** Fully compatible. Ensure Java and required system libraries are installed in the container

## Related Links

- [Installation via Maven](https://docs.groupdocs.com/total/java/installation/)
- [Licensing Guide](https://docs.groupdocs.com/total/java/licensing/)
- [Product Overview](https://products.groupdocs.com/total/java/)