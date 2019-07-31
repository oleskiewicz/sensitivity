#!/usr/bin/env python
import argparse

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from SALib.analyze import sobol
from SALib.util import read_param_file


def main(dir):
    fig, ax = plt.subplots()
    y = np.genfromtxt(f"{dir}/y.txt")
    p = read_param_file(f"{dir}/params.txt")
    si = sobol.analyze(p, y, conf_level=0.68)
    pd.DataFrame({"S1": si["S1"], "ST": si["ST"]}, index=p["names"]).plot.barh(
        ax=ax,
        xerr=pd.DataFrame({"S1": si["S1_conf"], "ST": si["ST_conf"]}, index=p["names"]),
    )


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
