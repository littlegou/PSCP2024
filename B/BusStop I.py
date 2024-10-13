"""BusStop I"""
def main(ppl,busstop):
    """main"""
    bus = []
    count = 0
    lis = []
    for _ in range(busstop):
        lis.append(input())
    lis.sort(key=lambda x: int(x.split()[0]))
    for j in lis:
        j = j.split()
        check = int(j[0])
        wf = list(map(int, j[1:]))
        if check == 1:
            bus = wf[:ppl]
        else:
            for passenger in wf:
                if len(bus) < ppl and passenger>check:
                    bus.append(passenger)
        newbus = []
        for passenger in bus:
            if passenger == check+1:
                count += 1
            else:
                newbus.append(passenger)
        bus = newbus
    print(count)
main(int(input()), int(input()))
