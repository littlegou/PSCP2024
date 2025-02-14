"""isprime_all"""
def is_prime(num):
    """is_prime"""
    for i in range(3,int(num**0.5)+1,2):
        if not num%i:
            return print("False")
    if not num or num == 1 or (not num%2 and num != 2):
        return print("False")
    return print("True")
def main():
    """main"""
    num = int(input())
    is_prime(num)
main()
