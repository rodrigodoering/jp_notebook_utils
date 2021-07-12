# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:03:02 2021

@author: rodrigo doering neves
@email: rodrigodoeringneves@gmail.com
"""

import pandas as pd
import numpy as np
import seaborn as sb
import functools

import matplotlib.pyplot as plt
from matplotlib.axes import _subplots

from Visuals._base_._axes_base import AxesInstance
from Visuals._utils_._exceptions import *
from Visuals._utils_._type_definitions import *
import Visuals._utils_._functions as utils


class GraphBase:

    def __init__(self,):
        self.axObj = None
    
    def new_plot(
            self, 
            n_axis: int = None, 
            current_Axes: _subplots.Axes=None,
            current_plt: AxesInstance=None,
            labels: Iterable[str] = None, 
            fontsize: int = None, 
            lims: Tuples = None, 
            elev: int = None, 
            azim: int = None,
            grid: bool = False,
            title: str = None,
            **kwargs
        ) -> NoReturn:
        
        if current_Axes is not None:
            if not isinstance(current_Axes, _subplots.Axes):
                raise Error('InvalidAxesObject')    
            self.axObj = current_Axes
        
        elif current_plt is not None:
            if True:
                self.axObj = current_plt.axObj
            
        elif n_axis is None:
            # se não for passado, o padrão é um plot 2D
            self.axObj = AxesInstance(n_axis=2, **kwargs)
        else:
            self.axObj = AxesInstance(n_axis, **kwargs)
        
        if labels is not None:
            self.axObj.set_ax_labels(labels, fontsize)
            
        if lims is not None:
            self.axObj.set_ax_limits(lims)
        
        if self.axObj.n_axis == 3:
            self.axObj.set_ax_view(elev, azim)
        
        if title is not None:
            self.axObj.set_ax_title(title)
        
        if grid:
            self.axObj.ax.grid()            
            
        
    
    def enable_legend(self) -> NoReturn:
        self.axObj.ax.legend()
        

    def full_coordinates(self, X: NumpyArray) -> bool:
        # Se X é unidimensional, então não pode conter coordenadas de multiplos eixos
        if X.ndim == 1:
            return False
        
        # Se as condições acimas não foram satisfeitas, as dimensões de X serão testadas
        elif X.ndim == 2:
            # Assume-se também que X está orientado como samples x features
            n_samples, n_features = X.shape
            
            if n_features == self.axObj.n_axis:
                return True
            
            else:
               return False 
            
        # Para tensores (ndim > 2), mantem-se os inputs como foram passados
        # Possivelmente, essa lógica poderá ser revista mais a frente para suportar tensores
        else:
            return False
                

    def iter_params(
            self,
            X: NumericArray, 
            Y: NumericArray = None, 
            Z: NumericArray = None,
        ) -> Iterator[NumericArray]:
        
        # Se Y e Z não foram passados, avalia X
        if all(_input_ is None for _input_ in [Y,Z]):
            
            X = utils.to_numpy(X)
            
            if X.ndim == 1:
                X = utils.numpy_convert(X, expand=True)
            
            n_samples, n_features = X.shape
                
            if n_features == self.axObj.n_axis:
                for coord in X.T:
                    yield coord
            
            else:
                raise ValueError('Input Não reconhecido')    
                    
        elif self.axObj.n_axis == 2:
            for coord in (X, Y):
                yield coord
                
        elif self.axObj.n_axis == 3 and Z is None:
            raise Error('MissingZ')
            
        else:
            for coord in (X, Y, Z):
                yield coord                    
                    
        
        
        
        
        
        
        

