def main():
    n = int(input())
    colors = input()
    count = 0
    for i in range(len(colors)-1):
        if colors[i] == colors[i+1]:
            count+=1


    print(count)
main()