"""Safe"""
def main(bf,key):
    """main"""
    ans = 0
    l = len(bf)
    for i in range(l):
        ans += min(abs(ord(bf[i]) - ord(key[i])),26-abs(ord(key[i]) - ord(bf[i])))
    print(ans)
main(input(),input())
