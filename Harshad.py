"""Harshad"""
def main():
    """main"""
    x = 0
    while x<10:
        a = 0
        num = int(input())
        for i in str(abs(num)):
            a += int(i)
        if not a:
            print("No")
        elif not num%a:
            print("Yes")
        else:
            print("No")
        x += 1
main()
