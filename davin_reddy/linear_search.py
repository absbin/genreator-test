pos = -1


def search(lst, n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()["pos"] = i
            return True
        i = i + 1
    return False


lst = [-1, 0, 1, 2, 3, 4, 5, 5, 6, 7]
n = 5
if search(lst, n):
    print("Found at : ", pos)
else:
    print("Not found in the list")
