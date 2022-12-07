# import numpy as np

# i_list = np.random.randint(1, 100, size=100)
# i_list.sort()
# i_list = list(i_list)
# # i_list.append(25)
# print(i_list)


def binary_search(i_list, key):
    left = 0
    right = len(i_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if i_list[middle] == key:
            return middle
        if i_list[middle] > key:
            right = middle - 1
        if i_list[middle] < key:
            left = middle + 1
    return -1


# print(binary_search(i_list, 80))

# Binary_search using recursion
def find_item(list, item):
    # Returns True if the item is in the list, False if not.
    if len(list) == 0:
        return False

    # Is the item in the center of the list?
    middle = len(list) // 2
    if list[middle] == item:
        return True

    # Is the item in the first half of the list?
    if item < list[middle]:
        # Call the function with the first half of the list
        return find_item(list[:middle], item)
    else:
        # Call the function with the second half of the list
        return find_item(list[middle + 1 :], item)

    return False
