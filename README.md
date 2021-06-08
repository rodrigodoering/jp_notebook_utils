## 1. Introduction

`jp_notebook_visuals` was developed as a custom utility package to facilitate displaying visuals in jupyter notebook presentations. It was primarly designed for internal usage, but from now on will be also uploaded at Python Pakage Index (PyPI) so that the source code can be installed and imported thru different environments and systems 

#### 1.1 Motivation

As a data scientist & data engineer, one of the most frequent tasks when dealing with data is to proper visualize it for data exploration and presentations. Python, being the most popular programming language for data analysis nowadays, has several open source libraries available for ploting charts and visuals in general, among them, `matplotlib` is by far the most cited one. However, eventhough the objects and modules within matplot.pyplot are pretty intuitive, it usually envolves a few repetitive code lines to generate even the simplest graph, specially considering you might want to generate more than one plot in a jupyter notebook for example. The main goal of the module created here is to encapsulate matplotlib in straightforward classes to generate most of the popular available plots with no more than 2 or 3 lines of code in a few seconds, maintaining the jupyter notebook presentation as clean as possible, without huge code cells of plotting related code, keeping only the important data science code explicit. The functions developed are flexible, support and handle different types of inputs and, for beginners in Python, it will most likely be easier to use than calling and applying Matplotlib modules directly. 

As a complementary module, a module was also included with functions to produce a nice display of mathematical equations and formulations using LaTex language and IPython built-in modules for display and markdown. 



## 2. Installation 

To install Visuals module, two main options are available

#### 2.1 via pip install

The simplest way is to install the package is achieved via PIP, the __package installer for python__ used to download packages from <a href='https://pypi.org/'>PyPI</a>, the Python Package Index. The package url in PyPI can be found <a href='https://pypi.org/project/jp-notebook-utils/'>here</a>

To install the package, simply open a terminal or kernel and run the following command:

`pip install jp_notebook_visuals` 

#### 2.2 via github

It is also possible to clone a public github repository or simply download zip file where the source code is located. In case you are reading this readme.md file from anywhere but github, Visuals package source code can be found in github <a href='https://github.com/rodrigodoering/jp_notebook_visuals'>here</a>


#### 2.3 Installation requirements

At the moment, as a pre-alpha stage code, jp_notebook_visuals package requires a strict set of public python libraries with a minimum obligatory version, which can be found at `setup.py` script: 

     python >= 3.5.2
     matplotlib >= 3.3.0
     numpy >= 1.19.2
     pandas >= 1.1.3

If any of the above requirements is not satisfied and jp_notebook_visuals package is installed via __pip__ ina  terminal, installation will be cancalled. It can however works perfectly if installation occurred via repository clone since it wont evaluate install requirements set in `setup.py`. 

__Important Note__:

Although these requirements might stop installation in the middle if not fulfilled, they are not strictly mandatory for the package to work. During setup configuration and package development, code has been tested only in two specific python environments, so the requirerments are, at least for now, simply based on the least up to date environment where the modules were tested in first place. In general terms, what the package strictly requires for running is a python 3.5 environment since the modules make use of __type hinting__ which was only introduced to python in that version. Type hints allow a more readable code with better documentation which is exactly what we are looking for here. In special, its possible to study the existing user-defined types <a href='https://github.com/rodrigodoering/jp_notebook_visuals/blob/main/Visuals/_utils_/_type_definitions.py'>here</a>, making it easier to use the functions. 


## 3 Importing

To undestand what you should import, it's easier to take a look at the structure within the repository before since the project envolves packages and sub-packages with different relations between modules. The source code is structured in the repository as follows:

    jp_notebook_visuals/
    |      LICENSE
    |      README.md      >>>you are here<<<
    |      Userguide.pdf  >>>you should also read<<<
    |      Visuals/    
    |      |       __init__.py
    |      |       FastMatplot.py
    |      |       LaTex.py
    |      |       
    |      |       _base_/
    |      |      |      __init__.py
    |      |      |      _axes_base.py
    |      |      |      _graph_base.py 
    |      |       
    |      |       _utils_/
    |      |      |      __init__.py
    |      |      |      _exceptions.py
    |      |      |      _type_definitions.py
    |      |      |      _functions.py


The package containing everything described above is the `Visuals` package. Its possible to import the package itself:

    import Visuals
    import Visuals as vs
    from Visuals import *  

The last one, `from Visuals import *` is not really recommended though, it would be importing a lot of unecessary modules and functions. In fact, it is preferable to import the standalone modules instead of the whole package. `LaTex.py` and `FastMatplot.py` modules contain the end user functions we should import from `Visuals` package after installing it. `Visuals.FastMatplot.py` define a `Plot` class that should be imported in order to create new plots:

    from Visuals import FastMatplot
    from Visuals import FastMatplot as fm
    from Visuals.FastMatplot import Plot

On the other hand, `Visuals.LaTex.py` is far more simple, containing simple plain functions to display LaTex expressions to complement notebook presentations with nice math expressions in LaTex. Should be imported as:

    from Visuals import LaTex
    from Visuals import LaTex as lx
    from Visuals.LaTex import display_expression
    from Visuals.LaTex import display_matrix
    from Visuals.LaTex import display_vec
    
Since there are only 3 main functions and a few list variables, for this module it's actually a good choice to full import:

    from Visuals.LaTex import *

Now, there are two specific folders inside `Visuals` package: `_base_` and `_utils_`. These are sub-packages of `Visuals` and have different applications within the package structure, but none of them are designed for the end user and should not be imported (eventhough you can). `Visuals._utils_` holds modules with utility functions and variables required throughout the package modules:

- Visuals._utils_.exceptions : class with expected error messages
- Visuals._utils_._type_definitions : all the user defined types for type hinting
- Visuals._utils_._functions : utility functions for other modules
            
As for the other sub-package, `Visuals._base_`, it holds parent classes to be used in a relashionship with `Visuals.FastMatplot.Plot` object. As briefly mentioned in introduction, the plotting functions are written as classes in object oriented programming (which is heavily supported in Python) in orther to encapsulate all the plotting/matplotlib related code. Despite only importing the `Plot`class is required, the base classes are running as well. A more visual way to describe the relation between the modules and classes within Visuals package is presented below:
<br><br>
<img src='/Imgs/plot_class_diagram.png' width='800px'>

