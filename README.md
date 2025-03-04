# PandaModelsBackend
Provides a high fidelity backend for grid2op that uses PowerModels.jl. It achieves this using pandapower interface that calls PandaModels using PyCall to call julia functions from python.

## Prerequisites
1. Julia
2. Julia Packages
    - PowerModels.jl
    - PandaModels.js
    - PyCall
3. Configuring PyCall for python

## Installation
```pip install pandamodelsbackend```

## 