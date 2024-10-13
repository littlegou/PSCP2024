"""Century"""
def main(n):
    """main"""
    for _ in range(n):
        a = input()
        if a[:4] == "B.E.":
            a = int(a[5:])-543
        elif a[:4] == "A.D.":
            a = int(a[5:])
        if a<0:
            print("ERROR")
        elif not a%100:
            print(a//100)
        else:
            print((a//100)+1)
main(int(input()))
