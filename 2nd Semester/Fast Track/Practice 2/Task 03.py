def difference_of_list(min_list,max_list):
    max = max_list[0] - min_list[0]
    index = 0
    for i in range(len(max_list)):
        if max < max_list[i] - min_list[i]:
            max = max_list[i] - min_list[i]
            index = i
    return index

def main():
    list = [9,10,23,15,47,2,29,36,58,14,30,16,90,40,83]
    min_list = []
    max_list = []
    min = 0
    max = 0
    index = 0
    while index < len(list)-1:

        if list[index] < list[index+1]:
            min = index
            max= 0

            while list[index] < list[index+1] and index < len(list)-2:
                max = index+1
                index+=1
            min_list.append(min)
            max_list.append(max)
        index+=1

    I = difference_of_list(min_list,max_list)
    i1 = min_list[I]
    i2 = max_list[I]
    for index in range(i1,i2+1):
        print(list[index])

main()

