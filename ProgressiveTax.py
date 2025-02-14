"""ProgressiveTax"""
import math
def fiveper(x):
    """5%"""
    return (x - 150000)*0.05
def tenper(x):
    """10%"""
    return ((x - 300000)*0.1)+7500
def fiftper(x):
    """15%"""
    return ((x - 500000)*0.15)+20000+7500
def tweper(x):
    """20%"""
    return ((x - 750000)*0.2)+37500+20000+7500
def twfper(x):
    """25%"""
    return ((x - 1000000)*0.25)+50000+37500+20000+7500
def ttper(x):
    """30%"""
    return ((x - 2000000)*0.3)+250000+50000+37500+20000+7500
def ttfper(x):
    """35%"""
    return ((x - 4000000)*0.35)+600000+250000+50000+37500+20000+7500
def main(income):
    """main"""
    if income>4000000:
        ans = math.floor(ttfper(income))
    elif income>2000000:
        ans = math.floor(ttper(income))
    elif income>1000000:
        ans = math.floor(twfper(income))
    elif income>750000:
        ans = math.floor(tweper(income))
    elif income>500000:
        ans = math.floor(fiftper(income))
    elif income>300000:
        ans = math.floor(tenper(income))
    elif income>150000:
        ans = math.floor(fiveper(income))
    else:
        ans = 0
    print(ans)
main(int(input()))
