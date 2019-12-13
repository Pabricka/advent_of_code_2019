f = open("6_input.txt", "r")
input = f.read().splitlines()
f.close()


class Object:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
    dist = None


def checksum(object):
    for o in objects:
        if object.parent == o.name:
            if o.dist is None:
                t = checksum(o)
                o.dist = t
                return t + 1
            else:
                return o.dist + 1
    return 1


def parents(object):
    par = []
    for o in objects:
        if object.parent == o.name:
            par.append(o.name)
            l = parents(o)
            if l is not None:
                return l + par
            else:
                return par

objects = []
for obj in input:
    objs = obj.split(")")
    objects.append(Object(objs[1], objs[0]))

total = 0
for o in objects:
    total += checksum(o)
print("Part 1: " + str(total))

visited = []
you = next(o for o in objects if o.name == "YOU")
san = next(o for o in objects if o.name == "SAN")
youparents = parents(you)
sanparents = parents(san)
i = 0
while youparents[i] == sanparents[i]:
    i += 1
print("Part 2: " + str(len(youparents)-i + len(sanparents)-i))