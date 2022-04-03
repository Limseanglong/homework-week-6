import math
def chunklist(list,chunk_size):
    chunks=[]
    length = len(list)
    counter = 0
    chunknumber= 0
    for i in range(math.ceil(len(list)/chunk_size)):
        chunks.append([])
    for j in range(length):
        chunks[chunknumber].append(list[j])
        counter+=1
        if counter == chunk_size:
            counter = 0
            chunknumber+=1
    print(chunks)

chunklist([5, 4, 7, 3, 4, 5, 4], 3)
chunklist([3, 4, 5], 1)

