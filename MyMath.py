"""MyMath"""
import math
def main():
    """main"""
    print((math.sin(math.radians(90))+(math.sin(math.radians(60)))**2)/\
    (math.cos(math.radians(245*245))+math.cos(math.radians(45+135))))
    print (math.factorial(16)*math.factorial(4)/math.factorial(8))
    print((15+25)/((25-12)**2+(12-15)**2)**(1/2))
    print(math.log((1234**4),10))
    print((math.log(4234,5)+math.log(8191,2)+71*math.log(156154,10))/\
    (math.log(777,7)-math.log(888,8)-math.log(999,9)))
main()
