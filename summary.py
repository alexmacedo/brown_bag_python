#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import statistics
import argparse


def summary(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    try:
        mode = statistics.mode(data)
    except statistics.StatisticsError as e:
        mode = str(e)
    stdev = statistics.stdev(data)
    variance = statistics.variance(data)
    return {"Média":mean, "Mediana":median, "Moda":mode,
            "Desvio padrão":stdev, "Variância":variance}


def main():
    parser = argparse.ArgumentParser(description="Stats summary.")
    parser.add_argument("infile", nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument("--mean", action="store_true")
    parser.add_argument("--median", action="store_true")
    args = parser.parse_args(sys.argv[1:])

    data = args.infile.read()
    data = [int(i) for i in data.split("\n")]
    stats = summary(data)

    if args.mean:
        print(stats["Média"])
    elif args.median:
        print(stats["Mediana"])
    else:
        for key, value in stats.items():
            print("{0}: {1}".format(key, value))


if __name__ == '__main__':
    main()
