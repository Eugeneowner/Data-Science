# ============================================================
# Counters: products and pairs
# ============================================================

from itertools import combinations
from collections import Counter, defaultdict
from typing import List, Dict, Tuple


def count_products(orders: List[List[str]]) -> Counter:
    product_counter = Counter()
    for order in orders:
        product_counter.update(set(order))  
    return product_counter


def count_product_pairs(orders: List[List[str]]) -> Dict[Tuple[str, str], int]:
    pair_counter = defaultdict(int)
    for order in orders:
        unique_products = sorted(set(order))
        for pair in combinations(unique_products, 2):
            pair_counter[pair] += 1

    return dict(pair_counter)