"""[Recommend] Grade III"""
def scor(x):
    """find"""
    grade = 0
    if x>=95:
        grade =  4
    elif x>=90:
        grade =  3.5
    elif x>=85:
        grade =  3
    elif x>=80:
        grade =  2.5
    elif x>=75:
        grade =  2
    elif x>=70:
        grade =  1.5
    elif x>=65:
        grade =  1
    elif x>=60:
        grade =  0.5
    elif x>=80:
        grade =  2.5
    else:
        grade = 0
    return grade
def main(n):
    """main"""
    sumgrade = 0
    for _ in range(n):
        sumgrade += float(scor(float(input())))
    sumgrade = int(sumgrade/n * 100)
    print(f"{sumgrade/100:.2f}")
main(int(input()))
