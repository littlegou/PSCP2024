"""Ping"""
import math
def tt(ma,mi,ping):
    """smaller"""
    if not ma and not mi:
        ma = ping
        mi = ping
    else:
        if ping>ma:
            ma = ping
        if ping<mi:
            mi = ping
    return ma,mi
def firstrow(x):
    """findip"""
    if x.find("[")!=-1:
        q,w = x.find("["),x.find("]")
        ip = x[q+1:w]
    else:
        x = x.replace("Pinging ","")
        x = x.replace(" with 32 bytes of data:","")
        ip = x
    return ip
def secondrow(z,x,c,v):
    """find2ndrow"""
    count = 0
    noi = 0
    if z.find("ms") != -1:
        count += 1
    if x.find("ms") != -1:
        count += 1
    if c.find("ms") != -1:
        count += 1
    if v.find("ms") != -1:
        count += 1
    if z.find("<") != -1:
        noi += 1
    if x.find("<") != -1:
        noi += 1
    if c.find("<") != -1:
        noi += 1
    if v.find("<") != -1:
        noi += 1
    return count,noi
def fourthrow(z,x,c,v,b):
    """find4throw"""
    avg = 0
    maximum = 0
    minimum = 0
    if z.find("time") != -1 and z.find("ms") != -1:
        ping1 = int(z[z.find("time")+5:z.find("ms")])
        avg += ping1
        if ping1>maximum:
            maximum = ping1
            minimum = ping1
    if x.find("time") != -1 and x.find("ms") != -1:
        ping2 = int(x[x.find("time")+5:x.find("ms")])
        avg += ping2
        maximum,minimum = tt(maximum,minimum,ping2)
    if c.find("time") != -1 and c.find("ms") != -1:
        ping3 = int(c[c.find("time")+5:c.find("ms")])
        avg += ping3
        maximum,minimum = tt(maximum,minimum,ping3)
    if v.find("time") != -1 and v.find("ms") != -1:
        ping4 = int(v[v.find("time")+5:v.find("ms")])
        avg += ping4
        if ping4>maximum:
            maximum = ping4
        if ping4<minimum:
            minimum = ping4
    if b == 4:
        maximum = 0
        minimum = 0
        avg = 0
    elif 0<b<4:
        minimum = 0
        avg -= b
    return maximum,minimum,avg
def main():
    """main"""
    _ = input()
    _ = input()
    thr = input()
    fou = input()
    fiv = input()
    six = input()
    sev = input()
    a,c = secondrow(fou,fiv,six,sev)
    maxi,mini,av = fourthrow(fou,fiv,six,sev,c)
    print(f"Ping statistics for {firstrow(thr)}:")
    print(f"    Packets: Sent = 4, Received = {a}, Lost = {4-a} ({int((4-a)/4*100)}% loss),")
    if a:
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {mini}ms, Maximum = {maxi}ms, Average = {math.floor(av/a)}ms")
main()
