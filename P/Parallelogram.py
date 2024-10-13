"""Parallelogram"""
def main(sentence):
    """main"""
    x = len(sentence)
    for i in range(x-2,-2,-1):
        x = len(sentence)
        for j in range(x):
            if j < i+1:
                print(" ",end = "")
            else:
                print(sentence[-x],end = "")
                x-=1
        print()
    x = len(sentence)
    y = len(sentence)
    for i in range(y):
        if x!=1:
            print(sentence[-(x-1):])
            x-=1
        else:
            break
main(input())
