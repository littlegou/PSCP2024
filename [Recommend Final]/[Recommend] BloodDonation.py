"""[Recommend] BloodDonation"""
def main(a,w,t):
    """[Recommend] BloodDonation"""
    p = "True"
    if a == 17 or 60 <= a <= 70:
        p = input()
    if ((17 <= a <= 55) or (55 < a <= 70 and t)) and p == "True" and w >=45:
        print("Yes")
    else:
        print("No")
main(int(input()),int(input()),int(input()))
