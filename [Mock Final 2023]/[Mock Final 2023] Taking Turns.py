"""Taking Turns"""
import json
from math import ceil
def main():
    """Taking Turns"""
    lis = json.loads(input())
    l = len(lis)
    ans = []
    for i in range(ceil(l/2)):
        ans.append(lis[(l-1)-i] if not i%2 else lis[i])
        ans.append(lis[i] if not i%2 else lis[(l-1)-i])
    if not l%2:
        print(ans)
    else:
        print(ans[:-1])
main()
