'''for j in range(len(size)):
    if abs(array[i] - array[j]) >= 5:
        size.remove(size[j])
        count += 1'''


def main():
    n,m,k = map(int,input().split())
    array  = list(map(int,input().split()))
    size = list(map(int,input().split()))
    count = 0
    v = False

    for i in range(n):
        a = []
        if len(size)==0:
            break
        for j in range(m):

            if abs(size[j] - array[i])<=k:
                a.append(size[j])
        count+=1
        b = min(a)
        size.remove(b)



    print(count)

main()

