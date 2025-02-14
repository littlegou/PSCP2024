"""[Recommend] ISBN"""
def main(num):
    """[Recommend] ISBN"""
    ch = int(num[-1]) if num[-1].isnumeric() else 10
    a = 10
    ans = 0
    for i in num[:-1]:
        ans += int(i)*a
        a -= 1
    x = "X"
    print("Yes" if (-ans)%11 == ch else f"No {(-ans)%11 if (-ans)%11 != 10 else x}")
main(input().replace("-",""))
