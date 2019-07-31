Sensitivity Analysis pipeline
=============================

Uses `SALib` Python library to run sensitivity analysis (SA) of models.


Requirements
------------

- make
- Python
- SALib Python library
- GNU Parallel


Usage
-----

	EXP=ishigami make sa fig

Will run experiment defined in exp/ishigami.mk, reading and writing data at
dat/ishigami, and saving figures in fig/ishigami.

The following structure is assumed:

	.
	├── dat/
	│   └── ishigami/
	│       ├── params.txt
	│       ├── si.txt
	│       ├── x.txt
	│       └── y.txt
	├── exp/
	│   └── ishigami.mk
	└── fig/
	    └── ishigami/
	        ├── grid.png
	        └── si.png

- .mk file contains experiment definition: random seed, sampling number, etc.
- params.txt contains SALib experiment parameter file, with variable ranges
- x.txt and y.txt contain model inputs and outputs
- si.txt is where sensitivity indices will be written to
- grid.png visualises all model inputs on a corner plot
- sa.png plots first and total order indices

The pipeline is declared in the Makefile, and multiple experiments can be ran by
simply swapping the exp/*.mk files.


Help
----

See https://github.com/SALib/SALib/blob/master/README-advanced.md for more
advanced options.
