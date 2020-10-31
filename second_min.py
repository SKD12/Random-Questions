def sort(list):

# Swap the elements to arrange in order
    for pos in range(len(list)-1,0,-1):
        for POS in range(pos):
            if list[POS]>list[POS+1]:
                temp = list[POS]
                list[POS] = list[POS+1]
                list[POS+1] = temp


list = [8,6,4,1,3]
sort(list)
print(list[1])