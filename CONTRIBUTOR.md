# Contributor Documentation

## Prerequisite environment setup

### Using python virtual environment

- Create a python virtual environment
```python3 -m venv venv```

    - If you don't have virtual env installed refer to this [link](https://www.geeksforgeeks.org/python-virtual-environment/)

    - To activate your environment:
    ```source venv/bin/activate```

    - Install grid2op, pandapower
    ```pip install grid2op pandapower```
    ```pip install julia```

- Julia Installation refer to [this](https://docs.julialang.org/en/v1/manual/installation/)]

    - set your path variable to find Julia e.g., on MAC
    ```export PATH=/Applications/Julia-1.11.app/Contents/Resources/julia/bin:$PATH```

    - Add PowerModels, PandaModels Packages in Julia
    Run Juila on command prompt. Access the package manager in julia by typing ]. Now install the packages: add Ipopt PowerModels.

    - Build PyCall: The library PyCall allows to use Python from inside julia. By default, PyCall uses the Conda.jl package to install a Miniconda distribution private to Julia. To use an already installed Python distribution (e.g. Anaconda), set the PYTHON environment variable inside the Julia prompt.

        Find path to your python in venv:
        ```which python```
        e.g., <your python path>  - <your venv folder>/bin/python

        On MacOS:
        ```ENV["PYTHON"]="/Users/%Username/opt/anaconda3/bin/python"```
    
     Access the package manager again in julia by typing ]. Now install the packages: ```add PyCall```. To pass the python environment variable, running build PyCall inside the julia package manager may be necessary.

### Using Conda
[TODO]

## Build
```
git clone https://github.com/gt-sse-center/PandaModelsBackend.git
cd PandaModelBackend.git
python3 -m build
pip install -e .
```

## Test
```
cd tests
python test_api_PandaModelBackend.py
```
