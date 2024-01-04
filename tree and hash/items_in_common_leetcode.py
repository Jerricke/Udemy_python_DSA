def item_in_common(l1, l2):
    mapper = {}
    for i in l1:
        mapper[i] = True
    for i in l2:
        if i in mapper:
            return True
    return False




list1 = [1,3,5]
list2 = [2,4,5]