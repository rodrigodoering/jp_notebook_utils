# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:03:02 2021

@author: rodrigo doering neves
@email: rodrigodoeringneves@gmail.com
"""

import pandas as pd
import numpy as np
import functools
from collections.abc import Iterable

import matplotlib.pyplot as plt
from matplotlib.axes import _subplots

from Visuals._utils_._exceptions import *
from Visuals._utils_._type_definitions import *
from Visuals._base_._graph_base import GraphBase
from Visuals._base_._axes_base import AxesInstance
import Visuals._utils_._functions as utils

        
class Plot(GraphBase):
    
    """ Representa o gráfico, herda de graph_base """
       

    def __init__(self, current_Axes: _subplots.Axes=None, current_plt: AxesInstance=None, **kwargs) -> NoReturn:
        # Inicia os parâmetros 
        if current_Axes is not None or current_plt is not None:
            self.new_plot(
                n_axis=None, 
                current_Axes = current_Axes,
                current_plt = current_plt,
                **kwargs
            )
        # Inicia GraphBase e o atributo axObj como NoneType
        super(Plot, self).__init__()


    def Annotate(
            self, 
            coords: NumericArray, 
            annotations: Iterable[str], 
            offset: float = 0.1, 
            ax_offset: int = 0, 
            **kwargs
            
        ) -> NoReturn:
        """
        Description:
        -----------
                Function to annotate plots with a list of coordinates and respective strings 
                Call _subplots.Axes.text method to draw annotations
        
        Arguments:
        ---------
                coords - Coordinates (x,y,z) 
                annotations - iterable with strings to annotate
                offset - displace annotations based on offset value
                ax_offset - offset axis for reference
                **kwargs - key arguments for _subplots.Axes.text
        
        """        
        coords = utils.to_numpy(coords)
        
        if type(annotations) is str:
            annotations = [annotations]
        
        # Se um axis inexistente for passado, zera o offset
        if ax_offset > self.axObj.n_axis:
            print('AxesInstance: ax_offset não existe no plot, desconsiderando offset')
            offset = 0
            
        # deve ser passada uma coordenada para cada anotação
        for vec, _str_ in zip(coords, annotations):
            coord_vals = (vec[i] + offset * int(i == ax_offset) for i in range(self.axObj.n_axis))
            self.axObj.ax_text(*coord_vals, text=_str_, **kwargs)  
    
    
    
    def Function(
            self, 
            function: Callable, 
            X: Union[NumericArray, tuple] = None,
            n_samples: int = 10,
            plot_intercept: bool = False,
            label: str = None,           
            **kwargs
            
        ) -> NoReturn:
        """
        Description:
        -----------
                Draw functions in 2D and 3D with _subplots.Axes.plot method
        
        Arguments:
        ---------
                function - Callable that return a numeric array
                X - domain, function input. X must be equal to [x] for 2D plots or X = [x,y] for 3D plots
                n_samples - if input was generated automatically, define how many input samples
                plot_intercept - Plot function intercept [0, function(0)] in 2D or [0, 0, function(0,0)] in 3D
                label - Function name, supports LaTex expressions
                **kwargs - key arguments for _subplots.Axes.plot
        
        """        
        n_features = self.axObj.n_axis - 1
        
        if X is None:
            # Se X não for passado, o domínio da função será composto por uma variável sintética
            # Por padrão a variável é criada com um range de 0 à 1
            X = np.array(
                [np.linspace(0,1,n_samples) for i in range(n_features)]
                ).reshape(n_samples, n_features)
    
        if isinstance(X, tuple):
            # Se o domínio passado for uma tupla, utiliza os valores para a variável base
            # Cria uma variável X sintética
            _min_ = X[0]
            _max_ = X[1]
            X = np.array(
                [np.linspace(_min_, _max_, n_samples) for i in range(n_features)]
                ).reshape(n_samples, n_features)           
        
        # Aplica a função e computa Y
        Y = function(X)
        
        if label is not None:
            self.axObj.ax_plot(*self.iter_params(X, Y), label=label, **kwargs)
            self.enable_legend()
        else:
            self.axObj.ax_plot(*self.iter_params(X, Y), **kwargs)
        
        if plot_intercept:
            zero_vec = np.zeros(n_features)
            intercept = function(zero_vec)
            p0 = (0 if i + 1 < self.axObj.n_axis else intercept[0] for i in range(self.axObj.n_axis))
            self.axObj.ax_scatter(*p0, color='black', marker='X')
        
        

    def Scatter(
            self,
            X: NumericArray, 
            Y: NumericArray = None, 
            Z: NumericArray = None,
            annot: Iterable[str] = None,
            offset: float = 0.1,
            ax_offset: int = 0,
            fontsize: int = 12,
            annot_color: str = 'black',
            **kwargs
            
        ) -> NoReturn:
        """
        Description:
        -----------
                Draw 2D and 3D scatter plots with _subplots.Axes.scatter method
                Supports flexible inputs as long as inputs are cohorent with number of axis existent
                and required number of inputs
        
        Arguments:
        ---------
                [X,Y,Z] - Numeric array of coordinates
                annot - iterable with strings to annotate
                offset - displace annotations based on offset value
                ax_offset - offset axis for reference
                fontsize - fontsize of annotations
                annot_color - color of annotations
                **kwargs - devem ser passados para  _subplots.Axes.scatter
        
        """ 
        self.axObj.ax_scatter(*self.iter_params(X, Y, Z), **kwargs)

        if annot is not None:
            coords = np.stack([*self.iter_params(X,Y,Z)], axis=1)

            self.Annotate(
                coords = coords, 
                annotations = annot, 
                offset = offset, 
                ax_offset = ax_offset, 
                fontsize = fontsize,
                color = annot_color
            )

        
    def Surface(
            self,
            grid: NumericArray = None,
            function: Callable = None,
            min_val: Numeric = -1,
            max_val: Numeric = 1,
            n_samples: int = 5,
            levels: int = None,
            **kwargs
            
        ) -> NoReturn:
        """
        Description:
        -----------
            Draw 2D and 3D surfaces based on a meshgrid of values. It is also flexible with inputs
            It's possible to either pass a full grid of values to draw the surface, or pass a callable function
            to compute the last dimension of a self generated meshgrid. If both parameters are skiped, it will
            throw an error since ther is no sufficient input to derive a surface.
            
            It's important to mention that changes between 2D and 3D plots is the underlying matplotlib function we call,
            specially because in both cases the function will perform precisely the same behaviour on creating a meshgrid.
            Any function passed will comput Z = f(X,Y) and the (X,Y,Z) grid will be created. What happens with the Z value
            is dependent on the number of axis: 
                
                - if the plot is bidimensional, surface will be displayed with _subplots.Axes.contourf method, where Z works
                  as a topographic colormapping and (X,Y) represent latitudinal and longitudinal coords.
                - if the plot is tridimensional, we use _subplots.Axes.surface method, and Z will be interpreted as altitude
                
                               
        Arguments:
        ---------
            grid - meshgrid with numeric values for plotting the surface
            function - callable to define the last dimension of a surface Z = f(X,Y). 
            min_val - min value for generating meshgrid
            max_val - max value for generating meshgrid
            n_samples - number of samples in base variable to generate 
            **kwargs - devem ser passados para  _subplots.Axes.surface or _subplots.Axes.contourf 
        
        """
        if grid is None:
            
            if callable(function):
                base_variable = np.linspace(min_val, max_val, n_samples)
                
                grid = np.broadcast_arrays(
                    base_variable[np.newaxis,:], 
                    base_variable[:,np.newaxis]
                )

                Z = utils.to_numpy(
                    function(
                        utils.numpy_convert(grid, check=True, flat=True)
                    )
                )
                
                grid.append(Z.reshape(n_samples, n_samples))                
                          
            else:
                raise Error('InsufficientInput')
        
        if self.axObj.n_axis == 2:
            self.axObj.ax_contourf(*grid, levels=levels, **kwargs)
            
        else:
            self.axObj.ax_surface(*grid, **kwargs)
            
            
            
    def Vectors(
            self,
            X: NumericArray, 
            Y: NumericArray = None, 
            Z: NumericArray = None,
            origin: tuple = None,
            color: Strings = None,
            annot: Iterable[str] = None,
            offset: float = 0.1,
            ax_offset: int = 0,
            fontsize: int = 12,
            annot_color: str = 'black',
            **kwargs
        
        ) -> NoReturn:
        """
        Description:
        -----------
                Draw 2D and 3D numeric vectors with _subplots.Axes.quiver method
                Supports flexible inputs as long as inputs are cohorent with number of axis existent
                and required number of inputs
        
        Arguments:
        ---------
                [X,Y,Z] - Numeric array of coordinates
                origin - numeric array with vector space origin values, must match number of axis
                color - color to plot the vectors
                annot - iterable with strings to annotate
                offset - displace annotations based on offset value
                ax_offset - offset axis for reference
                fontsize - fontsize of annotations
                annot_color - color of annotations
                **kwargs - key arguments to _subplots.Axes.quiver
        
        """         
        # Consolida os argumentos de input em uma única matriz
        vecs = np.array([*self.iter_params(X,Y,Z)]).T
        
        n_vecs = vecs.shape[0]
        print('\n')
        
        # Parâmetros interáveis precisam ser checados        
        if origin is not None:
            # ponto de origem deve ter a mesma dimensionalidade do plot
            # i.e mesmo número de componentes
            self.axObj.assert_sequence(origin, None)
        else:
            origin = tuple(0 for ax in range(self.axObj.n_axis))   
        
        if color is not None:
            if isinstance(color, str):
                color = [color for i in range(n_vecs)]
        else:
            color = ['black' for i in range(n_vecs)]
            
                        
        for vec, c in zip(vecs, color):
            print(vec, c)
            self.axObj.ax_quiver(
                *vec, 
                origin=origin, 
                color=c, 
                angles='xy',
                scale_units='xy',
                scale=1,
                **kwargs
            )

        if annot is not None:
            if type(annot) is str:
                annot = [annot]
                self.axObj.assert_sequence(annot, n_vecs)

            self.Annotate(
                coords = vecs + origin, 
                annotations = annot, 
                offset = offset, 
                ax_offset = ax_offset, 
                fontsize = fontsize,
                color = annot_color
            )
            

   
            
            
            
            
            
            
            
            
            
            
            
            
            
                  
