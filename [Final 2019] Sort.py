"""[Final 2019] Sor_t"""
def main():
    """main"""
    n = input()
    lis = []
    while n != "END":
        lis.append(int(n))
        n = input()
    while lis:
        print(min(lis))
        lis.remove(min(lis))
main()
