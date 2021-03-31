# GF2ER
[License Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Demo
Please view the following: 

[Demo](https://github.com/trungvu08/GF2ER/blob/main/Global%20Flood%20Equity%20XR%20Demo.pdf)

Presentation Video: [YouTube Link]

Presentation Slides: [Slides](https://github.com/trungvu08/GF2ER/blob/main/CFC%20Presentation.pptx)

## The Architecture
Please view the following: [System Architecture](https://github.com/trungvu08/GF2ER/blob/main/CFC%20GFEXR_System%20Architecture.pdf)

## Global Flood Equity Extended Reality: Long Description
Beginning with Hurricane Katrina in 2005, the National Flood Insurance Program (NFIP) has struggled with financial insolvency. The Congressional Budget Office estimated that the NFIP is expected to lose an annual $1.4 billion for the foreseeable future. The growing frequency and mounting economic costs of larger flooding events in the time of heightened climate change, rapid urbanization, environmental degradation, and rising sea levels have only exacerbated this issue. Furthermore, flooding has disproportional impacts on human society. Population in socially, economically, and geographically vulnerable areas experience most of the flood burdens and minimum mitigation benefits. Within the historical context, through centuries of slavery exploitation, several decades of Jim Crow domination, thirty years of civil rights oppression, recent flood disasters displacement, and gentrification has defined the settlement pattern of New Orleans and the development of the American cities. Consequently, the wealthy majority residents have historically had rights to the high-lying areas, while the lower-income, primarily minority residents were delegated to settle in the low-lying areas with greater flood risk and less flood protection. At the international scale, the global south is disproportionately affected and is unequipped to mitigate the climate crisis, while the wealthier counties are producing most of the greenhouse gases. Our University Challenge is to address these environmental justice and equity issues by developing an interactive web portal that calculates the flood risk of individual property and its optimal flood mitigation from a GIS database of the pilot city of New Orleans, which is one of the most hazard-prone urban cities in the world. A leading-edge AR interface will innovatively communicate the needed information to helping professionals, officials, and residents make better-informed decisions for self-determination within an environmental justice and equity framework. The GIS database uses a geographically weighted regressions model to produce a local spatial model of the latent factors of structural racism by fitting a regression equation to every map layer (gray/green infrastructure, hazard and risk, socioeconomic vulnerability, etc.). The map overlay methodology is a visual tool to display complex spatial data patterns of flood risk and mitigation in a concise understandable manner. The AR medium combine with information visualization technique for emergency management will be able to simply present the interaction of the many different cost-benefit analyses. Ultimately, the web tool will enhance the city's resiliency and adaptability. By globally scaling the IBM open-source technology, we hope to confront the social and humanitarian issues in the global south and other regions of the world that are disproportionally affected by climate change. An understanding of these underlying causes of environmental injustice and inequity will help us tailor the XR human experience to effectively inform flood risk and mitigation to diverse social, economic, political, environmental, cultural, and geographical factors. Without these direct technique interventions, the unequal distribution of the flood risk burden and mitigation benefit will be most felt on the national scale by indigenous, brown, and black Americans and on the larger scale, will amplify these environmental injustices and equities in the global south.

## Prerequisites
In this section, you’ll be installing the prerequisites needed before you can bootstrap your project, such as Python 3.

 ·         **Installing Python 3**
 
There is a big chance that you already have Python 3 installed on your system. If you don’t, you can simply head to the official website https://www.python.org/downloads/  and download the binaries for your operating system.

Depending on your system, you may also be able to install Python 3 or upgrade it to the latest version if it’s already installed by using the official package manager.

If you have a problem installing Python 3 or want more information, you can check the Python 3 Installation & Setup Guide https://realpython.com/installing-python/, which provides different ways to install Python 3 on your system.

Finally, you can check if you have Python 3 installed by running the following command:

$ python3 --version

Python 3.8.5

·         **Installing Django**

Django is the most popular Python framework for building web apps. It’s free, open source and written in python. Django offers a big collection of modules which you can use in your own projects. It makes it easy for developers to quickly build prototypes by providing a plethora of built-in APIs and sub-frameworks such as GeoDjango.

The Django package is available from the Python Package Index (PyPI) https://pypi.org/ so, you can simply use pip to install it by running the following command in your terminal:

$ pip install django

Or         $ pip install django  --upgrade (if already installed)

**To run the website:**

Download the project (located in master branch)

In your terminal, CD and then run: Python manage.py runserver

	
The application will be hosted at **localhost:8000**
