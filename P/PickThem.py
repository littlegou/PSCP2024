"""Milk"""
import json
def main(n):
    """main"""
    x = json.loads(n)
    num = 0
    for i in x:
        if not i % 2:
            print(i)
            num += 1
    if not num:
        print("Nope")
main(input())
