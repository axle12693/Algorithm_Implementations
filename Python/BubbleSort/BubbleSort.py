import random

accesses = 0


def bubble_sort(inputs_list, comparison_callback):

    global accesses
    for i in range(0, len(inputs_list)):
        print("Looping through " + str(len(inputs_list) - i) + " items")
        for j in range(0, len(inputs_list) - 1 - i):
            if comparison_callback(inputs_list[j], inputs_list[j + 1]) == 1:
                accesses += 2
                temp = inputs_list[j]
                accesses += 1
                inputs_list[j] = inputs_list[j + 1]
                accesses += 2
                inputs_list[j + 1] = temp
                accesses += 1
    return inputs_list


print("Creating list")
ls = []
for i in range(10000):
    ls.append(random.randint(0, 100000))
print("Created list")
# bubble_sort(ls, lambda a, b: -1 if a < b else (1 if a > b else 0))
print(bubble_sort(ls, lambda a, b: -1 if a < b else (1 if a > b else 0)))
print("Sorted list")
print("Accesses: " + str(accesses))
