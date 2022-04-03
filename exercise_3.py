def remove_all_after(lst, n):
    list = []
    for i in lst:
        if i <= n:
            list.append(i)
        else:
            break
    
    if list[-1] == list[-2]:
        list.pop(-1)
        print(list)
    else:
        print(list)

remove_all_after([1, 2, 3, 4, 5], 3)