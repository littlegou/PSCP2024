"""Flatten"""
import json
def main(l):
    """main"""
    sen = "["
    for i in l:
        if i not in ("[","]"):
            sen+=i
    sen += "]"
    lis = json.loads(sen)
    lis.sort(reverse= True)
    print(lis)
main(input())
