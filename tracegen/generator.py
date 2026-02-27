#!/usr/bin/env python3
"""
Synthetic trace generator.
"""

import argparse
import random


def gen_sequential(n: int):
    for i in range(n):
        yield f"R 0x{i*4:08x}"


def gen_stride(n: int, stride: int = 16):
    addr = 0
    for _ in range(n):
        yield f"R 0x{addr:08x}"
        addr += stride


def gen_random(n: int, max_addr: int = 1 << 20):
    for _ in range(n):
        yield f"R 0x{random.randint(0, max_addr):08x}"


def gen_matrix(n: int, dim: int = 32):
    for i in range(dim):
        for j in range(dim):
            addr = (i * dim + j) * 4
            yield f"R 0x{addr:08x}"


PATTERNS = {
    "sequential": gen_sequential,
    "stride": gen_stride,
    "random": gen_random,
    "matrix": gen_matrix,
}


def main():
    parser = argparse.ArgumentParser(description="Synthetic Trace Generator")
    parser.add_argument("--pattern", choices=PATTERNS.keys(), required=True)
    parser.add_argument("--size", type=int, required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    generator = PATTERNS[args.pattern](args.size)

    with open(args.output, "w") as f:
        for line in generator:
            f.write(line + "\n")

    print(f"Trace written to {args.output}")


if __name__ == "__main__":
    main()
