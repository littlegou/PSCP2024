"""SumOfNumber"""
def main(need,x):
    """main"""
    ans = 0
    while x!=-1 and ans != need:
        ans += x
        if ans == need:
            break
        x = int(input())
    print(ans)
main(int(input()),int(input()))
