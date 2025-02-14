"""Day I"""
def main(y):
    """main"""
    if not y%4:
        if y%100:
            print("Yes")
        else:
            if not y%400:
                print("Yes")
            else:
                print("No")
    else:
        print("No")
main(int(input()))
