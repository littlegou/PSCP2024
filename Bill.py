"""Bill"""
def main():
    """main"""
    f = int(input())
    if f*0.10>1000:
        print(f"{(f+1000)*1.07:.2f}")
    elif f*0.10<50:
        print(f"{(f+50)*1.07:.2f}")
    else:
        print(f"{(f*1.1)*1.07:.2f}")
main()
