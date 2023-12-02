def main():
    list = [9, 10, 23, 15, 47, 2, 29, 36, 58, 14, 30, 16, 90, 40, 83]
    for i in range(len(list)):
        small_middle = 0
        greater_middle = 0
        for j in range(len(list)):
            if list[i] < list[j]:
                small_middle +=1
            elif list[i] > list[j]:
                greater_middle +=1
        if greater_middle == 7 and small_middle==7:
            return list[i]
print(main())