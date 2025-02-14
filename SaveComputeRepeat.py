"""SCR"""
def main():
    """main"""
    start_here = 492137954293754252786
    miliseconds = start_here
    sec = miliseconds//1000
    miliseconds = miliseconds%1000
    minu = sec//60
    sec = sec%60
    hours = minu//60
    minu = minu%60
    days = hours//24
    hours = hours%24
    print (f"{days} {hours} {minu} {sec} {miliseconds}")
main()
