"""[Final 2020] Lucky Number"""
def main(n):
    """[Final 2020] Lucky Number"""
    lis = list(range(1,n+1,2))
    i = 1
    if n > 2:
        while i < len(lis):
            l = lis[i]
            ch = lis.copy()
            for j in range(l,len(ch)+1,l):
                lis.remove(ch[j-1])
            i += 1
        print(*lis)
    else:
        print(1)
main(int(input()))
