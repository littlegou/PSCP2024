"""Olympic"""
def main(n):
    """main"""
    lis = []
    for _ in range(n):
        sen = input().split()
        sen.append(str(int(sen[1])+int(sen[2])+int(sen[3])))
        lis.append(sen)
    lis = sorted(lis,key = lambda x:(-int(x[1]),-int(x[2]),-int(x[3]),x[0]))
    l = len(lis)
    lis.append(["","","",""])
    rem = 0
    for i in range(1,l+1):
        if lis[i-1][1:] == lis[i][1:]:
            print(str(i-rem) , " ".join(lis[i-1]))
            rem += 1
        else:
            print(str(i-rem) , " ".join(lis[i-1]))
            rem = 0
main(int(input()))
