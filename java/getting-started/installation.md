---
id: installation
url: total/java/installation
title: Install GroupDocs.Total for Java
linkTitle: Installation
weight: 4
keywords: installation, maven
description: "This topic describes how to install GroupDocs.Total for Java."
productName: GroupDocs.Total for Java
hideChildren: False
toc: True
---

## Install using Maven

All Java packages are hosted at [GroupDocs Artifact Repository](https://repository.groupdocs.com/). You can easily reference GroupDocs.Total for Java API directly in your Maven project using following steps.

### Add GroupDocs Artifact Repository

Specify repository configuration and location in the Maven `pom.xml`:

{{< tabs "example1">}}
{{< tab "pom.xml" >}}
```xml
<repositories>
    <repository>
        <id>GroupDocs Artifact Repository</id>
        <name>GroupDocs Artifact Repository</name>
        <url>https://releases.groupdocs.com/java/repo/</url>
    </repository>
</repositories>
```
{{< /tab >}}
{{< /tabs >}}

### Add GroupDocs.Total as a dependency

Define GroupDocs.Total for Java API dependency in your `pom.xml`:

{{< tabs "example2">}}
{{< tab "pom.xml" >}}
```xml
<dependencies>
    <dependency>
        <groupId>com.groupdocs</groupId>
        <artifactId>groupdocs-total</artifactId>
        <version>24.9</version> 
    </dependency>
</dependencies>
```
{{< /tab >}}
{{< /tabs >}}
