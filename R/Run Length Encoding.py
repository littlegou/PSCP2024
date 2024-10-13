"""Run Length Encoding"""
def main(s):
    """main"""
    alp = s[0]
    count = 1
    ans = ""
    for i in s[1:]:
        if i == alp:
            count += 1
        else:
            ans += str(count)+alp
            alp = i
            count = 1
    print(ans+str(count)+alp)
main(input())
