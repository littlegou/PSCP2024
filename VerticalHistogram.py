"""VerticalHistogram"""
def main(sen):
    """main"""
    dic = {}
    for i in sen:
        if i.isalpha() and i not in dic:
            dic[i] = 1
        elif i.isalpha():
            dic[i] += 1
    maxx = max(dic.values())
    dic = sorted(dic.items(),key = lambda x:(x[0],x[0].islower()))
    l = len(dic)
    lisans = []
    alp = []
    for i in range(maxx,0,-1):
        ans = f"{i:>2}  "
        for j in range(l):
            alp.append(dic[j][0])
            if i <= dic[j][1]:
                ans += "* "
            else:
                ans += "  "
        lisans.append(ans)
    lisans.append("    "+" ".join(alp[:l]))
    print(*lisans,sep="\n")
main(input())
