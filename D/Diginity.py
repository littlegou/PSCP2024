"""number"""
def main(x):
    """main"""
    while x:
        ans = 0
        while len(str(x))>1:
            for i in str(x):
                ans += int(i)
            x = ans
            ans = 0
        print(x)
        x = int(input())
main(int(input()))
