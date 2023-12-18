def descending_order(num):
    testNum = list(str(num))
    testNum.sort(reverse = True)
    num = int("".join(testNum))
    return num
print(descending_order(123456789))
# print(descending_order(15))
# print(descending_order(0))