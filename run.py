#!/usr/bin/env python3
"""
Main CLI entry for RISC-V Memory Hierarchy Simulator.
"""

import argparse
import os
from src.simulator import CacheSimulator


def format_box(title: str, content: str) -> str:
    line = "=" * 60
    return f"\n{line}\n{title}\n{line}\n{content}\n{line}\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RISC-V Cache Memory Hierarchy Simulator"
    )

    parser.add_argument("--trace", required=True, help="Path to trace file")
    parser.add_argument("--cache_size", type=int, required=True, help="Cache size in bytes")
    parser.add_argument("--block_size", type=int, required=True, help="Block size in bytes")
    parser.add_argument("--assoc", type=int, required=True, help="Associativity")
    parser.add_argument("--policy", choices=["LRU", "FIFO"], required=True)
    parser.add_argument("--hit_time", type=float, required=True)
    parser.add_argument("--miss_penalty", type=float, required=True)

    args = parser.parse_args()

    if not os.path.exists(args.trace):
        raise FileNotFoundError(f"Trace file not found: {args.trace}")

    sim = CacheSimulator(
        trace_file=args.trace,
        cache_size=args.cache_size,
        block_size=args.block_size,
        associativity=args.assoc,
        replacement_policy=args.policy,
        hit_time=args.hit_time,
        miss_penalty=args.miss_penalty,
    )

    results = sim.run()

    output = (
        f"Total Accesses : {results['accesses']}\n"
        f"Cache Hits     : {results['hits']}\n"
        f"Cache Misses   : {results['misses']}\n"
        f"Hit Rate       : {results['hit_rate']:.4f}\n"
        f"Miss Rate      : {results['miss_rate']:.4f}\n"
        f"AMAT           : {results['amat']:.4f}"
    )

    print(format_box("SIMULATION RESULTS", output))


if __name__ == "__main__":
    main()
