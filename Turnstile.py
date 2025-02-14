"""Turnstile"""
def main():
    """main"""
    a = input()
    lis = []
    count = 0
    while a != "END":
        lis.append(a)
        a = input()
    lis.append(" ")
    b = len(lis)
    for i in range(b):
        if lis[i] == "C" and lis[i+1] == "P":
            count += 1
    print(count)
main()
