"""PlanB"""
def main(score):
    """main"""
    if score>=450:
        print("Pass")
    elif score<450:
        print("Fail")
    print("Process is terminated")
main(float(input()))
