# ============================================================
# MAIN - entry point
# ============================================================

from config import (
    FILE_NAME, DOCUMENT_URL, SEPARATOR,
    MIN_SUPPORT, MIN_CONFIDENCE, TIMEOUT_SECONDS
)
from downloader import download_document
from parser import read_orders
from counters import count_products, count_product_pairs
from rules import build_association_rules
from utils import print_summary, print_rules


def main() -> None:
    download_document(FILE_NAME, DOCUMENT_URL, timeout=TIMEOUT_SECONDS)
    orders = read_orders(FILE_NAME, SEPARATOR)
    products = count_products(orders)
    pairs = count_product_pairs(orders)
    rules = build_association_rules(products, pairs, MIN_SUPPORT, MIN_CONFIDENCE)
    print_summary(len(orders), len(products), len(pairs), len(rules))
    print_rules(rules)


if __name__ == "__main__":
    main()