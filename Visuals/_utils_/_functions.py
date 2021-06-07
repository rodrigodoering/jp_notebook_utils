# -*- coding: utf-8 -*-
"""
Created on Wed May 12 19:56:10 2021

@author: rodri
"""
import numpy as np

from Visuals._utils_._type_definitions import *


def to_numpy(array: NumericArray) -> np.ndarray:
    """
    Avalia e converte se necessário um input numérico para um numpy.ndarray
    
    Argumentos:
    ----------
    array: array numérico que será testado

    Retorna: Input convertido para um numpy.ndarray
    -------    
    """
    if not isinstance(array, np.ndarray):

        if any(type(array) is _type_ for _type_ in (list, tuple)):
            array = np.array(array)

        elif isinstance(array, pd.DataFrame):
            array = array.values

        # Conforme bugs forem surgindo, atualizarei esse bloco de código
        # Para suportar novos tipos
        else:
            raise ValueError('Tipo de input não reconhecido')
    return array


def numpy_convert(
        array: NumericArray,
        check: bool = True,
        squeeze: bool = False, 
        expand: bool = False,
        flat: bool = False
        
    ) -> np.ndarray:
    '''
    Recebe um input numérico e avalia se este é uma instancia do numpy. Permite algumas manipulações com o input
    
    Argumentos:
    ----------
    array: array numérico que será testado
    check: se verdadeiro, avalia se o input é uma instancia de numpy.ndarray chamando to_numpy()
    squeeze: se verdadeiro, assume-se um input n-dimensional que deve ser reduzir a um array uni-dimensional
    expand: se verdadeiro, oposto à squeeze, incrementa o array para objetos dimensionais maiores
    flat: útil para matrizes numéricas multidimensionais como grids de valores, 
          retorna uma versão matricial com um vetor coordenada por linha
    
    Retorna: Input convertido para um numpy.ndarray
    -------
    
    '''     
    if check:
        ndarray = to_numpy(array)

    if squeeze and ndarray.ndim >= 2:
        ndarray = np.squeeze(ndarray)

    if expand and ndarray.ndim == 1:
        ndarray = np.expand_dims(ndarray, axis=0)

    if flat and ndarray.ndim >= 2:
            flatten = [feature.ravel() for feature in ndarray]
            ndarray = np.array(flatten).T

    return ndarray



def number_to_string(array: NumericArray) -> Iterable[str]:
    '''
    Transforma um array de valores numéricos nativos em strings que podém ser encaixadas em uma
    expressão de LaTex por exemplo, especialmente utilizada pelas funções do módulo Visuals.LaTex
    
    Argumentos:
    ----------
    array: array contendo os vetores que será convertido em string
    
    Retorna: Iterable de strings, no caso um generator por ser mais performático. No caso a função
    -------  retorna o objeto gerador inteiro ao invés de implementar uma função geradora com a chave "yield".
             **Essa decisão foi mais estética do que por qualquer outro motivo, embora isso possa ser alterado em um futuro próximo
    '''      
    rounded = (round(x,4) for x in array)
    if array.dtype == np.float64:
        # retorna as duas primeiras casas decimais se forem valores decimais
        return ('%.2f' % val if str(val)[-2:] != '.0' else '%d' % val for val in rounded)
    else:
        return map(str, rounded)



