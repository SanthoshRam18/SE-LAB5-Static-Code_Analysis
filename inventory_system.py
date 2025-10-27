"""
Inventory management system.
Demonstrates safe, secure, and PEP8-compliant inventory operations.
Uses logging, proper file handling, and input validation.
"""

import json
import logging
from datetime import datetime
from typing import Optional, Dict, List

# Configure module-level logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Global variable (simple in-memory store)
stock_data: Dict[str, int] = {}


def add_item(
    item: str = "default", qty: int = 0, logs: Optional[List[str]] = None
) -> None:
    """
    Add a given quantity of an item to the inventory.

    Args:
        item (str): Item name to add.
        qty (int): Quantity to add.
        logs (list, optional): List to record log entries.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str):
        logger.error("add_item: item must be a string, got %r", item)
        return

    if not isinstance(qty, int):
        logger.error("add_item: qty must be an integer, got %r", qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    entry = f"{datetime.now().isoformat()}: Added {qty} of {item}"
    logs.append(entry)
    logger.info(entry)


def remove_item(item: str, qty: int) -> None:
    """
    Remove a given quantity of an item from inventory.

    Args:
        item (str): Item name to remove.
        qty (int): Quantity to remove.
    """
    if not isinstance(item, str):
        logger.error("remove_item: item must be a string, got %r", item)
        return

    if not isinstance(qty, int):
        logger.error("remove_item: qty must be an integer, got %r", qty)
        return

    try:
        if item not in stock_data:
            logger.warning("remove_item: item %s not in stock", item)
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logger.info("Removed %d of %s", qty, item)
    except KeyError as err:
        logger.exception("remove_item: unexpected key error: %s", err)


def get_qty(item: str) -> int:
    """
    Retrieve the current quantity of an item.

    Args:
        item (str): Item name.
    Returns:
        int: Quantity in stock (0 if not found).
    """
    return stock_data.get(item, 0)


def load_data(file_path: str = "inventory.json") -> None:
    """
    Load inventory data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.
    """
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
        logger.info("Loaded data from %s", file_path)
    except FileNotFoundError:
        logger.warning(
            "load_data: %s not found. Starting with empty inventory.",
            file_path,
        )
        stock_data = {}
    except json.JSONDecodeError:
        logger.error(
            "load_data: invalid JSON in %s. Starting with empty inventory.",
            file_path,
        )
        stock_data = {}


def save_data(file_path: str = "inventory.json") -> None:
    """
    Save current inventory data to a JSON file.

    Args:
        file_path (str): Path to the JSON file.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=2)
        logger.info("Saved data to %s", file_path)
    except IOError as err:
        logger.exception(
            "save_data: failed to write to %s: %s", file_path, err
        )


def print_data() -> None:
    """Print a simple inventory report."""
    print("Items Report")
    for name, qty in stock_data.items():
        print(name, "->", qty)


def check_low_items(threshold: int = 5) -> list:
    """
    Return list of items whose quantity is below threshold.

    Args:
        threshold (int): Minimum acceptable quantity.
    Returns:
        list: Items with quantity lower than threshold.
    """
    result = []
    for name, qty in stock_data.items():
        if qty < threshold:
            result.append(name)
    return result


def main() -> None:
    """Demonstrate basic inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("banana", 3)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
