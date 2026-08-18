---
id: installation
url: total/nodejs-java/installation
title: Install GroupDocs.Total for Node.js via Java 
linkTitle: Installation
weight: 4
description: "Install GroupDocs.Total for Node.js via Java using npm or an offline package. Includes prerequisites, Java setup, verification, and troubleshooting."
keywords: installation, npm, nodejs, java
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
---

### Prerequisites

- Node.js: 20 LTS or later
- Java: JRE/JDK 8+ (recommended 17 LTS)
- Build tools if needed by your environment (node-gyp toolchain)

See full details on the [System Requirements]({{< ref "total/nodejs-java/getting-started/system-requirements" >}}) page.

### Install from npm

All Java-bridged packages are hosted on npm. Install the library into your project using your preferred package manager:

```bash
# npm
npm install @groupdocs/groupdocs.total

# yarn
yarn add @groupdocs/groupdocs.total

# pnpm
pnpm add @groupdocs/groupdocs.total
```

The install step also downloads the Total library used by the Node.js bridge.

### Set up Java (JAVA_HOME)

Ensure your Java installation is available on PATH and `JAVA_HOME` is set.

Windows (PowerShell):

```powershell
$env:JAVA_HOME="C:\Program Files\Java\jdk-17"
$env:Path="$env:JAVA_HOME\bin;$env:Path"
```

Linux/macOS (Bash):

```bash
export JAVA_HOME=/usr/lib/jvm/java-17
export PATH="$JAVA_HOME/bin:$PATH"
```

See the [System Requirements]({{< ref "total/nodejs-java/getting-started/system-requirements" >}}) page for more details.

### Verify installation

Create a small script (e.g., `check.js`) and run it with Node.js:

{{< tabs "check-installation" >}}
{{< tab "check.js" >}}  
```js
import { Viewer } from '@groupdocs/groupdocs.total';

try {
  console.log('GroupDocs.Total loaded:', typeof Viewer === 'function');
  console.log('Java bridge initialized successfully.');
  process.exit(0);
} catch (e) {
  console.error('Failed to load GroupDocs.Total:', e);
  process.exit(1);
}
```
{{< /tab >}}
{{< /tabs >}}


And then run the script to verify the installation:

```bash
node check.js
```

### Download from GroupDocs.Releases (offline)

You can download a package archive from [GroupDocs.Releases](https://releases.groupdocs.com/total/nodejs-java/#direct-download) and add it to your app. After downloading the `.tar` file, install it locally:

```bash
npm install ./groupdocs-groupdocs.total-<version>.tar
```

Alternatively, configure npm to use your corporate registry or proxy, then install using the standard command.

### Minimal JavaScript app example

Once you have installed the GroupDocs.Total package, here's a minimal example of how you can use it in a Node.js application.

1. **Create a JavaScript file** (e.g., `app.js`) in your project's root directory.

2. **Import the GroupDocs.Total module** and implement a simple file viewing functionality:

   {{< tabs "render-docx-to-html">}}
   {{< tab "JavaScript" >}}
   ```js
   import { Viewer } from '@groupdocs/groupdocs.total';
   import java from 'java';

   const HtmlViewOptions = java.import('com.groupdocs.viewer.options.HtmlViewOptions');

   // Path to the file you want to render
   const filePath = 'contract.docx';

   // Initialize viewer
   const viewer = new Viewer(filePath);

   // Render the file to HTML
   viewer.view(HtmlViewOptions.forEmbeddedResources());
   viewer.close();

   process.exit(0);
   ```
   {{< /tab >}}
   {{< tab "contract.docx" >}}
   {{< tab-text >}}
   `contract.docx` is the sample file used in this example. Click [here](/total/nodejs-java/_sample_files/contract.docx) to download it.
   {{< /tab-text >}}
   {{< /tab >}}
   {{< /tabs >}}

3. **Run the app** by executing the following command in your terminal:

   ```bash
   node app.js
   ```

This minimal example converts a document to HTML format. The output will contain rendered pages in HTML format.

{{< alert style="info" >}}
Always import `@groupdocs/groupdocs.total` before calling `java.import(...)`. Main entry points such as `Viewer` and `Converter` are exported from the package; options and helper classes live in the suite JAR and are loaded with `java.import('fully.qualified.ClassName')`.
{{< /alert >}}

### Troubleshooting installation

- node-gyp toolchain not found: install the required build tools for your OS (see System Requirements).
- Java not detected: set `JAVA_HOME` and add `<JAVA_HOME>/bin` to `PATH`.
- Corporate proxy: configure npm proxy settings before running install. Allow HTTPS access to GroupDocs release storage if the library download fails during install.
- Permission errors: ensure you have write access to the project directory and cache folders.
- `java.import(...)` returns null / ClassNotFound: import `@groupdocs/groupdocs.total` first; use the full Java class name.
