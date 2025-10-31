---
id: licensing-and-evaluation
url: total/python-net/licensing-and-evaluation
title: Licensing and Evaluation
weight: 6
keywords: free, free trial, evaluation, groupdocs.total
description: "GroupDocs.Total provides multiple licensing options, including a Free Trial and a 30-day Temporary License for evaluation."
productName: GroupDocs.Total for Python via .NET
hideChildren: False
toc: True
---

This guide explains the different licensing options available for GroupDocs.Total for Python via .NET and how to properly set up licensing in your applications.

## Overview

GroupDocs offers multiple licensing options to suit your needs:
- Free Trial (for evaluation)
- 30-day Temporary License
- Purchased License
- Metered License (pay-as-you-go)

{{< alert style="info" >}}
For detailed information about our licensing policies and frequently asked questions, please visit the [Purchase Policies and FAQ](https://purchase.groupdocs.com/policies/) section.
{{< /alert >}}

## Evaluation Options

### Free Trial

The evaluation version is identical to the purchased version and becomes fully licensed once a valid license is applied. However, it includes the following limitations:
- Evaluation watermark on output documents
- Page processing limits (vary by product)
- Other product-specific limitations

### Temporary License

For testing without trial limitations, you can request a 30-day Temporary License:
1. Visit the [Get a Temporary License](https://purchase.groupdocs.com/temporary-license/) page
2. Follow the on-screen instructions to request your temporary license
3. Apply the license using one of the methods described below

## License Application

### Important Notes

- Set the license only once per application
- Set the license before using any GroupDocs.Total code
- Multiple calls to `set_license` are safe but unnecessary
- Avoid multiple calls to `set_metered_key`, as this may interfere with accurate consumption tracking.

### License Application Methods

You can apply the license using a file path or a stream.

{{< alert style="info" >}}
The following code examples show how to set license for GroupDocs.Conversion API but the process it the same for all of the APIs included into GroupDocs.Total.
{{< /alert >}}

#### 1. From a File

The following code demonstrates setting a license from a file:

```python
import os
from groupdocs.conversion import License

def set_license_from_file():
    # Get absolute path to license file
    license_path = os.path.abspath("./GroupDocs.Total.lic")

    # Instantiate License and set the license
    license = License()
    license.set_license(license_path)

if __name__ == "__main__":
    set_license_from_file()
```

#### 2. From a Stream 

This example shows how to set a license from a stream:

```python
import os
from groupdocs.conversion import License

def set_license_from_stream():
    # Get absolute path to license file
    license_path = os.path.abspath("./GroupDocs.Total.lic")

    # Create a readable steam
    with open(license_path, "rb") as license_stream:
        # Instantiate and set the license
        license = License()
        license.set_license(license_stream)

if __name__ == "__main__":
    set_license_from_stream()
```

#### 3. Metered License

A [Metered License](https://reference.groupdocs.com/conversion/python-net/groupdocs.conversion/metered/) is also available as an alternative to a traditional license file. It is a usage-based licensing model that may be more suitable for customers who prefer to be billed based on actual API feature usage. For more information, refer to the [Metered Licensing FAQ](https://purchase.groupdocs.com/faqs/licensing/metered/).

The following sample demonstrates how to use metered licensing:

```python
from groupdocs.conversion import Metered

def set_metered_license():
    # Set your public and private keys
    public_key = "******" 
    private_key = "******" 

    # Instantiate Metered and set keys
    metered = Metered()
    metered.set_metered_key(public_key, private_key)

    # Get the number of MBs processed
    mb_processed = metered.get_consumption_quantity()
    print("MB processed: ", mb_processed)

    # Get the number of credits used
    credits_used = metered.get_consumption_credit()
    print("Credits used: ", credits_used)

if __name__ == "__main__":
    set_metered_license()
```

## Troubleshooting

### License File Naming
- You can rename the license file as needed
- Ensure the filename in your code matches the actual file name

### Common Issues

#### Can't find a license file

If you're setting a license file using a relative path and encountering issues, try using the absolute file path instead.