"""3nPlus1"""
def cou(n):
    """count"""
    count = 1
    while n != 1:
        if not n%2:
            n /= 2
            count +=1
        else:
            n = n*3 + 1
            count += 1
    return count
def main(n):
    """main"""
    while n:
        print(cou(n))
        n = int(input())
main(int(input()))
