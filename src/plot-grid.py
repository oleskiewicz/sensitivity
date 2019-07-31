#!/usr/bin/env python
import argparse

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def _facet_scatter(x, y, c, **kwargs):
    kwargs.pop("color")
    plt.scatter(x, y, c=c, **kwargs)


def main(dir):
    X = pd.read_csv(f"{dir}/x.txt", header=None, sep=" ")
    y = np.genfromtxt(f"{dir}/y.txt")
    fig = sns.PairGrid(X).map_diag(plt.hist).map_offdiag(_facet_scatter, c=y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    main(args.dir)

    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()
