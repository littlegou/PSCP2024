"""BTU"""
def artwo(a):
    """area2"""
    if 1201 <= a <= 1400:
        return 23000
    if 1401 <= a <= 1500:
        return 24000
    if 1501 <= a <= 2000:
        return 30000
    if 2001 <= a <= 2500:
        return 34000
    return 0
def arone(a):
    """area1"""
    rec = 0
    if 100 <= a <= 150:
        rec = 5000
    elif 151 <= a <= 250:
        rec = 6000
    elif 251 <= a <= 300:
        rec = 7000
    elif 301 <= a <= 350:
        rec = 8000
    elif 351 <= a <= 400:
        rec = 9000
    elif 401 <= a <= 450:
        rec = 10000
    elif 451 <= a <= 550:
        rec = 12000
    elif 551 <= a <= 700:
        rec = 14000
    elif 701 <= a <= 1000:
        rec = 18000
    elif 1001 <= a <= 1200:
        rec = 21000
    else:
        rec = artwo(a)
    return rec
def main(area,height,ppl,room,sun):
    """BTU"""
    btu = arone(area)
    if height>8:
        btu += (height-8)*1000
    if ppl>2:
        btu += (ppl-2)*600
    if room == "kitchen":
        btu += 4000
    if sun == "facing the sun":
        btu *= 1.1
    elif sun == "shaded":
        btu *= 0.9
    print(int(btu))
main(int(input()),int(input()),int(input()),input(),input())
