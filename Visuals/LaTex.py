# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:03:02 2021

@author: rodrigo doering neves
@email: rodrigodoeringneves@gmail.com
"""

# Importa módulos built-ins
import warnings

# Impede mensagens de aviso de serem exibidas no notebook
warnings.filterwarnings("ignore")

# Importa pacotes gerais da comunidade
import numpy as np
import pandas as pd

# Importa funções específicas
from IPython.display import display, Markdown

from Visuals._utils_._type_definitions import *
import Visuals._utils_._functions as utils


# Define argumentos personalisáveis do código LaTex
# O índice posicional de cada elemento será o argumento a ser passado nas funções

# Lista de tamanhos disponíveis
available_sizes = [
    '$\\tiny ',
    '$\\scriptsize ',
    '$\\small ',
    '$\\normalsize ',
    '$\\large ',
    '$\\Large ',
    '$\\LARGE ',
    '$\\huge ',
    '$\\Huge ',
]

# Lista de estilos disponíveis
available_styles = [
    ' ',
    ' \\displaystyle ',
    ' \\textstyle ', 
    ' \\scriptstyle ', 
    ' \\scriptscriptstyle '
]

# Lista de fontes disponíveis
available_fonts = [
    '',
    '\\mathcal',
    '\\mathfrak',
    '\\mathbb',
    '\\mathrm',
    '\\mathit',
    '\\mathbf',
    '\\mathsf',
    '\\mathtt',      
]


def display_expression(expr: str, size: int=4, style: int=0, font: int=0, spacing: int=1) -> NoReturn:
    '''
    Exibe no stdout uma expressão LaTex fazendo uso dos módulos Display e Markdown do módulo IPython
    **NOTA: A função NÃO avalia a sintaxe da expressão LaTex passada, isso deve ser garantido pelo usuário.
    Também permite algumas personalizações com os argumentos numéricos, onde o valor inteiro representa o índex
    da lista de opções disponíveis.
    
    Argumentos:
    ----------
            expr: expressão LaTex a ser exibida. 
            size: tamanho de fonte da expressão LaTex (opções definidas em "available_sizes")
            style: estilo de fonte da expressão (opções definidas em "available_styles")
            font: assim como size e style, serve para selecionar uma opção entre as existentes, no caso, tipo de fonte
            spacing: espaçamento para gerar a visualização da expressão latex. É feito pensando em células de jupyter
                     notebooks. O espaçamento se dá com a tag <br> de HTML, que refere-se a quebra de linha.
                     Supondo que spacing seja 3, cria-se duas tags de 3 quebras de linhas (<br><br><br>) antes e depois da expressão
            

    '''
    if type(expr) is not str:
        raise('Passe apenas strings')
    
    if size > len(available_sizes) - 1:
        print('**display_expression: Tamanho de fonte não disponível, setando tamanho default (4)')
        size = 4

    if style > len(available_styles) - 1:
        print('**display_expression: Estilo de sentença não disponível, setando estilo default (0)')
        style = 0
    
    if font > len(available_fonts) - 1:
        print('**display_expression: Fonte não disponível, sentado fonte default (0) ')
    
    expr = ''.join([available_fonts[font], '{', expr, '}']) 
    start = available_sizes[size] + available_styles[style]
    space = '<br>' * spacing
    final_expr = ''.join([space, start, expr, '$', space])
    display(Markdown(final_expr))



def display_vec(V: NumericArray, label: str=None, info: bool=True, **kwargs) -> NoReturn:
    '''
    Exibe no stdout um vetor através de linguagem latex de visualização
    
    Argumentos:
    ----------
            V - array contendo o vetor a ser exibido com Latex
            label - rótulo do vetor, também será exibido em Latex
            info - se verdadeira, exibe o espaço vetorial pertencente
            **kwargs - a serem passados para display_expression()
    '''
    V = utils.numpy_convert(V, check=True)
    
    if V.ndim > 1:
        V = V.reshape(-1)
        
    if label is not None:
        vector_name = label
        latex_code = '{} = '.format(label) + '\\begin{bmatrix}%s\\end{bmatrix}'
    else:
        vector_name = '{\\small \\text{vector space in }}'
        latex_code = '\\begin{bmatrix}%s\\end{bmatrix}'
        
    # cria a string latex final contendo os valores do vetor
    add = '\\\\'.join(utils.number_to_string(V))
    display_expression(latex_code % add, **kwargs)
    
    if info:
        display_expression('\\text{Vector space in }\mathbb{R}^%d' % len(V), size=2)



def display_matrix(M: NumericArray, n_rows: int=None, n_cols: int=None, label: str=None, info: bool=True, **kwargs) -> NoReturn:
    '''
    Exibe no Stdout a matriz numérica passada junto com demais argumentos
    
    Argumentos:
    ----------
            M - Pandas.DataFrame ou 2-D Numpy.array contendo vetor ou matriz a ser plotada com markdown
            n_rows - quantidade máxima de linhas a serem exibidas
            n_cols - quantidade máxima de colunas a serem exibidas
            label - nome/símbolo da matriz passada
            info - se verdadeira, exibe dimensões da matriz com LaTex
            **kwargs - a serem passados para display_expression()
    '''
    if isinstance(M, pd.DataFrame):
        M = M.values
    else:
        M = utils.numpy_convert(M, check=True)
    
    # dimensões da matriz
    dims_matriz = M.shape
    
    if n_rows:
        M = M[:n_rows]
        
    if n_cols:
        M = M[:, :n_cols]

    # Gera o código latex
    if label is not None:
        latex_code = '{} = '.format(label) + '\\begin{bmatrix}%s\\end{bmatrix}'
    else:
        latex_code = '\\begin{bmatrix}%s\\end{bmatrix}'
        
    # cria a string contendo os valores da matriz e exibe a matriz
    M_str = (utils.number_to_string(vec) for vec in M)
    add = '\\\\'.join('&'.join(vec) for vec in M_str)
    display_expression(latex_code % add,  **kwargs)
    
    if info:
        display_expression(
            '\\text{Matrix of elements }a_{i,j} \in \\mathbb{R}^{%d \\times %d}' %(dims_matriz[0], dims_matriz[1]),
            size=2
        )


