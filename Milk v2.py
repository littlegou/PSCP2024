"""Milk v2"""
def main(a,b,c,d,e):
    """Milk v2"""
    f = float(input())
    ans = f//a
    fa = f//a
    bot = f//a
    while fa >= b or bot >= d:
        ch1 = fa>=b
        ch2 = bot >= d
        fa -= (b*(ch1))
        fa += c*(ch1)+e*(ch2)
        bot += c*(ch1)+e*(ch2)
        bot -= (d*(ch2))
        ans += c*(ch1)+e*(ch2)
    print(int(ans))
main(float(input()),int(input()),int(input()),int(input()),int(input()))
