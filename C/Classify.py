"""Classify"""
def main(x):
    """main"""
    lis = []
    while x != "END":
        lis.append(x[:4])
        x = input()
    lis.sort()
    ans = []
    dic = {i:lis.count(i) for i in lis}
    for i in dic:
        ans.append([i[:2]] + [i[2:].lstrip("0")] + [str(dic[i])])
    a = len(ans)
    for i in range(a):
        if not i or ans[i][0] != check:
            print(" ".join(ans[i]))
        elif ans[i][0] == check:
            print("-- "+ " ".join(ans[i][1:]))
        check = ans[i][0]
main(input())
