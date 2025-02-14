"""Sequence XXX"""
def main(n,m):
    """main"""
    for i in range(n):
        ans = ""
        for j in range(n):
            if not i or i == n-1:
                ans += "*"
            elif not i or i == n-1:
                ans += " "
            elif not j or j == n-1 or i == j or j == n-i-1:
                ans += "*"
            else:
                ans += " "
        print((ans+" ")*m)
main(int(input()),int(input()))
