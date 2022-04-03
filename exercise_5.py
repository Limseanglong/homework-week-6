def backward(string):
    list1 = []
    list2 = string.split()
    # reverse every word
    for i in list2:
        list1.append(i[::-1])
    # put the words back to their places
    for j in range(len(list2)):
        string = string.replace(list2[j], list1[j])

    return string
