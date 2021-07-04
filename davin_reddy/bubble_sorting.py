def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                a, b = lst[j], lst[j + 1]
                lst[j], lst[j + 1] = b, a
    return lst

lst_i = [2, 1, 4, 7, 8, 2, 3,10,12,0]
aa=lst_i
print(lst_i)
lst_sorted = bubble_sort(aa)
print("{x}\nSorted list is : {y}".format(x=lst_i,y=lst_sorted))

print('*******************************')

lst_i = [2, 1, 4, 7, 8, 2, 3,10,12,0]
aa=lst_i.copy()
print(lst_i)
lst_sorted = bubble_sort(aa)
print("{x}\nSorted list is : {y}".format(x=lst_i,y=lst_sorted))
