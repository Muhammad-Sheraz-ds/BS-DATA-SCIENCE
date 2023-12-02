def first_index(list,i1,i2):
    for i in range(len(list)):
        for j in range(len(list)):
            if i!=i1 and j!=i2:
                if list[i] +list[j]==list[i1]+list[i2]:
                    return i
def second_index(list,i1,i2):
    for i in range(len(list)):
        for j in range(len(list)):
            if i!=i1 and j!=i2:
                if list[i] +list[j]==list[i1]+list[i2]:
                    return j

def main():
    list = [9, 10, 23, 15, 47, 2, 29, 36, 58, 14, 30, 16, 90, 40, 83]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] + list[j] == list[first_index(list,i,j)]+list[second_index(list,i,j)] and list[i]!=list[second_index(list,i,j)] and j !=list[first_index(list,i,j)] and j!=i:
                print(f'{list[i]},{list[j]}has sum equal to {list[first_index(list,i,j)]},{list[second_index(list,i,j)]}' )
main()