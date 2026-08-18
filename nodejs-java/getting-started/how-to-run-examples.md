---
id: how-to-run-examples
url: total/nodejs-java/how-to-run-examples
title: How to Run Examples
weight: 7
description: "Learn how to clone, configure, and run GroupDocs.Total for Node.js via Java example projects."
keywords: How to run examples, basic usage, code examples
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

The complete project [GroupDocs.Total for Node.js via Java — Code Examples](https://github.com/groupdocs-total/GroupDocs.Total-for-Node.js-via-Java) with runnable examples and sample files is hosted on GitHub. The structure and commands below are based on this repository and its README.

## Prerequisites

Before running examples, make sure your environment meets the [System Requirements]({{< ref "total/nodejs-java/getting-started/system-requirements" >}}) and [Installation]({{< ref "total/nodejs-java/getting-started/installation" >}}) guides:

- **Node.js**: 20 LTS or later
- **Java**: JRE/JDK 8+ (17 LTS recommended)
- **Java environment**: `JAVA_HOME` set and added to `PATH`

Windows PowerShell:

```powershell
$env:JAVA_HOME="C:\Program Files\Java\jdk-17"
$env:Path="$env:JAVA_HOME\bin;$env:Path"
```

Linux/macOS:

```bash
export JAVA_HOME=/usr/lib/jvm/java-17
export PATH=$JAVA_HOME/bin:$PATH
```

## Run examples using npm

To get started, make sure that [Node.js](https://nodejs.org/) and Java are installed and configured as described above.

1. **Clone the repository with examples**

   ```bash
   git clone git@github.com:groupdocs-total/GroupDocs.Total-for-Node.js-via-Java.git
   ```

2. **Navigate to the `Examples` folder**

   ```bash
   cd ./GroupDocs.Total-for-Node.js-via-Java/Examples
   ```

3. **Install dependencies**

   ```bash
   npm install
   ```

   This pulls [`@groupdocs/groupdocs.total`](https://www.npmjs.com/package/@groupdocs/groupdocs.total) from npm. We typically keep the dependency on the latest published version; to use another version, change it in `package.json`.

   If installation fails with native build errors, review the build tools section in [System Requirements]({{< ref "total/nodejs-java/getting-started/system-requirements" >}}).

4. **Configure license (optional)**

   If you have a license file, you can set the license path in the `run_all_examples.js` file. By default, the runner checks for the `GROUPDOCS_LICENSE_PATH` (or `GROUPDOCS_LIC_PATH`) environment variable or looks for files with the `.lic` extension in the `Examples` directory. You can also [get a temporary license](https://purchase.groupdocs.com/temporary-license) to test all the features.

   Without a license the APIs run in evaluation mode and add trial watermarks to output.

5. **Run all examples**

   ```bash
   npm start
   ```

   List every example, then run one on its own:

   ```bash
   node run_all_examples.js --list
   node run_all_examples.js --example ViewerRenderToHtml
   ```

   You can also run an individual example by navigating to the folder containing the example script and running it. Output files are placed in the same folder as the script file.

## More Resources

Find additional details and examples in the [GroupDocs.Total for Node.js via Java documentation](https://docs.groupdocs.com/total/nodejs-java/).

We also offer **GroupDocs.Total** packages for other platforms:
* [**GroupDocs.Total for .NET**](https://products.groupdocs.com/total/net/)
* [**GroupDocs.Total for Java**](https://products.groupdocs.com/total/java/)
* [**GroupDocs.Total for Python via .NET**](https://products.groupdocs.com/total/python-net/)
