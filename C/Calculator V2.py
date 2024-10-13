"""Cal"""
def main(n):
    """main"""
    count = 0
    for i in range(len(str(n))):
        count += n-int(0 if not i*"9" else i*"9")
    print(count+n if n>1 else 1)
main(int(input()))
