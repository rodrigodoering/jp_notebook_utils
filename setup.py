
import setuptools

def get_discription():
    with open("README.md", "r") as file:
        return file.read()

setuptools.setup(
     name='jp_notebook_utils',  
     version='1.0.1.2',
     author="Rodrigo Doering Neves",
     author_email="rodrigodoeringneves@gmail.com",
     description="Package containing utility modules for Jupyter Notebook presentations",
     long_description=get_discription(),
     long_description_content_type="text/markdown",
     url="https://github.com/rodrigodoering/jp_notebook_utils",
     packages=['Visuals', 'Visuals._base_', 'Visuals._utils_'],
     python_requires='>3.5.2',
     install_requires=[
         'matplotlib>=3.3.0',
         'numpy>=1.19.2',
         'pandas>=1.1.3'
     ],     
     classifiers=[
         "Programming Language :: Python :: 3 :: Only",
         "Topic :: Software Development :: Libraries :: Python Modules",
         "License :: OSI Approved :: MIT License",
         "Natural Language :: Portuguese (Brazilian)",
         "Development Status :: 3 - Alpha",
         "Intended Audience :: End Users/Desktop"
     ]
 )


