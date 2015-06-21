#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import random
from urllib.request import urlopen


def fibonacci(limit=100):
    """
    Fibonacci interativo usando yield
    """
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b
    return


def get_url(url):
    with urlopen(url) as response:
        data = response.read().decode("latin1")
    return data


def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


def generate_random_data(limit=100):
    numbers = random.sample(range(1, 10001), limit)
    return numbers


def main():
    print("Fibonacci:")
    for i in fibonacci(1000):
        print(i)

    content = get_url("https://www.google.com.br/")
    chars = {}
    for i in content:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 0

    print(json.dumps(chars, indent=4))

    random_data = generate_random_data()
    write_file("random.txt", "\n".join([str(i) for i in random_data]))


if __name__ == '__main__':
    main()
