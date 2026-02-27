"""
Cache data structures and logic.
"""

from typing import List
from .policies import ReplacementPolicy, LRUReplacement, FIFOReplacement


class CacheLine:
    """Represents a single cache line."""

    def __init__(self) -> None:
        self.valid: bool = False
        self.tag: int = -1


class CacheSet:
    """Represents a set in the cache."""

    def __init__(self, assoc: int, policy: ReplacementPolicy) -> None:
        self.lines: List[CacheLine] = [CacheLine() for _ in range(assoc)]
        self.policy = policy

    def access(self, tag: int) -> bool:
        """Access cache set. Returns True on hit."""
        # Hit check
        for idx, line in enumerate(self.lines):
            if line.valid and line.tag == tag:
                self.policy.on_hit(idx)
                return True

        # Miss — choose victim
        victim = self.policy.on_miss(len(self.lines))
        self.lines[victim].valid = True
        self.lines[victim].tag = tag
        return False


class Cache:
    """Top-level cache model."""

    def __init__(
        self,
        cache_size: int,
        block_size: int,
        associativity: int,
        replacement_policy: str,
    ) -> None:
        self.block_size = block_size
        self.assoc = associativity

        num_blocks = cache_size // block_size
        self.num_sets = num_blocks // associativity

        if self.num_sets <= 0:
            raise ValueError("Invalid cache configuration.")

        self.sets: List[CacheSet] = []

        for _ in range(self.num_sets):
            if replacement_policy == "LRU":
                policy = LRUReplacement(associativity)
            else:
                policy = FIFOReplacement(associativity)

            self.sets.append(CacheSet(associativity, policy))

    def access(self, address: int) -> bool:
        """Access cache with given address."""
        block_addr = address // self.block_size
        set_index = block_addr % self.num_sets
        tag = block_addr // self.num_sets
        return self.sets[set_index].access(tag)
