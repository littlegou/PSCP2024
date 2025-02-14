"""Difference"""
import json
def main(a,b):
    """Difference"""
    dic = {}
    for i in a:
        if i in b:
            if i not in dic:
                dic[i] = str(abs(a.count(i)-b.count(i)))
            while i in b:
                b.remove(i)
        else:
            if i not in dic:
                dic[i] = str(a.count(i))
    for i in b:
        if i not in dic:
            dic[i] = str(b.count(i))
    lis = sorted(list(dic.items()),key=lambda x:x[0])
    if lis and len(lis) != (list(dic.values())).count("0"):
        for i in lis:
            if i[1] != "0":
                print(" ".join(i))
    else:
        print("ONAJI DAYO!")
main(json.loads(input()),json.loads(input()))
