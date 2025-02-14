"""ClockHands"""
def main(hr,mn):
    """main"""
    if ((hr*5+(mn/60)*5) >= (mn%60)) and abs((hr*5+(mn/60)*5) - (mn%60)) <= 1%60:
        print(True)
        return
    print(False)
main(int(input()),int(input()))
