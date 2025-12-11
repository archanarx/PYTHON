# Pet Store Inventory Program

# The program starts with an empty list inventory = [] to hold the names of pet supplies as strings, making it simple for beginners.
inventory = []


# Function to Add Items to Inventory
def add_item(item):
    inventory.append(item)


#  Recursive Function to Count Items
def count_items(items):
    # Base Case: list is empty
    if not items:
        return 0
    
    # Recursive Step: count current item + count rest
    return 1 + count_items(items[1:])


#  Lambda Function to Display Items
show_item = lambda item: print(f"Item in Stock: {item}")


#  Main Function
def main():
    # Add the four required items
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    print("\n--- Pet Store Inventory List ---")

    # Display each item using lambda
    for item in inventory:
        show_item(item)

    # Count total items using recursive function
    total = count_items(inventory)

    print("\nTotal Number of Items in Stock:", total)


# Run the Program
main()
