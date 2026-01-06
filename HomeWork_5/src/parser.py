# ============================================================
# Parsing orders file
# ============================================================

from typing import List


def read_orders(file_name: str, separator: str) -> List[List[str]]:
    orders: List[List[str]] = []
    with open(file_name, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            products = [p.strip() for p in line.split(separator) if p.strip()]
            orders.append(products)

    return orders