"""Runner"""
def main(dist,team):
    """main"""
    al = []
    for _ in range(team):
        x = input().split()
        x = list(map(int,x))
        al.append(x)
    lisans = []
    for i in al:
        ans = (dist - i[1])/i[0]
        lisans.append(ans)
    ans = min(lisans)
    lisagain = []
    for i in al:
        if (dist - i[1])/i[0] == ans:
            lisagain.append(i)
    lisagain.sort(key = lambda x:-x[0])
    print(al.index(lisagain[0])+1)
main(float(input()),int(input()))
