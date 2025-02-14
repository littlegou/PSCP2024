"""Cat Parade"""
def main(s):
    """main"""
    lis = []
    while s != "END":
        if s == "IT'S A DOG":
            lis = lis[:-1]
        else:
            lis.extend(s.split(", "))
        s = input()
    newlis = sorted(lis)
    ans = []
    for i in newlis:
        yoy = [i,str(lis.index(i)+1),str(lis.count(i))]
        if yoy in ans:
            pass
        else:
            ans.append(yoy)
    for i in ans:
        print(" ".join(i))
main(input())
