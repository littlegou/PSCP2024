"""Bonus"""
def main(salary,year,month):
    """main"""
    if month>=10:
        year += 1
    if year>20:
        year = 20
    ans = salary*year
    if ans<5000:
        ans = 5000
    elif ans>1000000:
        ans = 1000000
    print(ans)
main(int(input()),int(input()),int(input()))
