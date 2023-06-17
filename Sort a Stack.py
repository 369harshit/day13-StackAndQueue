def sort_stack(stack):
    stack_list = stack  # Convert stack to a list
    stack_list.sort(reverse=True)  # Sort the list in descending order
    sorted_stack = stack_list[::1]  # Convert the sorted list back to a stack
    return sorted_stack


# Example usage
stack = [4, 2, 9, 6, 1, 5]
sorted_stack = sort_stack(stack)
print(sorted_stack)
