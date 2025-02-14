"""Helloooo"""
def main(sen):
    """Helloooo"""
    ans = ""
    count = 0
    for i in sen[::-1]:
        if i in "aeiouAEIOU" and not count:
            ans += i*4
            count += 1
        else:
            ans += i
    print(ans[::-1])
main(input())
