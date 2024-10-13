"""[Mock Midterm 2022] Palindrome"""
def main(n,time):
    """main"""
    hr = int(time[:-3])
    mi = int(time[-2:])
    count = 0
    while count!=n:
        for _ in range(60):
            if mi + 1 >= 60:
                hr = (hr + 1)%24
            mi = (mi + 1)%60
            if hr == 24 and not mi:
                hr,mi = 0,00
            a = str(hr)+f"{mi:>02}"
            if a == a[::-1]:
                count += 1
                print(str(hr)+":"+f"{mi:>02}")
            if count == n:
                break
main(int(input()),input())
