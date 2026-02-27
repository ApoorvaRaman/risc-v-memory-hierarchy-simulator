#!/usr/bin/env python3
"""
Parameter sweep and graph generation.
"""

import argparse
import os
import matplotlib.pyplot as plt
from src.simulator import CacheSimulator


def ensure_results():
    os.makedirs("results", exist_ok=True)


def sweep_cache_sizes(trace, sizes, block_size, assoc, policy, hit, miss):
    hit_rates = []

    for size in sizes:
        sim = CacheSimulator(trace, size, block_size, assoc, policy, hit, miss)
        result = sim.run()
        hit_rates.append(result["hit_rate"])

    plt.figure()
    plt.plot(sizes, hit_rates, marker="o")
    plt.title("Hit Rate vs Cache Size")
    plt.xlabel("Cache Size (bytes)")
    plt.ylabel("Hit Rate")
    plt.grid(True)
    plt.savefig("results/hit_rate_vs_cache_size.png")
    print("Saved results/hit_rate_vs_cache_size.png")


def sweep_block_sizes(trace, cache_size, blocks, assoc, policy, hit, miss):
    miss_rates = []

    for blk in blocks:
        sim = CacheSimulator(trace, cache_size, blk, assoc, policy, hit, miss)
        result = sim.run()
        miss_rates.append(result["miss_rate"])

    plt.figure()
    plt.plot(blocks, miss_rates, marker="o")
    plt.title("Miss Rate vs Block Size")
    plt.xlabel("Block Size (bytes)")
    plt.ylabel("Miss Rate")
    plt.grid(True)
    plt.savefig("results/miss_rate_vs_block_size.png")
    print("Saved results/miss_rate_vs_block_size.png")


def main():
    parser = argparse.ArgumentParser(description="Cache parameter sweeps")
    parser.add_argument("--trace", required=True)
    args = parser.parse_args()

    ensure_results()

    sweep_cache_sizes(
        args.trace,
        sizes=[256, 512, 1024, 2048, 4096],
        block_size=16,
        assoc=1,
        policy="LRU",
        hit=1,
        miss=10,
    )

    sweep_block_sizes(
        args.trace,
        cache_size=1024,
        blocks=[8, 16, 32, 64],
        assoc=1,
        policy="LRU",
        hit=1,
        miss=10,
    )


if __name__ == "__main__":
    main()
