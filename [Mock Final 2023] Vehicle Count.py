"""[Mock Final 2023] Vehicle Count"""
def main(edg):
    """[Mock Final 2023] Vehicle Count"""
    n = input()
    lis = []
    while n != edg:
        lis.append(n.strip("|").split("|"))
        n = input()
    lisans = []
    anslaew = [0,0,0,0,0]
    if not lis:
        print(*anslaew,sep="\n")
        return
    for i in range(len(lis[0])):
        ans = ""
        l = len(lis)
        for j in range(l):
            ans += "x" if lis[j][i] == " x " else "  "
        lisans.append(ans)
    for i in lisans:
        anslaew[0] += i.count(" x ")
        i = i.replace(" x ","_")
        anslaew[1] += i.count(" xx ")
        i = i.replace(" xx ","_")
        anslaew[2] += i.count(" xxx ")
        i = i.replace(" xxx ","_")
        i = i.replace("_"," ")
        for j in i.split():
            if len(j)>=4:
                anslaew[3] += 1
            else:
                anslaew[4] += 1
    print(*anslaew,sep="\n")
main(input())
