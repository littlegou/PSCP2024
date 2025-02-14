"""Flatten"""
import json
def ch(l):
    """ch"""
    lis = []
    for i in l:
        if isinstance(i,list):
            lis.extend(ch(i))
        else:
            lis.append(i)
    return lis
def main(l):
    """main"""
    lis = []
    for i in l:
        if isinstance(i,list):
            lis.extend(ch(i))
        else:
            lis.append(i)
    lis.sort(reverse=True)
    print(lis)
main(json.loads(input()))
