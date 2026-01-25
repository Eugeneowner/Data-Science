# ============================================================
# Helper printing utilities
# ============================================================

from typing import List, Tuple


def print_summary(orders_count: int, unique_products: int, pairs_found: int, rules_found: int) -> None:
    print(f"Total orders: {orders_count}")
    print(f"Unique products: {unique_products}")
    print(f"Product pairs found: {pairs_found}")
    print(f"Association rules found: {rules_found}\n")


def print_rules(rules: List[Tuple[str, str, float, int]]) -> None:
    for i, (a, b, conf, supp) in enumerate(rules, start=1):
        print(
            f"p{i} {a} => {b} "
            f"({conf * 100:.2f}% confidence), {supp} support"
        )