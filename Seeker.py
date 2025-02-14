"""Seeker"""
def main(sen):
    """main"""
    ans = 0
    num = "0"
    for i in sen:
        if i.isnumeric():
            num += i
        elif num:
            ans += int(num)
            num = "0"
    print(ans+int(num))
main(input())
