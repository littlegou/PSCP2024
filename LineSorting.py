"""LineSorting"""
def main(n):
    """main"""
    lis = []
    for _ in range(n):
        lis.append(input())
    newlis = sorted(lis, key=len)
    for i in newlis:
        print(i)
main(int(input()))
