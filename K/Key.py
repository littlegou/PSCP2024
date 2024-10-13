"""Key"""
def main():
    """a"""
    x = input()
    ans = 0
    for i in x:
        ans += int(i)
    a = int(str(x)[10:])*10
    ans += a
    if len(str(ans))>4:
        ans = str(ans)[-4:]
    elif ans<1000:
        ans += 1000
        ans = str(ans)[-4:]
    print(ans)
main()
