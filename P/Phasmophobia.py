"""Phasmophobia"""
def find(a):
    """find"""
    lis = []
    if a.issubset({"EMF Level 5","Fingerprints","Freezing Temperatures"}):
        lis.append("Banshee")
    if a.issubset({"Ghost Writing","Spirit Box","Freezing Temperatures"}):
        lis.append("Demon")
    if a.issubset({"EMF Level 5","Spirit Box","Ghost Orb"}):
        lis.append("Jinn")
    if a.issubset({"Freezing Temperatures","Spirit Box","Ghost Orb"}):
        lis.append("Mare")
    if a.issubset({"EMF Level 5","Spirit Box","Ghost Writing"}):
        lis.append("Oni")
    if a.issubset({"Freezing Temperatures","EMF Level 5","Ghost Orb"}):
        lis.append("Phantom")
    if a.issubset({"Fingerprints","Spirit Box","Ghost Orb"}):
        lis.append("Poltergeist")
    if a.issubset({"EMF Level 5","Fingerprints","Ghost Writing"}):
        lis.append("Revenant")
    if a.issubset({"EMF Level 5","Ghost Orb","Ghost Writing"}):
        lis.append("Shade")
    if a.issubset({"Spirit Box","Fingerprints","Ghost Writing"}):
        lis.append("Spirit")
    if a.issubset({"Spirit Box","Fingerprints","Freezing Temperatures"}):
        lis.append("Wraith")
    if a.issubset({"Freezing Temperatures","Ghost Writing","Ghost Orb"}):
        lis.append("Yurei")
    lis.sort(key=lambda x:x[0])
    return lis
def main(ev1,ev2,ev3):
    """main"""
    se = set()
    if ev1 != "No evidence":
        se.add(ev1)
    if ev2 != "No evidence":
        se.add(ev2)
    if ev3 != "No evidence":
        se.add(ev3)
    if find(se):
        print(*find(se),sep="\n")
    else:
        print("Not yet discovered")
main(input(),input(),input())
