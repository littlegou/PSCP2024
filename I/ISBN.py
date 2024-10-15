"""ISBN"""
def main(num):
    """ISBN"""
    x = num[-1] if num[-1] != "X" else 10
    num = num.replace("-","")
    ch = 0
    for i in range(10,1,-1):
        ch += i*int(num[-i])
    ch *= -1
    if int(x) == ch%11:
        print("Yes")
    else:
        print("No", (ch%11 if len(str(ch%11)) == 1 else "X"))
main(input())
