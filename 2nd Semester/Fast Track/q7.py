'''def main():
    n,m = map(int,input().split())
    array = [''] * n
    array[0]+='#'*m
    j = 2
    for i in range(1,n,2):
        if j % 2==0:
            array[i]+='.'*(m-1) + '#'
        else:
            array[i]+='#'*(m-1) + '.'
        array[i+1] += '#'*m
        j+=1
    for i in range(n):
        print(array[i])

main()'''
def main():
    n,m = map(int,input().split())
    s='#'*m
    j = 2
    for i in range(1,n,2):
        s+='\n'
        if j % 2==0:
            s+='.'*(m-1) + '#' + '\n'
        else:
            s+='#' + '.'*(m-1)+ '\n'
        s += '#'*m
        j+=1
    print(s)

main()