---
id: licensing-and-evaluation
url: total/nodejs-java/licensing-and-evaluation
title: Licensing and evaluation
weight: 6
keywords: free, free trial, evaluation, groupdocs.total
description: "GroupDocs.Total for Node.js via Java provides different plans for purchasing or offers a Free Trial and a 30-day Temporary License for evaluation."
productName: GroupDocs.Total for Node.js via Java
hideChildren: False
toc: True
aliases:
    - /total/nodejs-java/licensing-and-subscription/
---
To study the system, you may want quick access to the API. To make this easier, GroupDocs.Total provides different plans for purchase and offers a Free Trial and a 30-day Temporary License for evaluation.

{{< alert style="info" >}}

Note that there are a number of general policies and practices that guide you on how to evaluate, properly license, and purchase our products. You can find them in the [Purchase Policies and FAQ](https://purchase.groupdocs.com/policies/) section.

{{< /alert >}}

## Purchased License

After buying, apply the license file or include it as an embedded resource. 

License needs to be set:
- Only once per application, using the unified Total `License` API
- Before using any other GroupDocs.Total classes
    
### License Applying Options

Licenses can be applied from different locations:

*   Explicit path
*   The folder containing your application
*   As a Metered License that allows you to pay for your usage. For details, see the [Metered Licensing FAQ](https://purchase.groupdocs.com/faqs/licensing/metered/).

Use a **GroupDocs.Total for Node.js via Java** (or Total Product Family) license with this package. Total uses a **static** license API — set it once at startup; it applies to all products in the suite.

Calling `License.setLicense` multiple times is not harmful, it simply wastes processor time.

Calling `setMeteredKey` multiple times is not harmful either but wastes processor time and can accumulate consumption improperly.

#### Apply the License

After obtaining the license, set it. This section explains how to do this. When developing your application, call `License.setLicense` in your startup code before using the GroupDocs.Total classes.

##### Set a License from a File

The following code snippet shows how to set a license from a file:

{{< tabs "example1">}}
{{< tab "JavaScript" >}}

```js
import { License } from '@groupdocs/groupdocs.total';
import { existsSync } from 'fs';

const licensePath = 'GroupDocs.Total.lic';

if (!existsSync(licensePath)) {
    console.log('License file not found. Running in evaluation mode.');
    process.exit(0);
}

License.setLicense(licensePath);
console.log('License set successfully.');
```

{{< /tab >}}
{{< /tabs >}}

##### Set a License from a Stream

The following code snippet shows how to set a license from a stream:

{{< tabs "example2">}}
{{< tab "JavaScript" >}}

```js
import { License, readDataFromStream } from '@groupdocs/groupdocs.total';
import { createReadStream, existsSync } from 'fs';

const licensePath = 'GroupDocs.Total.lic';

if (!existsSync(licensePath)) {
    console.log('License file not found. Running in evaluation mode.');
    process.exit(0);
}

const stream = await readDataFromStream(createReadStream(licensePath));
License.setLicense(stream);
console.log('License set successfully.');
```

{{< /tab >}}
{{< /tabs >}}

#### Apply Metered License

You can set the `Metered` license as an alternative to license file. It is useful for the customers who want to be billed based on the usage of the API features. For more details, please refer to [Metered Licensing FAQ](https://purchase.groupdocs.com/faqs/licensing/metered/).

Metered keys are applied per product. The following code snippet shows how to use the metered license for GroupDocs.Viewer and GroupDocs.Conversion:

{{< tabs "example3">}}
{{< tab "JavaScript" >}}
```js
import { ViewerMetered } from '@groupdocs/groupdocs.total';
import java from 'java';

const Metered = java.import('com.groupdocs.conversion.licensing.Metered');

const publicKey = ''; // Your public license key
const privateKey = ''; // Your private license key

// Set metered keys for GroupDocs.Viewer
const meteredViewer = new ViewerMetered();
meteredViewer.setMeteredKey(publicKey, privateKey);

// Get amount (MB) consumed
const amountConsumed = ViewerMetered.getConsumptionQuantity();
console.log('Amount (MB) consumed: ' + amountConsumed);

// Get count of credits consumed
const creditsConsumed = ViewerMetered.getConsumptionCredit();
console.log('Credits consumed: ' + creditsConsumed);

// Set metered keys for GroupDocs.Conversion
const meteredConversion = new Metered();
meteredConversion.setMeteredKey(publicKey, privateKey);
```
{{< /tab >}}
{{< /tabs >}}

### Changing the License File Name

You do not have to name the license file "GroupDocs.Total.lic". Feel free to rename it as you prefer, and use that name when setting the license in your application.

### "Cannot find license filename" Exception

When you buy and download a license from the GroupDocs website, the license file is named "GroupDocs.Total.lic." Download it using your browser. Sometimes, browsers recognize it as XML and add the .xml extension, making the full file name "GroupDocs.Total.lic.XML" on your computer.

If Microsoft Windows is set to hide file extensions (which is the default in most installations), the license file will show as "GroupDocs.Total.lic" in Windows Explorer. You might assume this is the actual file name and call `License.setLicense` with "GroupDocs.Total.lic", but there is no such file, leading to an exception.

To fix this issue, rename the file to remove the hidden .xml extension. Additionally, we suggest disabling the **Hide extensions** option in Microsoft Windows.

## How to Evaluate GroupDocs.Total

You can also try GroupDocs.Total without buying a license.

### Free Trial

The evaluation version is identical to the purchased one; it becomes licensed once you set the license. You can set the license using methods described in the following sections of this article.

The evaluation version has the following limitations:

- Rendering is limited to the first 2 pages.
- Trial badges are added to the top of a rendered page.

### Temporary License

If you want to test GroupDocs.Total without the limitations of the trial version, request a 30-day Temporary License. For details, see the ["Get a Temporary License"](https://purchase.groupdocs.com/temporary-license/) page.
