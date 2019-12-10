f = open("3_input.txt", "r")
input = f.read().splitlines()
first = input[0].split(",")
second = input[1].split(",")
f.close()


def construct_wire(instructions):
    x = 0
    y = 0

    for path in instructions:
        direction = path[0]
        distance = int(path[1:len(path)])
        if direction == "U":
            for i in range(distance):
                y -= 1
                yield tuple([x, y])

        elif direction == "D":
            for i in range(distance):
                y += 1
                yield tuple([x, y])

        elif direction == "R":
            for i in range(distance):
                x += 1
                yield tuple([x, y])

        elif direction == "L":
            for i in range(distance):
                x -= 1
                yield tuple([x, y])


first_wire = list(construct_wire(first))
second_wire = list(construct_wire(second))

intersections = set(first_wire).intersection(set(second_wire))
print("Nearest at distance: " + str(min(abs(x)+abs(y) for (x, y) in intersections)))
steps = []
for intersect in intersections:
    steps.append(first_wire.index(intersect) + second_wire.index(intersect))

print("Least steps: " + str(min(steps) +2))