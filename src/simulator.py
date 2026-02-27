"""
Simulation engine.
"""

from typing import Dict
from .cache import Cache
from .trace_parser import parse_trace


class CacheSimulator:
    """Runs cache simulation."""

    def __init__(
        self,
        trace_file: str,
        cache_size: int,
        block_size: int,
        associativity: int,
        replacement_policy: str,
        hit_time: float,
        miss_penalty: float,
    ) -> None:
        self.trace_file = trace_file
        self.hit_time = hit_time
        self.miss_penalty = miss_penalty

        self.cache = Cache(
            cache_size,
            block_size,
            associativity,
            replacement_policy,
        )

        self.accesses = 0
        self.hits = 0
        self.misses = 0

    def run(self) -> Dict[str, float]:
        """Execute simulation."""
        for _, addr in parse_trace(self.trace_file):
            self.accesses += 1
            if self.cache.access(addr):
                self.hits += 1
            else:
                self.misses += 1

        hit_rate = self.hits / self.accesses if self.accesses else 0
        miss_rate = self.misses / self.accesses if self.accesses else 0
        amat = self.hit_time + (miss_rate * self.miss_penalty)

        return {
            "accesses": self.accesses,
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": hit_rate,
            "miss_rate": miss_rate,
            "amat": amat,
        }
