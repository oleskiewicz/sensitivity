#!/usr/local/bin/parallel --shebang-wrap /usr/bin/env python3
import sys
import math


def evaluate(x1, x2, x3):
    A = 7
    B = 0.1
    return math.sin(x1) + A * (math.sin(x2))**2 + B * x3**4 * math.sin(x1)


if __name__ == '__main__':
    xs = map(lambda x: float(x), sys.argv[-1].split())
    print(evaluate(*xs))
