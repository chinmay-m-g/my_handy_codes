# import numpy as np

# i_list = np.random.randint(1, 100, size=100)
# i_list = list(i_list)
# # i_list.append(25)
# print(i_list)


def linear_search(i_list, key):
    for i, element in enumerate(i_list):
        if element == key:
            return i
    return -1
