# ============================================================
# Association rules builder
# ============================================================

from collections import Counter
from typing import Dict, Tuple, List


def build_association_rules(
    products: Counter,
    pairs: Dict[Tuple[str, str], int],
    min_support: int,
    min_confidence: float
) -> List[Tuple[str, str, float, int]]:
    rules: List[Tuple[str, str, float, int]] = []

    for (x, y), support in pairs.items():
        if support < min_support:
            continue

        conf_x_y = support / products[x]
        conf_y_x = support / products[y]

        if conf_x_y >= min_confidence:
            rules.append((x, y, conf_x_y, support))

        if conf_y_x >= min_confidence:
            rules.append((y, x, conf_y_x, support))

    rules.sort(key=lambda r: (-r[3], -r[2]))
    return rules