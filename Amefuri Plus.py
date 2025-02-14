"""Amefuri Plus"""
def check(x,y):
    """check"""
    if x == 1:
        print("Lost")
    elif x == 2:
        print("Dry")
    else:
        if not y:
            print("Dry")
        else:
            print(f"Still Wet (Wet Level: {y:.2f})")
def main(time,weather):
    """main"""
    cause = 0
    start = 8
    for i in weather.lower():
        if start<=0:
            cause = 2
            break
        if start >16:
            start = 16
        if i == "c" and 6<=time<18:
            start -= 0.5
        elif i == "n" and 6<=time<18:
            start -= 1
        elif i == "w" and 6<=time<18:
            start -= 1.5
        elif i == "c" and (0 <= time < 6 or 18 <= time <= 24):
            start -= 0.25
        elif i == "n" and (0 <= time < 6 or 18 <= time <= 24):
            start -= 0.5
        elif i == "w" and (0 <= time < 6 or 18 <= time <= 24):
            start -= 0.75
        elif i == "r":
            start += 2
        elif i == "s":
            start += 3
        elif i == "h":
            cause = 1
            break
        time = (time+1)%24
    check(cause,start)
main(int(input()),input())
