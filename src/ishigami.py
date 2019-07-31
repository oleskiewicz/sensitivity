#!/usr/bin/env python
import math
import sys


def f(x1, x2, x3):
    A = 7.0
    B = 0.1
    return (
        math.sin(x1) + A * math.pow(math.sin(x2), 2.0) + B * pow(x3, 4.0) * math.sin(x1)
    )


if __name__ == "__main__":
    xs = list(map(lambda x: float(x), sys.argv[-1].split()))
    print(f(*xs))
