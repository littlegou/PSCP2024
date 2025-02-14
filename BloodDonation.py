'''BloodDonation'''
def main():
    'pep8'
    age = int(input())
    wg = int(input())
    time = int(input())
    if age == 17 or 60 <= age <= 70:
        rub = input()
        if rub == 'True' and wg >= 45:
            if not time and age > 55:
                print('No')
            else:
                print('Yes')
        else:
            print('No')
    elif 18 <= age < 60 and wg >= 45:
        if not time and age > 55:
            print('No')
        else:
            print('Yes')
    else:
        print('No')
main()
