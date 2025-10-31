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

This guide explains the different licensing options available for GroupDocs.Total for .NET and how to properly set up licensing in your applications.

## Overview

GroupDocs.Total for .NET offers multiple licensing options to suit your needs:
- Free Trial for evaluation
- 30-day Temporary License
- Purchased License
- Metered License (pay-as-you-go)

{{< alert style="info" >}}
For detailed information about our licensing policies and frequently asked questions, please visit the [Purchase Policies and FAQ](https://purchase.groupdocs.com/policies/) section.
{{< /alert >}}

## Evaluation Options

### Free Trial

The evaluation version is identical to the purchased version and becomes fully licensed once you set the license. However, it includes the following limitations:
- Evaluation watermark on output documents
- Page processing limits (varies by product)
- Other product-specific limitations

### Temporary License

For testing without trial limitations, you can request a 30-day Temporary License:
1. Visit the [Get a Temporary License](https://purchase.groupdocs.com/temporary-license/) page
2. Follow the instructions to request your temporary license
3. Apply the license using one of the methods described below

## License Application

### Important Notes

- Set the license only once per application domain
- Set the license before using any GroupDocs.Total classes
- Multiple calls to `SetLicense` are safe but unnecessary
- Multiple calls to `SetMeteredKey` should be avoided to prevent improper consumption tracking

### License File Locations

You can apply licenses from various locations:
- Explicit file path
- Same folder as GroupDocs.Total.dll
- Same folder as the calling assembly
- Same folder as the entry assembly (.exe)
- As an embedded resource

### License Application Methods

#### 1. From a File

{{< tabs "example1">}}
{{< tab "C#" >}}

```csharp
string licensePath = "GroupDocs.Total.lic";

// Set license for all products
GroupDocs.Total.License.SetLicense(licensePath);

// Or set license for specific products
GroupDocs.Viewer.License licenseViewer = new GroupDocs.Viewer.License();
licenseViewer.SetLicense(licensePath);

GroupDocs.Conversion.License licenseConversion = new GroupDocs.Conversion.License();
licenseConversion.SetLicense(licensePath);
```

{{< /tab >}}
{{< /tabs >}}


#### 2. From a Stream

{{< tabs "example2">}}
{{< tab "C#" >}}

```csharp
string licensePath = "GroupDocs.Total.lic";
using (FileStream licenseStream = File.OpenRead(licensePath))
{
    // Set license for all products
    GroupDocs.Total.License.SetLicense(licenseStream);

    // Or set license for specific products
    GroupDocs.Viewer.License licenseViewer = new GroupDocs.Viewer.License();
    licenseViewer.SetLicense(licenseStream);

    GroupDocs.Conversion.License licenseConversion = new GroupDocs.Conversion.License();
    licenseConversion.SetLicense(licenseStream);
}
```

{{< /tab >}}
{{< /tabs >}}

#### 3. As an Embedded Resource

To use an embedded license:

1. Add the license file to your project
2. Set its **Build Action** property to "Embedded Resource"
3. Ensure the license name matches the parameter in `SetLicense`

{{< tabs "example3">}}
{{< tab "C#" >}}

```csharp
// Set license for all products
GroupDocs.Total.License.SetLicense("GroupDocs.Total.lic");

// Or set license for specific products
GroupDocs.Viewer.License licenseViewer = new GroupDocs.Viewer.License();
licenseViewer.SetLicense("GroupDocs.Total.lic");

GroupDocs.Conversion.License licenseConversion = new GroupDocs.Conversion.License();
licenseConversion.SetLicense("GroupDocs.Total.lic");
```

{{< /tab >}}
{{< /tabs >}}

#### 4. Metered License

For pay-as-you-go licensing, use the Metered License option. For more details, see the [Metered Licensing FAQ](https://purchase.groupdocs.com/faqs/licensing/metered/).

{{< tabs "example4">}}
{{< tab "C#" >}}


```csharp
string publicKey = ""; // Your public license key
string privateKey = ""; // Your private license key

// Set metered keys for GroupDocs.Viewer
GroupDocs.Viewer.Metered meteredViewer = new GroupDocs.Viewer.Metered();
meteredViewer.SetMeteredKey(publicKey, privateKey);

// Get consumption metrics
decimal amountConsumed = GroupDocs.Viewer.Metered.GetConsumptionQuantity();
decimal creditsConsumed = GroupDocs.Viewer.Metered.GetConsumptionCredit();

// Set metered keys for GroupDocs.Conversion
GroupDocs.Conversion.Metered meteredConversion = new GroupDocs.Conversion.Metered();
meteredConversion.SetMeteredKey(publicKey, privateKey);
```

{{< /tab >}}
{{< /tabs >}}


## Troubleshooting

### License File Naming
- You can rename the license file as needed
- Ensure the filename in your code matches the actual file name

### Common Issues

#### Can't find a license file

If you're setting a license file using a relative path and encountering issues, try using the absolute file path instead.