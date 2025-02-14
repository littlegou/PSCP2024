"""BTSMRT"""
def main(day,age,height):
    """main"""
    if (age<14 and height<90) or (day == "Children Day" and age<14 and height<=140):
        print("FREE")
    elif day == "Senior Day" and age>=60:
        print("FREE")
    else:
        print("PAY")
main(input(),float(input()),float(input()))
