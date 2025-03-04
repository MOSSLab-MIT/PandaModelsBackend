# Contributor Documentation

## Prerequisite environment setup

### Using python virtual environment

- Create a python virtual environment
```python3 -m venv venv```

    - If you don't have virtual env installed refer to this [link](https://www.geeksforgeeks.org/python-virtual-environment/)

    - To activate your environment:
    ```source venv/bin/activate```

- Julia Installation refer to [this](https://docs.julialang.org/en/v1/manual/installation/)]

    - set your path variable to find Julia 

    e.g., on MAC
    ```export PATH=/Applications/Julia-1.11.app/Contents/Resources/julia/bin:$PATH```

- Add PowerModels, PandaModels Packages in Julia


- Build PyCall in Julia

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
