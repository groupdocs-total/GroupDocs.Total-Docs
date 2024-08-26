---
id: licensing-and-evaluation
url: total/net/licensing-and-evaluation
title: Licensing and evaluation
weight: 5
keywords: free, free trial, evaluation, groupdocs.total
description: "GroupDocs.Total provides different plans for purchasing or offers a Free Trial and a 30-day Temporary License for evaluation."
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
aliases:
    - /total/net/licensing-and-subscription/
---
To study the system, you may want quick access to the API. To make this easier, GroupDocs.Total provides different plans for purchase and offers a Free Trial and a 30-day Temporary License for evaluation.

{{< alert style="info" >}}

Note that there are a number of general policies and practices that guide you on how to evaluate, properly license, and purchase our products. You can find them in the [Purchase Policies and FAQ](https://purchase.groupdocs.com/policies) section.

{{< /alert >}}

## Purchased License

After buying, apply the license file or include it as an embedded resource. 

License needs to be set:
- Only once per application domain and only once for each GroupDocs product you want to use
- Before using any other GroupDocs.Total classes
    
### License Applying Options

Licenses can be applied from different locations:

*   Explicit path
*   The folder containing the _GroupDocs.Total.dll_ file
*   The folder containing the assembly that called _GroupDocs.Total.dll_
*   The folder containing the entry assembly (your _.exe_)
*   As a Metered License that allows you to pay for your usage. For details, see the [Metered Licensing FAQ](https://purchase.groupdocs.com/faqs/licensing/metered/).
*   As an embedded resource
When you reference _GroupDocs.Total.dll_ in the application, the library is copied to your output directory (unless **Copy Local** in the properties for that entry is set to false). The easiest way to set a license is often to place the license file in the same folder as _GroupDocs.Total.dll_ and specify just the filename without the path.

Use the `SetLicense` method to license a specific GroupDocs product. For example, to apply license for GroupDocs.Viewer component [SetLicense](https://reference.groupdocs.com/viewer/net/groupdocs.viewer/license/setlicense/) method has to be used.

Calling `SetLicense` multiple times is not harmful, it simply wastes processor time.

Calling `SetMeteredKey` multiple times is not harmful either but wastes processor time and can accumulate consumption improperly.

#### Apply the License

After obtaining the license, set it. This section explains how to do this. When developing your application, call the `SetLicense` method in your startup code before using the GroupDocs.Total classes.

##### Set a License from a File

The following code snippet shows how to set a license from file:

{{< tabs "example1">}}
{{< tab "C#" >}}

```csharp
string licensePath = "GroupDocs.Total.lic";
GroupDocs.Viewer.License licenseViewer = new GroupDocs.Viewer.License();
licenseViewer.SetLicense(licensePath);

GroupDocs.Conversion.License licenseConversion = new GroupDocs.Conversion.License();
licenseConversion.SetLicense(licensePath);

// Set licenses for other GroupDocs products you are going to use

```

{{< /tab >}}
{{< /tabs >}}

##### Set a License from a Stream

The following code snippet shows how to set a license from a stream:

{{< tabs "example2">}}
{{< tab "C#" >}}

```csharp
string licensePath = "GroupDocs.Total.lic";
using (FileStream fileStream = File.OpenRead(licensePath))
{
    GroupDocs.Viewer.License licenseViewer = new GroupDocs.Viewer.License();
    licenseViewer.SetLicense(fileStream);

    GroupDocs.Conversion.License licenseConversion = new GroupDocs.Conversion.License();
    licenseConversion.SetLicense(fileStream);

    // Set licenses for other GroupDocs products you are going to use
}
```

{{< /tab >}}
{{< /tabs >}}

#### Apply Metered License

You can set the `Metered` license as an alternative to license file. It is useful for the customers who want to be billed based on the usage of the API features. For more details, please refer to [Metered Licensing FAQ](https://purchase.groupdocs.com/faqs/licensing/metered).

The following code snippet shows how to use the metered license:

{{< tabs "example3">}}
{{< tab "C#" >}}
```csharp
string publicKey = ""; // Your public license key
string privateKey = ""; // Your private license key

// Set metered keys for GroupDocs.Viewer
GroupDocs.Viewer.Metered meteredViewer = new GroupDocs.Viewer.Metered();
meteredViewer.SetMeteredKey(publicKey, privateKey);

// Get amount (MB) consumed
decimal amountConsumed = GroupDocs.Viewer.Metered.GetConsumptionQuantity();
Console.WriteLine("Amount (MB) consumed: " + amountConsumed);

// Get count of credits consumed
decimal creditsConsumed = GroupDocs.Viewer.Metered.GetConsumptionCredit();
Console.WriteLine("Credits consumed: " + creditsConsumed);

// Set metered keys for GroupDocs.Conversion
GroupDocs.Conversion.Metered meteredConversion = new GroupDocs.Conversion.Metered();
meteredConversion.SetMeteredKey(publicKey, privateKey);

```
{{< /tab >}}
{{< /tabs >}}

#### Apply License from an Embedded Resource

Instead of using a license file, you can install the license as an embedded resource. To do this, add a license to the project and specify the license name in the `SetLicense` method without specifying the full path to this file.

{{< alert style="info" >}}
To use the embedded license, add it to your project and set the **Build Action** property of this file to "Embedded Resource". Ensure that the license name in the embedded resources matches the string parameter of the `SetLicense` method.
{{< /alert >}}

The following code snippet shows how to use the embedded license:

{{< tabs "example4">}}
{{< tab "C#" >}}
```csharp
GroupDocs.Viewer.License licenseViewer = new GroupDocs.Viewer.License();
licenseViewer.SetLicense("GroupDocs.Total.lic");

GroupDocs.Conversion.License licenseConversion = new GroupDocs.Conversion.License();
licenseConversion.SetLicense("GroupDocs.Total.lic");
```
{{< /tab >}}
{{< /tabs >}}

### Changing the License File Name

You do not have to name the license file "GroupDocs.Total.lic". Feel free to rename it as you prefer, and use that name when setting the license in your application.

### "Cannot find license filename" Exception

When you buy and download a license from the GroupDocs website, the license file is named "GroupDocs.Total.lic." Download it using your browser. Sometimes, browsers recognize it as XML and add the .xml extension, making the full file name "GroupDocs.Total.lic.XML" on your computer.

If Microsoft Windows is set to hide file extensions (which is the default in most installations), the license file will show as "GroupDocs.Total.lic" in Windows Explorer. You might assume this is the actual file name and call the `SetLicense` method with "GroupDocs.Total.lic", but there is no such file, leading to an exception.

To fix this issue, rename the file to remove the hidden .xml extension. Additionally, we suggest disabling the **Hide extensions** option in Microsoft Windows.

## How to Evaluate GroupDocs.Total

You can also try GroupDocs.Total without buying a license.

### Free Trial

The evaluation version is identical to the purchased one; it becomes licensed once you set the license. You can set the license using methods described in the following sections of this article.

The evaluation version has the following limitations:

- Rendering is limited to the first 2 pages.
- Trial badges are added to the top of a rendered page.

### Temporary License

If you want to test GroupDocs.Total without the limitations of the trial version,   request a 30-day Temporary License. For details, see the ["Get a Temporary License"](https://purchase.groupdocs.com/temporary-license) page.
