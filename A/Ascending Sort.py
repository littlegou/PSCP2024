"""Ascending Sort"""
def main():
    """main"""
    number = []
    n = int(input())
    for _ in range(n):
        a = int(input())
        number.append(a)
    number.sort()
    for x in number:
        print(x)
main()
