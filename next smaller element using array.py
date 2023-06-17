def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result array with -1

    # Extend the array by appending a copy of itself
    arr_extended = arr + arr

    for i in range(n):
        for j in range(i + 1, i + n):
            if arr_extended[j] < arr[i]:
                result[i] = arr_extended[j]
                break

    return result


# Example usage
arr = [3,10,4,2,1,2,6,1,7,2,9]
nse = next_greater_element(arr)
print("The next smaller element are:")
print(nse)


#nse stand for next smaller element
