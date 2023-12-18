def array_diff(a, b):
    for selected in b: 
        while (a.count(selected)):
            a.remove(selected)
    return a
print(array_diff([1, 2, 3],[1,2]))
# print(array_diff([], [1,2]))
# print(array_diff([1,2,2], []))
# print(array_diff([1,2,2], [2]))
# print(array_diff([1,2,2], [1]))