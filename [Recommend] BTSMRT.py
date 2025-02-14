"""[Recommend] BTSMRT"""
def main(day,age,height):
    """main"""
    if (day == "Children Day" and height<=140 and age<14) or (day == "Senior Day" and age>=60):
        print("FREE")
    elif height<90 and age <14:
        print("FREE")
    else:
        print("PAY")
main(input(),float(input()),float(input()))
