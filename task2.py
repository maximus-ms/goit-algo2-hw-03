import csv
import timeit
from BTrees.OOBTree import OOBTree

def add_item_to_tree(tree, item):
    """Add an item to the OOBTree structure."""
    tree[float(item['Price'])] = {
    # tree[item['ID']] = {
        'ID': item['ID'],
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': float(item['Price'])
    }

def add_item_to_dict(dict_structure, item):
    """Add an item to the dictionary structure."""
    dict_structure[float(item['Price'])] = {
    # dict_structure[item['ID']] = {
        'ID': item['ID'],
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': float(item['Price'])
    }

def range_query_tree(tree, min_price, max_price):
    """Execute range query on OOBTree using items(min, max) method."""
    return {k: v for k, v in tree.items(min_price, max_price) if min_price <= v['Price'] <= max_price}

def range_query_dict(dict_structure, min_price, max_price):
    """Execute range query on dictionary using linear search."""
    return {k: v for k, v in dict_structure.items() if min_price <= v['Price'] <= max_price}

def main():
    # Initialize data structures
    tree = OOBTree()
    dict_structure = {}
    
    # Load data from CSV
    with open('generated_items_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            add_item_to_tree(tree, row)
            add_item_to_dict(dict_structure, row)
    
    # Define price range for queries
    min_price = 10.0
    max_price = 50.0
    
    # Measure time for OOBTree queries
    tree_time = timeit.timeit(
        lambda: range_query_tree(tree, min_price, max_price),
        number=100
    )
    
    # Measure time for dict queries
    dict_time = timeit.timeit(
        lambda: range_query_dict(dict_structure, min_price, max_price),
        number=100
    )
    
    # Print results
    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    main()
