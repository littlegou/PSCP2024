"""WordSequence II"""
def main(first,sec):
    """main"""
    for i in range(max(len(first),len(sec))+1):
        print(sec[:i]+first[i:])
main(input(),input())
