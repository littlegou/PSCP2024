"""B - Fully pair?"""
def main(sen):
    """main"""
    yo = ""
    for i in sen:
        if sen.count(i) % 2 and i not in yo:
            yo += i
    if not yo:
        print("fully paired")
    else:
        print(yo)
main(input())
