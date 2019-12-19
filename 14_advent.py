from collections import defaultdict
from math import ceil

f = open("14_input.txt", "r")
inp = f.read().splitlines()
f.close()

reactions = []
for line in inp:
    line = line.split(" ")
    amount = True
    required = []
    produced = ()
    pro = False
    for l in line:
        chemical = ""
        if amount:
            if l == "=>":
                pro = True
            else:
                units = int(l)
                amount = False
        else:
            chemical = l
            if l[len(l)-1] == ",":
                chemical = l[:len(l)-1]
            if not pro:
                required.append((units, chemical))
            else:
                produced = (units, chemical)
            amount = True
    reactions.append((required, produced))


def ores_to_produce(units, chemical, supply=None):
    if supply is None:
        supply = defaultdict(int)
    if chemical == "ORE":
        return units

    extra = min(units, supply[chemical])
    units -= extra
    supply[chemical] -= extra

    for r in reactions:
        if r[1][1] == chemical:
            reactions_needed = ceil(units / r[1][0])

            total_ore = 0
            for i in range(len(r[0])):
                total_ore += ores_to_produce(reactions_needed * r[0][i][0], r[0][i][1], supply)

            supply[chemical] += reactions_needed * r[1][0] - units

            return total_ore


print("Part 1: " + str(ores_to_produce(1, "FUEL")))
