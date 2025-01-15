---
id: installation
url: total/net/installation
title: Install GroupDocs.Total for .NET
linkTitle: Installation
weight: 4
keywords: installation, NuGet package, NuGet package manager
description: "This topic describes how to install GroupDocs.Total for .NET."
productName: GroupDocs.Total for .NET
hideChildren: False
toc: True
---

This topic describes how to add the **GroupDocs.Total** library to your .NET project. You can use a NuGet package to install this library or you can download necessary DLLs from the GroupDocs website: [https://releases.groupdocs.com/total/net/](https://releases.groupdocs.com/total/net/).

### Select GroupDocs.Total package and version

<div class="gdoc-two-columns">
    <div class="gdoc-two-columns__column">
        <ul class="gdoc-two-columns__column__list">
            <li>
                <div>
                    <svg class="gdoc-two-columns__column__icon"><use xlink:href="/img/groupdocs-stack.svg#nuget"></use></svg>
                </div>
                <div>
                    <a class="gdoc-two-columns__column__link"
                        href="https://www.nuget.org/packages/GroupDocs.Total">GroupDocs.Total</a>
                    <div class="gdoc-two-columns__column__descr">
                        - .NET Standard 6.0 assembly.
                        <br>
                        - .NET Standard 2.0 in versions prior to 24.9.
                    </div>
                </div>
            </li>
        </ul>
    </div>
    <div class="gdoc-two-columns__column">
        <ul class="gdoc-two-columns__column__list">
            <li>
                <div>
                <svg class="gdoc-two-columns__column__icon"><use xlink:href="/img/groupdocs-stack.svg#nuget"></use></svg>
                </div>
                <div>
                    <a class="gdoc-two-columns__column__link"
                        href="https://www.nuget.org/packages/GroupDocs.Total.NETFramework">GroupDocs.Total.NETFramework</a>
                        <div class="gdoc-two-columns__column__descr">
                        - .NET Framework assembly.
                        <br>
                        - .NET Framework 4.6.2 and later.
                    </div>
                </div>
            </li>
        </ul>
    </div>
</div>

You can also use GroupDocs.Total with .NET Framework 2.0 (Visual Studio 2005-2008), .NET Framework 4.0 (Visual Studio 2010), and later .NET Framework versions by selecting one of the previous versions of the GroupDocs.Total package. See the complete list of package versions and supported frameworks in the table below.

{{< tabs "package-versions">}}
{{< tab "GroupDocs.Total" >}}

| Package version | Target frameworks |
| --- | --- |
| [24.12](https://www.nuget.org/packages/GroupDocs.Total/24.12) | .NET 6.0 |
| [24.11.1](https://www.nuget.org/packages/GroupDocs.Total/24.11.1) | .NET 6.0 |
| [24.11.0](https://www.nuget.org/packages/GroupDocs.Total/24.11.0) | .NET 6.0 |
| [24.10.0](https://www.nuget.org/packages/GroupDocs.Total/24.10.0) | .NET 6.0 |
| [24.9.1](https://www.nuget.org/packages/GroupDocs.Total/24.9.1) | .NET 6.0 |
| [24.8.0](https://www.nuget.org/packages/GroupDocs.Total/24.8.0) | .NET Standard 2.0 |
| [24.7.0](https://www.nuget.org/packages/GroupDocs.Total/24.7.0) | .NET Standard 2.0 |
| [24.6.0](https://www.nuget.org/packages/GroupDocs.Total/24.6.0) | .NET Framework 4.6.2, .NET Standard 2.0 |
| [24.5.0](https://www.nuget.org/packages/GroupDocs.Total/24.5.0) | .NET Framework 4.6.2, .NET Standard 2.0 |
| [24.4.0](https://www.nuget.org/packages/GroupDocs.Total/24.4.0) | .NET Framework 4.6.2, .NET Standard 2.0 |
| [24.3.0](https://www.nuget.org/packages/GroupDocs.Total/24.3.0) | .NET Framework 4.6.2, .NET Standard 2.0 |
| [24.2.0](https://www.nuget.org/packages/GroupDocs.Total/24.2.0) | .NET Framework 4.6.2, .NET Standard 2.0 |
| [24.1.0](https://www.nuget.org/packages/GroupDocs.Total/24.1.0) | .NET Framework 4.6.2, .NET Standard 2.0 |

<details>
<summary>See previous versions</summary>

| Package version | Target frameworks |
| --- | --- |
| [23.12.0](https://www.nuget.org/packages/GroupDocs.Total/23.12.0) | .NET Framework 4.6.2, .NET Standard 2.0 |
| [23.11.0](https://www.nuget.org/packages/GroupDocs.Total/23.11.0) | .NET Framework 4.6.2, .NET Standard 2.0 |
| [23.10.0](https://www.nuget.org/packages/GroupDocs.Total/23.10.0) | .NET Framework 4.6.2, .NET Standard 2.0 |
| [23.9.0](https://www.nuget.org/packages/GroupDocs.Total/23.9.0) | .NET Framework 4.6.1, .NET Standard 2.0 |
| [23.8.0](https://www.nuget.org/packages/GroupDocs.Total/23.8.0) | .NET Framework 4.6.1, .NET Standard 2.0 |
| [23.7.0](https://www.nuget.org/packages/GroupDocs.Total/23.7.0) | .NET Framework 4.6.1, .NET Standard 2.0 |
| [23.6.0](https://www.nuget.org/packages/GroupDocs.Total/23.6.0) | .NET Framework 4.6.1, .NET Standard 2.0 |
| [23.5.0](https://www.nuget.org/packages/GroupDocs.Total/23.5.0) | .NET Framework 4.6.1, .NET Standard 2.1 |
| [23.4.0](https://www.nuget.org/packages/GroupDocs.Total/23.4.0) | .NET Framework 4.6.1, .NET Standard 2.1 |
| [23.3.0](https://www.nuget.org/packages/GroupDocs.Total/23.3.0) | .NET Framework 4.6.1, .NET Standard 2.1 |
| [23.2.0](https://www.nuget.org/packages/GroupDocs.Total/23.2.0) | .NET Framework 4.6.1, .NET Standard 2.1 |
| [23.1.0](https://www.nuget.org/packages/GroupDocs.Total/23.1.0) | .NET Framework 4.6.1, .NET Standard 2.1 |
| [22.12.0](https://www.nuget.org/packages/GroupDocs.Total/22.12.0) | .NET Framework 4.6.1, .NET Standard 2.1 |
| [22.11.0](https://www.nuget.org/packages/GroupDocs.Total/22.11.0) | .NET Framework 4.5, .NET Standard 2.1 |
| [22.10.0](https://www.nuget.org/packages/GroupDocs.Total/22.10.0) | .NET Framework 4.5, .NET Standard 2.1 |
| [22.9.0](https://www.nuget.org/packages/GroupDocs.Total/22.9.0) | .NET Framework 4.5, .NET Standard 2.1 |
| [22.8.0](https://www.nuget.org/packages/GroupDocs.Total/22.8.0) | .NET Framework 4.5, .NET Standard 2.1 |
| [22.7.1](https://www.nuget.org/packages/GroupDocs.Total/22.7.1) | .NET Framework 4.5, .NET Standard 2.1 |
| [22.7.0](https://www.nuget.org/packages/GroupDocs.Total/22.7.0) | .NET Framework 4.5, .NET Standard 2.1 |
| [22.4.0](https://www.nuget.org/packages/GroupDocs.Total/22.4.0) | .NET Framework 3.5, .NET Standard 2.1 |
| [22.1.0](https://www.nuget.org/packages/GroupDocs.Total/22.1.0) | .NET Framework 2.0, .NET Standard 2.0 |
| [21.12.0](https://www.nuget.org/packages/GroupDocs.Total/21.12.0) | .NET Framework 2.0, .NET Standard 2.0 |
| [21.11.0](https://www.nuget.org/packages/GroupDocs.Total/21.11.0) | .NET Framework 2.0, .NET Standard 2.0 |
| [21.10.0](https://www.nuget.org/packages/GroupDocs.Total/21.10.0) | .NET Framework 2.0, .NET Standard 2.0 |
| [21.9.0](https://www.nuget.org/packages/GroupDocs.Total/21.9.0) | .NET Framework 2.0, .NET Standard 2.0 |
| [21.7.0](https://www.nuget.org/packages/GroupDocs.Total/21.7.0) | .NET Framework 2.0, .NET Standard 2.0 |
| [21.6.0](https://www.nuget.org/packages/GroupDocs.Total/21.6.0) | .NET Framework 2.0, .NET Standard 2.0 |
| [21.5.0](https://www.nuget.org/packages/GroupDocs.Total/21.5.0) | .NET Framework 2.0, .NET Standard 2.0 |
| [21.4.0](https://www.nuget.org/packages/GroupDocs.Total/21.4.0) | .NET Framework 2.0, .NET Standard 2.0 |
| [21.3.0](https://www.nuget.org/packages/GroupDocs.Total/21.3.0) | matapackage |
| [21.2.0](https://www.nuget.org/packages/GroupDocs.Total/21.2.0) | matapackage |
| [21.1.0](https://www.nuget.org/packages/GroupDocs.Total/21.1.0) | matapackage |
| [20.12.0](https://www.nuget.org/packages/GroupDocs.Total/20.12.0) | matapackage |
| [20.11.0](https://www.nuget.org/packages/GroupDocs.Total/20.11.0) | matapackage |
| [20.10.0](https://www.nuget.org/packages/GroupDocs.Total/20.10.0) | matapackage |
| [20.9.0](https://www.nuget.org/packages/GroupDocs.Total/20.9.0) | matapackage |
| [20.8.0](https://www.nuget.org/packages/GroupDocs.Total/20.8.0) | matapackage |
| [20.7.2](https://www.nuget.org/packages/GroupDocs.Total/20.7.2) | matapackage |
| [20.7.1](https://www.nuget.org/packages/GroupDocs.Total/20.7.1) | matapackage |
| [20.7.0](https://www.nuget.org/packages/GroupDocs.Total/20.7.0) | matapackage |
| [20.6.1](https://www.nuget.org/packages/GroupDocs.Total/20.6.1) | matapackage |
| [20.6.0](https://www.nuget.org/packages/GroupDocs.Total/20.6.0) | matapackage |
| [20.5.1](https://www.nuget.org/packages/GroupDocs.Total/20.5.1) | matapackage |
| [20.5.0](https://www.nuget.org/packages/GroupDocs.Total/20.5.0) | matapackage |
| [20.4.0](https://www.nuget.org/packages/GroupDocs.Total/20.4.0) | matapackage |
| [20.3.1](https://www.nuget.org/packages/GroupDocs.Total/20.3.1) | matapackage |
| [20.3.0](https://www.nuget.org/packages/GroupDocs.Total/20.3.0) | matapackage |
| [20.2.0](https://www.nuget.org/packages/GroupDocs.Total/20.2.0) | matapackage |
| [20.1.1](https://www.nuget.org/packages/GroupDocs.Total/20.1.1) | matapackage |
| [20.1.0](https://www.nuget.org/packages/GroupDocs.Total/20.1.0) | matapackage |
| [19.12.1](https://www.nuget.org/packages/GroupDocs.Total/19.12.1) | matapackage |
| [19.12.0](https://www.nuget.org/packages/GroupDocs.Total/19.12.0) | matapackage |

</details>

{{< /tab >}}
{{< tab "GroupDocs.Total.NETFramework" >}}

| Package version | Target frameworks |
| --- | --- |
| [24.12.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.12.0) | .NET Framework 4.6.2 |
| [24.11.1](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.11.1) | .NET Framework 4.6.2 |
| [24.11.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.11.0) | .NET Framework 4.6.2 |
| [24.10.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.10.0) | .NET Framework 4.6.2 |
| [24.9.1](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.9.1) | .NET Framework 4.6.2 |
| [24.8.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.8.0) | .NET Framework 4.6.2 |
| [24.7.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.7.0) | .NET Framework 4.6.2 |
| [24.6.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.6.0) | .NET Framework 4.6.1 |
| [24.5.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.5.0) | .NET Framework 4.6.1 |
| [24.4.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.4.0) | .NET Framework 4.6.1 |
| [24.3.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.3.0) | .NET Framework 4.6.1 |
| [24.2.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.2.0) | .NET Framework 4.6.1 |
| [24.1.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/24.1.0) | .NET Framework 4.6.1 |
| [23.12.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/23.12.0) | .NET Framework 4.6.1 |
| [23.11.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/23.11.0) | .NET Framework 4.6.1 |
| [23.10.0](https://www.nuget.org/packages/GroupDocs.Total.NETFramework/23.10.0) | .NET Framework 4.6.1 |

{{< /tab >}}
{{< /tabs >}}

{{< alert style="tip" >}}

.NET Framework versions are designed to be backward compatible. This means that you can use GroupDocs.Total for .NET targeting .NET Framework 2.0 with later versions of .NET Framework, such as .NET Framework 4.8. Learn more about .NET Framework backward compatibility [here](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/version-compatibility).

{{< /alert >}}

## Install GroupDocs.Total using NuGet packages

You can use the following tools to install the [GroupDocs.Total](https://www.nuget.org/packages/GroupDocs.Total) NuGet package: 

 * [NuGet Package Manager](#use-the-nuget-package-manager-in-visual-studio)
 * [Package Manager Console](#use-the-package-manager-console-in-visual-studio)
 * [.NET CLI](#use-the-net-cli)

### Use the NuGet Package Manager

Open your project or solution in Visual Studio and follow the steps below to install the **GroupDocs.Total** package using the [NuGet Package Manager](https://learn.microsoft.com/en-us/nuget/consume-packages/install-use-packages-visual-studio):

1. In **Solution Explorer**, right-click your project name and select **Manage NuGet Packages** to display the NuGet Package Manager.

    <!-- ![Manage NuGet packages in Visual Studio](/total/net/images/getting-started/installation/manage-nuget-packages.png) -->

2. Select the **Browse** tab and type **GroupDocs.Total** in the search box. Select the latest version of the **GroupDocs.Total** package and click **Install**.

    <!-- ![](/total/net/images/getting-started/installation/install-nuget-package.png) -->

### Use the Package Manager Console

The [Package Manager Console](https://learn.microsoft.com/en-us/nuget/consume-packages/install-use-packages-powershell) uses PowerShell commands to install, update, and remove NuGet packages. Open your project in Visual Studio and click **Tools** -> **NuGet Package Manager** -> **Package Manager Console** to open the console window. Run the the following command to install the latest version of the **GroupDocs.Total** library:

{{< tabs "example1">}}
{{< tab ".NET application" >}}
```
PM> Install-Package GroupDocs.Total
```
{{< /tab >}}
{{< tab ".NET Framework application" >}}
```
PM> Install-Package GroupDocs.Total.NETFramework
```
{{< /tab >}}
{{< /tabs >}}

<!-- ![Use Package Manager Console ](/total/net/images/getting-started/installation/package-manager-console.png) -->

### Use the .NET CLI

You can also use the [.NET CLI tool](https://docs.microsoft.com/en-us/dotnet/core/tools/) to install and update NuGet packages. Open a terminal in your project's folder and execute the following command to install the **GroupDocs.Total** package:

{{< tabs "example2">}}
{{< tab ".NET application" >}}
```
dotnet add package GroupDocs.Total
```
{{< /tab >}}
{{< tab ".NET Framework application" >}}
```
dotnet add package GroupDocs.Total.NETFramework
```
{{< /tab >}}
{{< /tabs >}}

## Download GroupDocs.Total from the official website

Visit [https://releases.groupdocs.com/total/net/](https://releases.groupdocs.com/total/net/) and download the **GroupDocs.Total** assemblies as a ZIP archive. To reference the downloaded assembly files in your project, do the following:

1. Extract files from the ZIP archive with the assemblies to a specific location on your computer.
2. Open your solution or project in Visual Studio.
3. In **Solution Explorer**, right-click the **References** or **Dependencies** node, and select **Add Reference** (for a .NET Framework project) or **Add Project Reference** (for a .NET Core project).
4. In the **Reference Manager** dialog box, select the **Browse** tab and click **Browse** to locate the _GroupDocs.Total.dll_ file for the target framework.
5. Click **OK** to add a reference to the **GroupDocs.Total** library to your project.

{{< alert style="warning" >}}
When installing GroupDocs.Total from the official website ensure that your project has all the required dependencies installed. Refer to the following page for details: 
* [GroupDocs.Total dependencies](https://www.nuget.org/packages/groupdocs.total#dependencies-body-tab)
* [GroupDocs.Total.NETFramework dependencies](https://www.nuget.org/packages/groupdocs.total.netframework#dependencies-body-tab).
{{< /alert >}}
