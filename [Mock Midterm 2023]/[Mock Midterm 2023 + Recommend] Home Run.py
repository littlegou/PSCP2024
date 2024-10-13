"""Home Run"""
def main(n,rang):
    """main"""
    count = 0
    for _ in range(n):
        base = float(input())
        if base<rang:
            count += 1
    print(count)
main(int(input()),float(input()))
