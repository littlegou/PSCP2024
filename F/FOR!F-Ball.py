"""FOR!F-Ball"""
def main(x):
    """main"""
    ans = 1
    for i in x:
        if i == "A":
            if ans == 1:
                ans +=1
            elif ans == 2:
                ans -= 1
        elif i == "B":
            if ans == 2:
                ans += 1
            elif ans == 3:
                ans -= 1
        elif i == "C":
            if ans == 1:
                ans += 2
            elif ans == 3:
                ans -= 2
    print(ans)
main(input())
