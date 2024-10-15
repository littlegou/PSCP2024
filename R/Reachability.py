"""Reachability"""
import json
def main(dic,a):
    """Reachability"""
    lis = [a]
    i = 0
    while i < len(lis):
        for j in dic[lis[i]]:
            if j not in lis:
                lis.append(j)
        i += 1
    print(sorted(lis))
main(json.loads(input().replace("'",'"')),input())
