"""Run Length Decoding"""
def main(x):
    """main"""
    ans = ""
    num = ""
    for i in x:
        if i.isnumeric():
            num += str(i)
        else:
            ans += int(num) * str(i)
            num = ""
    print(ans)
main(input())
