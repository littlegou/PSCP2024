"""coprimeV1"""
def is_prime(num_1,num_2):
    """is_prime"""
    check = 0
    for i in range(min(num_1,num_2),1,-1):
        if not num_1%i and not num_2%i:
            print("NO")
            print(i)
            check = 1
            break
    if not num_1 and num_2 != 1:
        print("NO")
        print(num_2)
    elif not num_2 and num_1 != 1:
        print("NO")
        print(num_1)
    elif not check:
        print("YES")
        print(1)
def main():
    """main"""
    num_1 = abs(int(input()))
    num_2 = abs(int(input()))
    is_prime(num_1,num_2)
main()
