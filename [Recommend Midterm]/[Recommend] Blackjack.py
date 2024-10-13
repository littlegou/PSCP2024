"""[Recommend] Blackjack"""
def check(card):
    """check"""
    if card in ("J","Q","K"):
        return "10"
    return card
def find2():
    """find"""
    ans = 0
    a = 0
    for _ in range(2):
        card1 = check(input())
        if card1.isalpha():
            a += 1
        else:
            ans += int(card1)
    for _ in range(a):
        if ans+11<=21:
            ans += 11
        else:
            ans += 1
    return ans
def find3():
    """find"""
    a = 0
    ans = 0
    for _ in range(3):
        card1 = check(input())
        if card1.isalpha():
            a += 1
        else:
            ans += int(card1)
    if a == 3:
        ans = 13
    elif a == 2:
        if ans+12<=21:
            ans += 12
        else:
            ans += 2
    elif a == 1:
        if ans+11<=21:
            ans += 11
        else:
            ans += 1
    return ans
def main(hm):
    """main"""
    if hm == 2:
        print(find2())
    elif hm == 3:
        print(find3())
main(int(input()))
