# Grocery List
grocery_list = ["milk", "bread", "eggs"]

# Add Item Function, Write a function add_item(item) that adds a given item (string) to the grocery list.
def add_item(item):
    grocery_list.append(item)
    print(f"Added: {item}")

# Write a function remove_last_item() that removes the last item from the grocery list.
def remove_last_item():
    if grocery_list:  # check if list is not empty
        removed = grocery_list.pop()
        print(f"Removed: {removed}")
    else:
        print("The list is already empty!")

# Use a lambda function to print each item in the list with the format: "Item: <item>".
display_item = lambda item: print(f"Item: {item}")

# Write a recursive function count_characters(items) that returns the total number of characters in all item names combined. For example, ["milk", "bread"] has 4 + 5 = 9 characters..
def count_characters(items):
    # Base case: empty list
    if not items:
        return 0
    
    # Take first item length + recursively call for remaining items
    return len(items[0]) + count_characters(items[1:])



print("Initial List:", grocery_list)

add_item("butter")
add_item("cheese")

remove_last_item()

print("\nDisplay Items:")
for i in grocery_list:
    display_item(i)

total_chars = count_characters(grocery_list)
print("\nTotal characters in list:", total_chars)
