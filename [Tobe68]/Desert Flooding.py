"""Desert Flooding"""
def main(s,x,y):
    """main"""
    l = ((int(x)**2)+(int(y)**2))**0.5
    area = (3.14159*l*l)/s
    print(int(area))
main(int(input()),int(input()),int(input()))
