"""Backward"""
def main(w):
    """main"""
    lis = []
    while w != "NULL":
        lis.append(w)
        w = input()
    lis = lis[::-1]
    print("\n".join(lis))
main(input())
