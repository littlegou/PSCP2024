"""[Midterm 2024] Coffee Shop"""
def main(price,disone,distwo,protwo,need):
    """main"""
    one = price + (need-1)*(price*(1-(disone/100)))
    two = price*need
    if two>=protwo:
        two = (1-(distwo/100)) * two
    if one<two:
        print(1)
        print(f"{one:.2f}")
    else:
        print(2)
        print(f"{two:.2f}")
main(float(input()),float(input()),float(input()),float(input()),int(input()))
