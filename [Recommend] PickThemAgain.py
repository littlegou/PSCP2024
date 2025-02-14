"""[Recommend] PickThemAgain"""
def main(lis):
    """[Recommend] PickThemAgain"""
    check = 0
    for i in lis:
        if not int(i) % 3 or not int(i)%5:
            print(i)
            check += 1
    if not check:
        print("Nope")
main(input().split()[::-1])
