#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import statistics
import argparse


def summary(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    stdev = statistics.stdev(data)
    variance = statistics.variance(data)
    return {"Média":mean, "Mediana":median, "Moda":mode,
            "Desvio padrão":stdev, "Variância":variance}


def help():
    pass


def main():
    parser = argparse.ArgumentParser(description="Stats summary.")
    parser.add_argument("-i", "--input", dest="input")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--mean", action="store_true")
    parser.add_argument("--median", action="store_true")
    parser.add_argument("--mode", action="store_true")
    parser.add_argument("--stdev", action="store_true")
    parser.add_argument("--variance", action="store_true")
    args = parser.parse_args(sys.argv[1:])


if __name__ == '__main__':
    main()
