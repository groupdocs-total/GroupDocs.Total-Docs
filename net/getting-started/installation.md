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

## Install GroupDocs.Total using NuGet packages

You can use the following tools to install the [GroupDocs.Total](https://www.nuget.org/packages/GroupDocs.Total) NuGet package: 

 * [NuGet Package Manager](#use-the-nuget-package-manager-in-visual-studio)
 * [Package Manager Console](#use-the-package-manager-console-in-visual-studio)
 * [.NET CLI](#use-the-net-cli)

### Select package

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
                        - .NET Standard 2.0 assembly.
                        <br>
                        - .NET Core 3.1, NET 5 and later.
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

### Use the NuGet Package Manager

Open your project or solution in Visual Studio and follow the steps below to install the **GroupDocs.Total** package using the [NuGet Package Manager](https://learn.microsoft.com/en-us/nuget/consume-packages/install-use-packages-visual-studio):

1. In **Solution Explorer**, right-click your project name and select **Manage NuGet Packages** to display the NuGet Package Manager.

    <!-- ![Manage NuGet packages in Visual Studio](/total/net/images/getting-started/installation/manage-nuget-packages.png) -->

2. Select the **Browse** tab and type **GroupDocs.Total** in the search box. Select the latest version of the **GroupDocs.Total** package and click **Install**.

    <!-- ![](/total/net/images/getting-started/installation/install-nuget-package.png) -->

### Use the Package Manager Console

The [Package Manager Console](https://learn.microsoft.com/en-us/nuget/consume-packages/install-use-packages-powershell) uses PowerShell commands to install, update, and remove NuGet packages. Open your project in Visual Studio and click **Tools** -> **NuGet Package Manager** -> **Package Manager Console** to open the console window. Run the the following command to install the latest version of the **GroupDocs.Total** library:

{{< tabs "example1">}}
{{< tab "GroupDocs.Total" >}}
```
PM> Install-Package GroupDocs.Total
```
{{< /tab >}}
{{< tab "GroupDocs.Total.NETFramework" >}}
```
PM> Install-Package GroupDocs.Total.NETFramework
```
{{< /tab >}}
{{< /tabs >}}

<!-- ![Use Package Manager Console ](/total/net/images/getting-started/installation/package-manager-console.png) -->

### Use the .NET CLI

You can also use the [.NET CLI tool](https://docs.microsoft.com/en-us/dotnet/core/tools/) to install and update NuGet packages. Open a terminal in your project's folder and execute the following command to install the **GroupDocs.Total** package:

{{< tabs "example2">}}
{{< tab "GroupDocs.Total" >}}
```
dotnet add package GroupDocs.Total
```
{{< /tab >}}
{{< tab "GroupDocs.Total.NETFramework" >}}
```
dotnet add package GroupDocs.Total.NETFramework
```
{{< /tab >}}
{{< /tabs >}}

## Download GroupDocs.Total from the official website

Visit [https://releases.groupdocs.com/total/net/](https://releases.groupdocs.com/total/net/) and download the **GroupDocs.Total** assemblies as a ZIP archive or MSI installer. To reference the downloaded assembly files in your project, do the following:

1. Extract files from the ZIP archive or run the MSI installer to install **GroupDocs.Total** to a specific location on your computer.
2. Open your solution or project in Visual Studio.
3. In **Solution Explorer**, right-click the **References** or **Dependencies** node, and select **Add Reference** (for a .NET Framework project) or **Add Project Reference** (for a .NET Core project).
4. In the **Reference Manager** dialog box, select the **Browse** tab and click **Browse** to locate the _GroupDocs.Total.dll_ file for the target framework.

    <!-- ![Browse for the GroupDocs.Total assembly](/total/net/images/getting-started/installation/browse-for-groupdocs-dll.png) -->

5. Click **OK** to add a reference to the **GroupDocs.Total** library to your project.

{{< alert style="warning" >}}
If your application targets .NET Core / .NET 5+, ensure that your project has all the required dependencies installed. Refer to the following page for details: [GroupDocs.Total dependencies](https://www.nuget.org/packages/groupdocs.total#dependencies-body-tab).
{{< /alert >}}
