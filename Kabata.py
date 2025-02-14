"""Kabata"""
def main():
    """main"""
    n = int(input())
    ans = []
    for _ in range(n):
        sen = input()
        if sen.find("baka") != -1:
            ans.append("no")
        else:
            sen = sen.replace("bakka","")
            sen = sen.replace("ba","")
            sen = sen.replace("ka","")
            sen = sen.replace("ta","")
            if not sen:
                ans.append("yes")
            else:
                ans.append("no")
    print(*ans,sep="\n")
main()
