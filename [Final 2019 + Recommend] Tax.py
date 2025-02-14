"""[Final 2019 + Recommend] Tax"""
def main(y,cc):
    """[Final 2019 + Recommend] Tax"""
    if cc > 1800:
        ans = 2100 + (cc - 1800)*4
    elif cc > 600:
        ans = 300 + (cc - 600)*1.5
    else:
        ans = cc * 0.5
    if y >= 10:
        print(f"{ans*0.5:.2f}")
    elif y >= 9:
        print(f"{ans*0.6:.2f}")
    elif y >= 8:
        print(f"{ans*0.7:.2f}")
    elif y >= 7:
        print(f"{ans*0.8:.2f}")
    elif y >= 6:
        print(f"{ans*0.9:.2f}")
    else:
        print(f"{ans:.2f}")
main(float(input()),float(input()))
