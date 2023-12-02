'''def main():
    n = int(input())
    numbers = list(map(int,input().split()))
    s = set(numbers)

    for i in range(1,n):
        if i not in s:
            print(i)
            return
main()'''

def main():
    n = int(input())
    if n == 3:
        print(3)
    elif n== 2:
        print(2)
    else:
        print(n+1)

main()



