"""Milk"""
def main(n):
    """main"""
    x = n.split()
    num = 0
    for i in x[::-1]:
        if not int(i) % 3:
            print(i)
            num += 1
        elif not int(i) % 5:
            print(i)
            num += 1
    if not num:
        print("Nope")
main(input())
