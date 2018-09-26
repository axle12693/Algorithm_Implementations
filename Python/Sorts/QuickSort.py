import random
import math


INSERT_THRESHOLD = 10
accesses = 0


def insertion_sort(ls, comparison_callback):
    global accesses
    final_list = []
    while ls:
        lowest_item = ls[0]
        accesses += 1
        for i in ls:
            if comparison_callback(i, lowest_item) == -1:
                lowest_item = i
                accesses += 1
            accesses += 1
        final_list.append(lowest_item)
        accesses += 1
        ls.remove(lowest_item)
        accesses += 1
    return final_list


def quick_sort(ls, comparator_callback):
    global accesses
    print("Quick sort, ls length is: " + str(len(ls)))
    if len(ls) == 0:
        return []
    if len(ls) < INSERT_THRESHOLD:
        return insertion_sort(ls, comparator_callback)
    else:
        pivot_index = math.floor(len(ls)/2)
        left_list = []
        right_list = []
        for i in range(len(ls) - 1):
            if i != pivot_index:
                if comparator_callback(ls[i], ls[pivot_index]) == -1:
                    left_list.append(ls[i])
                    accesses += 3
                elif comparator_callback(ls[i], ls[pivot_index]) == 1:
                    right_list.append(ls[i])
                    accesses += 3
                else:
                    if random.randint(0, 1):
                        left_list.append(ls[i])
                        accesses += 2
                    else:
                        right_list.append(ls[i])
                        accesses += 2
        return quick_sort(left_list, comparator_callback) \
            + [ls[pivot_index]] + quick_sort(right_list, comparator_callback)


c = 0
print("Creating list")
ls = []
for i in range(10000):
    ls.append(random.randint(0, 100000))
print("Created list")
print(quick_sort(ls, lambda a, b: -1 if a < b else (1 if a > b else 0)))
print("Sorted list")
print("Accesses: " + str(accesses))
