"""[ Day 2 ] GMT"""
from datetime import datetime, timedelta
def main(timenow,gmtnow,gmtneed):
    timenow = timenow.replace("A.M.", "AM").replace("P.M.", "PM")
    timenow = datetime.strptime(timenow, "%I:%M %p")
    gmtdiff = gmtneed - gmtnow
    timediff = timedelta(hours=int(gmtdiff),minutes=float(f"{gmtdiff-int(gmtdiff):.2f}")*100)
    ans = timenow + timediff
    ans = ans.strftime("%I:%M %p")
    ans = ans.replace("AM", "A.M.").replace("PM", "P.M.")
    print(ans)
main(input(),float(input()),float(input()))
