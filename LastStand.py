"""LastStand"""
import json
def main(n):
    """main"""
    n = json.loads(n)
    for i in n:
        print(str(i)[-1])
main(input())
