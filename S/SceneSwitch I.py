"""SceneSwitch I"""
def main(n):
    """main"""
    cool = 2
    prev = 0
    count = 0
    while n != "End":
        ch = float(n) - prev
        if not cool and ch <= 6:
            count += 1
            cool = 3
        elif not cool and ch > 6:
            cool = 1
        elif cool >=1:
            cool -= 1
        prev = float(n)
        n = input()
    print(count)
main(input())
