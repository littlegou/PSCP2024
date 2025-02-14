"""Alcohol"""
def main():
    """Alcohol"""
    s = input()
    w = float(input())
    car = input()
    drink = float(input())
    alc = float(input())*0.01
    can = float(input())
    hr = int(input())
    ans = 0
    if s == "Male":
        ans = (alc*drink*can)/(w*0.68*10)
    elif s == "Female":
        ans = (alc*drink*can)/(w*0.55*10)
    if (ans*1000)-(hr*15)>50 or car == "No":
        print("Not Safe")
    else:
        print("Safe")
main()
