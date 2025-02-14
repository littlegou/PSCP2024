"""isprime_all"""
def is_prime(num):
    """is_prime"""
    check = 0
    for i in range(2,int(num**0.5)+1):
        if not num%i:
            print("NO")
            check = 1
            break
    if not num or num == 1:
        print("NO")
    elif not check:
        print("YES")
def main():
    """main"""
    num = int(input())
    is_prime(num)
main()
