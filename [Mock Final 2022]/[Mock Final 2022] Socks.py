"""Socks"""
def main(sen):
    """Socks"""
    dic = {}
    for i in sen:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    lis = list(dic.items())
    lis.sort(key = lambda x:x[0])
    ans = ""
    for i in lis:
        ans += f"{i[0]}{i[0]} "*(int(i[1])//2)
    print(ans.strip() if ans.strip() else "None")
    print(ans.count(" ") if ans.strip() else 0)
main(input())
