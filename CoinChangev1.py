"""[Not recommended] CoinChange"""
def main(n):
    """main"""
    print(n//25 + (n%25)//10 + ((n%25)%10)//5 + ((n%25)%10)%5)
main(int(input()))
