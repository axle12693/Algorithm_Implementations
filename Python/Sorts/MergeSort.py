import random

accesses = 0

def merge_sort(ls, comparison_callback):
    global accesses
    print("Started merge_sort with ls = " + str(ls))
    ls1 = []
    ls2 = []
    while True:
        writing_to_ls1 = True
        prev_element = None
        for element in ls:
            if prev_element is None:
                prev_element = element
                accesses += 1
            elif comparison_callback(prev_element, element) == 1:
                accesses += 1
                writing_to_ls1 = not writing_to_ls1

            (ls1 if writing_to_ls1 else ls2).append(element)
            prev_element = element
            accesses += 1
        index1 = 0
        index2 = 0
        print("Split ls into: ")
        print("ls1: " + str(ls1))
        print("ls2: " + str(ls2))
        if not ls2:
            return ls1
        ls1 = merge_sort(ls1, comparison_callback)
        ls2 = merge_sort(ls2, comparison_callback)
        new_ls = []
        while index1 <= len(ls1) - 1 and index2 <= len(ls2) - 1:
            while index1 != 0 and (index1 <= len(ls1) - 1) and (index2 <= len(ls2) - 1) and comparison_callback(ls1[index1 - 1], ls1[index1]) == 1 and comparison_callback(ls2[index2 - 1], ls2[index2]) != 1:
                accesses += 4
                new_ls.append(ls2[index2])
                accesses += 1
                index2 += 1
                continue
            while index2 != 0 and (index1 <= len(ls1) - 1) and (index2 <= len(ls2) - 1) and comparison_callback(ls2[index2 - 1], ls2[index2]) == 1 and comparison_callback(ls1[index1 - 1], ls1[index1]) != 1:
                accesses += 4
                new_ls.append(ls1[index1])
                accesses += 1
                index1 += 1
                continue
            if (index1 <= len(ls1) - 1) and (index2 <= len(ls2) - 1) and comparison_callback(ls1[index1], ls2[index2]) == -1:
                accesses += 2
                new_ls.append(ls1[index1])
                accesses += 1
                index1 += 1
            elif (index1 <= len(ls1) - 1) and (index2 <= len(ls2) - 1):
                new_ls.append(ls2[index2])
                accesses += 1
                index2 += 1
            if index1 > len(ls1) - 1 and index2 <= len(ls2) - 1:
                while index2 <= len(ls2) - 1:
                    new_ls.append(ls2[index2])
                    accesses += 1
                    index2 += 1
            if index2 > len(ls2) - 1 and index1 <= len(ls1) - 1:
                while index1 <= len(ls1) - 1:
                    new_ls.append(ls1[index1])
                    accesses += 1
                    index1 += 1
        print("new_ls = " + str(new_ls))
        return merge_sort(new_ls, comparison_callback)


print("Creating list")
ls = []
for i in range(100):
    ls.append(random.randint(0, 100))
print("Created list")
print(ls)
# bubble_sort(ls, lambda a, b: -1 if a < b else (1 if a > b else 0))
print(merge_sort(ls, lambda a, b: -1 if a < b else (1 if a > b else 0)))
print("Sorted list")
print("Accesses: " + str(accesses))

