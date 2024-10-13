"""isprime_all"""
def is_prime(num):
    """is_prime"""
    check = 0
    for i in range(2,num):
        if not num%i:
            print("No")
            check = 1
            break
    if not num or num == 1:
        print("No")
    elif not check:
        print("Yes")
def main():
    """main"""
    num = int(input())
    is_prime(num)
main()
