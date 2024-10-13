"""Rabbit"""
def main(x,y,n):
    i = 1
    while y >= i and x > 0 and n > 0:
        y -= i
        x -= 1
        n -= 1
        i += 1
    print("Ahhahaha" if not x and not y and not n else f"{x} {y} {n}")
main(int(input()),int(input()),int(input()))
