"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main(sen):
    """main"""
    lis = sen.split()
    lis.sort()
    count = 0
    ans = []
    for i in lis:
        for j in i:
            if j in ("AEIOUaeiou"):
                count += 1
        if count>=2:
            ans.append(i)
        count = 0
    for i in ans:
        for j in i:
            if j.isalpha():
                print(j,end="")
        print()
    if not ans:
        print("Nope")
main(input())
