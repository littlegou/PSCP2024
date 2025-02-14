"""[Midterm 2024] Real"""
def check():
    """y"""
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    f = input()
    g = input()
    xy = ""
    x = a == b == c == d == e == f == "on"
    y = g == "off"
    if x and y:
        xy = "0"
    x = b == c == "on"
    y = a == d == e == f == g == "off"
    if x and y:
        xy = "1"
    x = a == b == d == e == g == "on"
    y = c == f == "off"
    if x and y:
        xy = "2"
    x = a == b == c == d == g == "on"
    y = e == f == "off"
    if x and y:
        xy = "3"
    x = b == c == f == g == "on"
    y = a == d == e == "off"
    if x and y:
        xy = "4"
    x = a == c == d == g == f == "on"
    y = b == e == "off"
    if x and y:
        xy = "5"
    x = a == c == d ==e == f == g == "on"
    y = b == "off"
    if x and y:
        xy = "6"
    x = a == b == c == "on"
    y = d == e == f == g == "off"
    if x and y:
        xy = "7"
    x = a == b == c == d == e == f == g == "on"
    if x:
        xy = "8"
    x = a == b == c == d == g == f == "on"
    y = e == "off"
    if x and y:
        xy = "9"
    if not xy:
        return "Error"
    return xy
def main():
    """main"""
    ans = ""
    for _ in range(3):
        yay = check()
        dp = input()
        ans += yay
        if dp == "on":
            ans += "."
    if ans.count(".")>1 or ans.find("Error") != -1:
        print("Error")
    else:
        print(f"{float(ans):.2f}")
main()
