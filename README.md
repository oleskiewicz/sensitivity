# Sensitivity Analysis pipeline

Uses `SALib` Python library to run multivariate sensitivity analysis on a model
of choice.

1. create experiment file
1. sample parameter space, generate model inputs
1. calculate outputs, run model on the inputs using GNU Parallel
1. analyze model outputs, calculate Sobol indices
