import random

accesses = 0


def insertion_sort(ls, comparison_callback):
    global accesses
    final_list = []
    while ls:
        lowest_item = ls[0]
        accesses += 1
        print("ls is " + str(len(ls)) + " items long.")
        if len(ls) < 20:
            print(ls)
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


print("Creating list")
ls = []
for i in range(10000):
    ls.append(random.randint(0, 9))
print("Created list")
print(insertion_sort(ls, lambda a, b: -1 if a < b else (1 if a > b else 0)))
print("Sorted list")
print("Accesses: " + str(accesses))
