"""[Midterm 2024] Digital"""
def main():
    """main"""
    name = input()
    checkn = input()
    checkh = input()
    age = float(input())
    income = float(input())
    bank = float(input())
    if checkn in ("True","Yes") and checkh in ("True","Yes") and age>=16 \
and income<=840000 and bank<=500000:
        print(f"Congratulations! {name} is qualified to receive a digital \
wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main()
