def bubble_sort(lst):
    for i in range(len(lst) - 1):

        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                a, b = lst[j], lst[j + 1]
                lst[j], lst[j + 1] = b, a
    return lst


lst = [2, 1, 4, 7, 8, 2, 3]
lst_sorted = bubble_sort(lst)
print("Sorted list is : {}".format(lst_sorted))
