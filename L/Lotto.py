"""Lotto"""
def main(onepr,two,f31,f32,l31):
    """main"""
    ans = 0
    l32 = input()
    my = input()
    if my == onepr:
        ans += 6000000
    if my[-2:] == two:
        ans += 2000
    if my[:-3] == f31:
        ans += 4000
    if my[:-3] == f32:
        ans += 4000
    if my[-3:] == l31:
        ans += 4000
    if my[-3:] == l32:
        ans += 4000
    if my == str((int(onepr)+1000001))[-6:]:
        ans += 100000
    if my == str((int(onepr)+999999))[-6:]:
        ans += 100000
    print(ans)
main(input(),input(),input(),input(),input())
