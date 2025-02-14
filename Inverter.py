"""Inverter"""
def main():
    """main"""
    num = input()
    ans = ""
    for i in num:
        if i == "1":
            ans += "0"
        elif i == "0":
            ans += "1"
    print(ans.lstrip("0"))
main()
