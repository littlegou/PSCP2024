"""Timing II"""
def main(time):
    """main"""
    day = time//86400
    if len(str(day))>4:
        print("ERR_:__:__:__")
    else:
        hr = time%86400
        hour = hr//3600
        mi = hr%3600
        minute = mi//60
        sec = mi%60
        print(f"{day:>04}:{hour:>02}:{minute:>02}:{sec:>02}")
main(int(input()))
