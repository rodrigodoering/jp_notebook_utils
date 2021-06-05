# -*- coding: utf-8 -*-
"""
Created on Wed May 12 19:56:10 2021

@author: rodri
"""
import numpy as np


def to_numpy(array: NumericArray) -> np.ndarray:
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
    Argumentos:
    ----------
    array: numpy.array contendo os vetores que será convertido em string
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



def number_to_string(array):
    '''
    Argumentos:
    ----------
    array: numpy.array contendo os vetores que será convertido em string
    '''      
    rounded = (round(x,4) for x in array)
    if array.dtype == np.float64:
        # retorna as duas primeiras casas decimais se forem valores decimais
        return ('%.2f' % val if str(val)[-2:] != '.0' else '%d' % val for val in rounded)
    else:
        return map(str, rounded)



def flat_grid(grid):
    flatten = [coords.ravel() for coords in grid]
    return np.array(flatten).T

