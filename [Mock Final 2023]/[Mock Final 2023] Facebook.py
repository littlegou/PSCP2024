"""Facebook"""
def main(n):
    """Facebook"""
    dic = {}
    while "<->" in n:
        n = n.split(" <-> ")
        if n[0] not in dic:
            dic[n[0]] = set()
            dic[n[0]].add(n[1])
        else:
            dic[n[0]].add(n[1])
        if n[1] not in dic:
            dic[n[1]] = set()
            dic[n[1]].add(n[0])
        else:
            dic[n[1]].add(n[0])
        n = input()
    find = n.split(" ? ")
    ans = sorted(list(dic.get(find[0],{"21"})&dic.get(find[1],{"1"})))
    if ans:
        for i in ans:
            print(i)
    else:
        print("No mutual friend")
main(input())
