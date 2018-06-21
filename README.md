Sensitivity Analysis pipeline
=============================

Uses `SALib` Python library to run multivariate sensitivity analysis on a model
of choice.

Requirements
------------

- make
- Python 3
- SALib Python library
- GNU Parallel

Usage
-----

This pipeline automates the following steps:

1. create experiment file (`params.txt`)
2. sample parameter space, generate model inputs (`inputs.txt`)
3. calculate outputs, run model on the inputs using GNU Parallel (`outputs.txt`)
4. analyze model outputs, calculate Sobol indices (`inds.txt`)

        .
        ├── cmd
        │  └── ishigami.py
        ├── dat
        │  ├── inds.txt
        │  ├── inputs.txt
        │  ├── outputs.txt
        │  └── params.txt
        └── Makefile

It is entirely make-driven (see `Makefile`); model can be swapped for any
Parallel-compatible programme by simply changing `F` command.

Help
----

See https://github.com/SALib/SALib/blob/master/README-advanced.md for more
advanced options.
