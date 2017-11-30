
# *Restart and Run All* All Damn Day

Healthy doses of _**Restart and Run All**_ while developing in Jupyter notebooks 
will lead to more reusable code.  

# Types of Notebooks

Readable, reusable, reproducible

## Static Notebook

The static nbformat enables. 

## Interactive Notebook

While developing in notebooks, the author will flow through different styles of programming.  


### Non-Structured Programming

Exploratory programming

### Structured Programming

Structured programming create persistant code objects.

### Literate Programming

Code about the code.

## Procedural Notebook

In a procedural notebook, source code is executed linearly from beginning to end.  A procedural notebook will use combine a kernel language and macros/magics to executed source code from beginning to end.  Generally, a procedural notebook will be ordered and execute linearly.

Procudural notebooks will often use magic or macro operations to perform operations like convert nbformats, run tests, or create documentation.  To reuse magic functions in other contexts the following statement __must__ exist.


```python
    from IPython import get_ipython
```


    from IPython import get_ipython


In most jupyter applications, nothing is known about the __file__ object used by python.  


```python
    if '__file__' not in globals():
            !jupyter nbconvert --to markdown readme.ipynb
            !jupyter nbconvert --to python readme.ipynb
            !autopep8 --in-place --aggressive readme.py
            !ipython readme.py develop
```


    if '__file__' not in globals():
            !jupyter nbconvert --to markdown readme.ipynb
            !jupyter nbconvert --to python readme.ipynb
            !autopep8 --in-place --aggressive readme.py
            !ipython readme.py develop


    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 3188 bytes to readme.md
    [NbConvertApp] Converting notebook readme.ipynb to python
    [NbConvertApp] Writing 1940 bytes to readme.py
    ]0;IPython: tonyfast/restart[0;36m  File [0;32m"/Users/tonyfast/restart/readme.py"[0;36m, line [0;32m52[0m
    [0;31m    In most jupyter applications, nothing is known about the __file__ object used by python.[0m
    [0m          ^[0m
    [0;31mSyntaxError[0m[0;31m:[0m invalid syntax
    



```python
    if '__file__' in globals():
        %mkdir restarter
        %touch restarter/__init__.py
        __import__('setuptools').setup(
            name="restarter", py_modules=['restarter'], install_requires=[])
```


    if __name__ == '__main__' and '__file__' in globals():
            %mkdir restarter
            %touch restarter/__init__.py
            __import__('setuptools').setup(
                name="restarter", py_modules=['restarter'], install_requires=[])


### Interactive Mode
