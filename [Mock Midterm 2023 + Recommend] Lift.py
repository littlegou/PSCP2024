"""Lift"""
def main(ppl,lift):
    """main"""
    mai = 0
    allw = 0
    gern = 0
    for _ in range(ppl):
        age = int(input())
        allw += float(input())
        if age<12:
            mai += 1
        elif age>=12:
            gern += 1
    if (mai>0 and gern>0) and allw<=lift:
        print("Safe")
    elif not mai and allw<=lift:
        print("Safe")
    else:
        print("Not Safe")
main(int(input()),float(input()))
