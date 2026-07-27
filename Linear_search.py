def linear_search(sequence: list, target: any) -> int:
    """
    Performs a linear search on a list to find the target item.
    Returns the index of the first occurrence, or -1 if not found.
    """
    for index, item in enumerate(sequence):
        if item == target:
            return index  
    return -1  

if __name__ == "__main__":
    numbers = [10, 50, 30, 70, 80, 20, 90, 40]
    target_value = 30
    
    result = linear_search(numbers, target_value)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the list.")
