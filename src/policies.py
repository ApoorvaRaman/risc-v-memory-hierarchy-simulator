"""
Replacement policy implementations.
"""

from abc import ABC, abstractmethod
from collections import deque
from typing import Deque, List


class ReplacementPolicy(ABC):
    """Abstract base class."""

    @abstractmethod
    def on_hit(self, index: int) -> None:
        pass

    @abstractmethod
    def on_miss(self, num_lines: int) -> int:
        pass


class LRUReplacement(ReplacementPolicy):
    """Least Recently Used policy."""

    def __init__(self, assoc: int) -> None:
        self.order: List[int] = list(range(assoc))

    def on_hit(self, index: int) -> None:
        self.order.remove(index)
        self.order.append(index)

    def on_miss(self, num_lines: int) -> int:
        victim = self.order.pop(0)
        self.order.append(victim)
        return victim


class FIFOReplacement(ReplacementPolicy):
    """First-In First-Out policy."""

    def __init__(self, assoc: int) -> None:
        self.queue: Deque[int] = deque(range(assoc))

    def on_hit(self, index: int) -> None:
        # FIFO does nothing on hit
        pass

    def on_miss(self, num_lines: int) -> int:
        victim = self.queue.popleft()
        self.queue.append(victim)
        return victim
