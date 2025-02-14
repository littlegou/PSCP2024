"""Hamburger"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    n = ((a+b)*2)*"*"
    ans = ("|"*a)+n+("|"*b)
    print(ans)
main()
