"""SurprisingVote"""
def main(al,hig):
    """main"""
    min1 = (al-hig)/2
    if isinstance(min1,float):
        min1 -= 0.5
    min2 = al-hig-hig
    mini = min(abs(min1),abs(min2))
    if hig-mini > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()),float(input()))
