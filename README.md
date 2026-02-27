# RISC-V Memory Hierarchy Simulator

A production-quality, trace-driven cache simulator for analyzing RISC-V memory behavior.

---

## Overview

This project models cache performance for memory traces derived from RISC-V load/store patterns. It is designed for:

- Computer architecture coursework
- Research experiments
- Cache design exploration
- Performance analysis

The simulator is fully offline and CLI-driven.

---

## Features

### Cache Models

- Direct-mapped
- Set-associative (configurable)
- Fully associative

### Replacement Policies

- LRU
- FIFO

### Metrics

- Total accesses
- Hits / misses
- Hit rate / miss rate
- AMAT

### Graph Generation

- Hit rate vs cache size
- Miss rate vs block size
- Automatic PNG output

### Synthetic Trace Generator

Patterns:

- Sequential
- Stride
- Random
- Matrix-style

---

## Architecture
