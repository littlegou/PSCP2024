"""EOD"""
def main(num):
    """main"""
    print("Even"*bool(not num%2),end="")
    print("Odd"*bool(num%2))
main(int(input()))
