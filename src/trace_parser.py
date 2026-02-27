"""
Trace parser for memory access traces.
"""

from typing import Generator, Tuple


def parse_trace(file_path: str) -> Generator[Tuple[str, int], None, None]:
    """
    Parse trace file safely.

    Yields:
        (op, address)
    """
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) != 2:
                continue

            op, addr_str = parts
            if op not in ("R", "W"):
                continue

            try:
                address = int(addr_str, 16)
            except ValueError:
                continue

            yield op, address
