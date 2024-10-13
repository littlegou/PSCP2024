"""[Recommend] Bill"""
def main(bill):
    """main"""
    if bill*0.1 <50:
        bill += 50
    elif bill * 0.1>1000:
        bill += 1000
    else:
        bill += bill*0.1
    print(f"{bill*1.07:.2f}")
main(int(input()))
