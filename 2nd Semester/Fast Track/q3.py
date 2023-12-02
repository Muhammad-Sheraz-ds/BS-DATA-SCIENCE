def main():
    n,k = map(str,input().split())
    count = 0
    for i in range(len(n)):
        if n[i] == k:
            count+=1
    if count==int(k):
        print('YES')
    else:
        print('NO')
main()
