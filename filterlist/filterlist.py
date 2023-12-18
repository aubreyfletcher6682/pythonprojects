def filter_list(l):
    newList = []
    num = 0
    for element in l:
        if isinstance(element, str) == False:
            newList.insert(num,element)
            num += 1
    return newList
#print (filter_list([1, 'a', 'b', 0, 15]))
#print (filter_list([1, 2, 'a', 'b']))
#print (filter_list([1, 2, 'aasf', '1', '123', 123]))

