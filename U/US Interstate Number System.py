"""US Interstate Number System"""
def main(highway):
    """main"""
    if highway<100:
        if not highway%10 and highway:
            print("Horizontal Major Interstate")
            print(f"I-{highway}")
        elif highway%10 == 5:
            print("Vertical Major Interstate")
            print(f"I-{highway}")
        else:
            print("Others")
    elif highway<1000:
        if not (highway//100)%2 and highway and ((not highway%10 and highway%100)or highway%10==5):
            print("Even Minor Interstate")
            print(f"I-{highway%100}")
        elif (highway//100)%2 and ((not highway%10 and highway%100) or highway%10 == 5):
            print("Odd Minor Interstate")
            print(f"I-{highway%100}")
        else:
            print("Others")
    else:
        print("Others")
main(int(input()))
