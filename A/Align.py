"""Align"""
def main():
    """main"""
    size = int(input())
    dis = input()
    word = input()
    x = len(word)
    if not (size-x)%2:
        left = (size-x)/2
        right = (size-x)/2
    else:
        left = ((size-x)//2)+1
        right = (size-x)//2
    if dis == "left":
        print(f"{word:<{size}}")
    elif dis == "right":
        print(f"{word:>{size}}")
    elif dis == "center":
        ans = (" "*int(left))+(word)+(" "*int(right))
        print(ans)
main()
