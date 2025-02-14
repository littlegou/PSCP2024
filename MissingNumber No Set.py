"""MissingNumber No Set"""
def main(n,num):
    """main"""
    lis = []
    while num:
        lis.append(num)
        num = int(input())
    for i in range(1,n+1):
        if i in lis:
            pass
        else:
            print(i)
main(int(input()),int(input()))
