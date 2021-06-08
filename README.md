<p style='color:red'>Introdução sobre projeto.... preguiça de escrever agora</p>

## 1. Repository Structure

The package is structured in repository as follows:

    jp_notebook_visuals/
    |  LICENSE
    |  README.md   >>>you are here<<<
    |  Visuals/    
    |  |   __init__.py
    |  |   FastMatplot.py
    |  |   LaTex.py
    |  |  
    |  |   _base_/
    |  |  |   __init__.py
    |  |  |  _axes_base.py
    |  |  |  _graph_base.py
    |  |  
    |  |  _utils_/
    |  |  |   __init__.py
    |  |  |  _exceptions.py
    |  |  |  _type_definitions.py
    |  |  |  _functions.py
    
            

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

Although these requirements might stop installation in the middle if not fulfilled, they are not strictly mandatory for the package to work. During setup configuration and package development, code has been tested only in two specific python environments, so the requirerments are, at least for now, simply based on the least up to date environment where the modules were tested in first place. In general terms, what the package strictly requires for running is a python 3.5 environment since the modules make use of __type hinting__ which was only introduced to python by that version. Type hints allow a more readable code with better documentation which is exactly what we are looking for here. In special, its possible to study the existing user-defined types <a href='https://github.com/rodrigodoering/jp_notebook_visuals/blob/main/Visuals/_utils_/_type_definitions.py'>here</a>, making it easier to use the functions. 


## 3 Importing

Once....something 


<p style='color:red'>
PRECISO CONTINUAR AQUI DEPOIS, MAS SI PA NÃO VOU PRECISAR DESSA PARTE...
CÉLULA DE CÓDIGO ABAIXO É APENAS PARA CARREGAR O DIRETÓRIO LOCAL NO PC - NÃO ESQUECER DE
EXCLUIR NA VERSÃO FINAL

</p>


```python
import sys
sys.path.append('C:\\Users\\rodri\\github\\jp_notebook_visuals_git')
```

<p style='color:red'>Seguindo...</p>

## 4 LaTex Module

LaTex module contains functions for displaying LaTex language expressions in a nice fashion in jupyter notebook presentations. Three main functions are declared within the module:

- display_expression
- display_vec
- display_matrix

`display_expression` function is the principal one, responsible for actually displaying latex code in stdout. The other two, `display_vec` and `display_matrix` are adaptations for structuring specific latex code for displaying matrices and vectors, but internally use `display_expression` function as well.

For more information about latex expressions, a good option is __Overleaf__, where you can find a good and complete documentation about what LaTex is and how to use it (specially in the context of writing scientific papers that require mathematical formulations). The following <a href='https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes'>link</a> is a 30 minutes tutorial in Overleaf, where you can read more about it.

To import LaTex module we can run the following:


```python
from Visuals import LaTex
```

Other options to import the module with an alias:

    from Visuals import LaTex as lx
   
Or to import directly the existing functions:

    from Visuals.LaTex import display_expression
    from Visuals.LaTex import display_matrix
    from Visuals.LaTex import display_vec

Lets create a example latex expression using the famous __sigmoid function__ (a popular activation function used  by many algorithms in machine learning and statistical modelling fields):


```python
sigmoid = 'f(x) = \\frac{1}{1 + e^{-(x)}}'
```


```python
type(sigmoid)
```




    str



If we simply print this variable, it will appear as a simple string in stdout:

    print(sigmoid)
    >>> 'f(x) = \frac{1}{1 + e^{-(x)}}'
  
Now, by passing this same expression to __LaTex.display_expression__ function, it will properly display the latex equation:
    


```python
LaTex.display_expression(sigmoid)
```


<br>$\large  {f(x) = \frac{1}{1 + e^{-(x)}}}$<br>


There are a few customizable parameters the function supports, all related to LaTex native keywords: `size`, `style` and `font`. Please refer to the following documentations in Overleaf for more information about:

- <a href='https://www.overleaf.com/learn/latex/Font_sizes,_families,_and_styles'>font sizes</a>
- <a href='https://www.overleaf.com/learn/latex/Display_style_in_math_mode'>display styles</a>
- <a href='https://www.overleaf.com/learn/latex/Mathematical_fonts'>Math fonts</a>
    
The available options are stored as list variables inside the module `Visuals.LaTex`itself, and we can even access this variables if needed: 


```python
print('Available styles', LaTex.available_styles)
```

    Available styles [' ', ' \\displaystyle ', ' \\textstyle ', ' \\scriptstyle ', ' \\scriptscriptstyle ']
    

The parameters here are integers since they work as index for the desired value. Lets run an example with math fonts to see how the function select the desired preset and display the sigmoid function with different values for `font`parameter:


```python
# Interate over the first three available fonts
# For the example it's not necessary to use all available fonts
for i, font in enumerate(LaTex.available_fonts[:3]):
    
    # print selected index and respective font
    print('\nIndex %d, Font: %s' % (i, font))
    
    # display expression with selected font
    LaTex.display_expression(sigmoid, size=5, font=i)
    
```

    
    Index 0, Font: 
    


<br>$\Large  {f(x) = \frac{1}{1 + e^{-(x)}}}$<br>


    
    Index 1, Font: \mathcal
    


<br>$\Large  \mathcal{f(x) = \frac{1}{1 + e^{-(x)}}}$<br>


    
    Index 2, Font: \mathfrak
    


<br>$\Large  \mathfrak{f(x) = \frac{1}{1 + e^{-(x)}}}$<br>


Now, suppose we want to implement and run the sigmoid function, we can display the data easily with the other two functions in the module. First we create a vector with $x$ values as input for the sigmoid function:


```python
import numpy as np

X = np.linspace(0,1,5)
```

Now, we must define a simple sigmoid function to pass the $x$ input and compute $f(x)$ values


```python
def sigmoid(x):
    """ Implements sigmoid function """
    return 1 / (1 + np.e**(-x))

f_x = [sigmoid(x) for x in X]
```

Lets view the vector produced in LaTex display by calling `display_vec`function:


```python
LaTex.display_vec(f_x, label='f(x)', size=3)
```


<br>$\normalsize  {f(x) = \begin{bmatrix}0.50\\0.56\\0.62\\0.68\\0.73\end{bmatrix}}$<br>



<br>$\small  {\text{Vector space in }\mathbb{R}^5}$<br>


A few interesting things above:
- both `display_vec`and `display_matrix` functions supports a `label` parameter where you can name and identify the matrix or vector. It supports Latex display as well and we can even pass more elaborated LaTex expressions as labels for the visualization.

- we are passing once again the `size` parameter, only now this is a __kwarg__ argunment. As mentioned before, both `display_vec`and `display_matrix` functions are calling `display_expression`internally, thus allowing the user to personalize LaTex keywords by passing kwargs internally to `display_expression` call.

- In both functions, there is a boolean parameter `info` with default value of `True`. If true, it will display stylish information formated in LaTex as well about the vector or matrix dimensions. 

To test the other function, `display_matrix`, lets simply stack both vectors and compose a 5x2 matrix called $S$:


```python
S = np.vstack((x,y)).T
LaTex.display_matrix(aug_matrix, label='S')
```


<br>$\large  {S = \begin{bmatrix}0&0.50\\0.25&0.56\\0.50&0.62\\0.75&0.68\\1&0.73\end{bmatrix}}$<br>



<br>$\small  {\text{Matrix of elements }a_{i,j} \in \mathbb{R}^{5 \times 2}}$<br>


One very import thing to always keep in mind is that displaying LaTex is __memory consuming__. Often in fields such as data science and machine learning engineering we will be presented to huge datasets with millions of rows or columns (or both depending on the application), and displaying those as latex might cause memory crashs and __very__ slow execution times. Turns out, you can define a limit value for rows or columns (or both) with `n_rows` and `n_cols` arguments prior to be shown. In case of matrices, you can use both parameters. As for vectors, since they are uni-dimensional, usa only `n_rows`. Bellow I run an example by creating a $100 \times 10$ matrix and display it:


```python
LaTex.display_matrix(np.random.rand(100,10), n_rows=10, n_cols=3)
```


<br>$\large  {\begin{bmatrix}0.62&0.42&0.49\\0.02&0.41&0.97\\0.00&0.38&0.28\\0.35&0.20&0.20\\0.04&0.38&0.50\\0.03&0.92&0.01\\0.48&0.85&0.88\\0.79&0.05&0.20\\0.11&0.78&0.86\\0.24&0.41&0.35\end{bmatrix}}$<br>



<br>$\small  {\text{Matrix of elements }a_{i,j} \in \mathbb{R}^{100 \times 10}}$<br>


So, there are $1000$ values stored in that matrix, but I decided to limit the visualization to only 30 values (10 rows with 3 columns each). However, observe that the information displayed at the bottom holds the original dimensions of the matrix. The operation of "cropping" the matrix happens after storing the matrix dimensions. Take note that in the current version of the module,  by default all the existing values __will be displayed__, there is __not__ a code block inside this functions evaluating the size of the input prior to displaying it eventhough the option of cropping is available for both functions. However, we do intend to create such behaviour inside the functions in future updates


