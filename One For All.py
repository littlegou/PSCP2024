"""One For All"""
def main(x):
    """main"""
    if not x:
        print()
    else:
        ans = ""
        for i in range(1,x):
            name = input()
            if i%2:
                ans += (name + ("*"*i))
            else:
                ans += (name + ("-"*i))
        name = input()
        ans += f"{name}_{x}"
        print(ans)
main(int(input()))
