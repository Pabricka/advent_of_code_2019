def validate1(password):
    last = ""
    increasing = True
    double = False
    for c in password:
        if c < last:
            increasing = False
            break
        if c == last:
            double = True
        last = c
    if double and increasing:
        return True
    else:
        return False


def validate2(password):
    last = ""
    increasing = True
    double = False
    counter = 1
    for c in password:
        if c < last:
            increasing = False
            break
        if c == last:
            counter += 1
        else:
            if counter == 2:
                double = True
            counter = 1
        last = c
    if counter == 2:
        double = True
    if double and increasing:
        return True
    else:
        return False


minimum = 146810
maximum = 612564

part1 = 0
for i in range(minimum, maximum):
    if validate1(str(i)):
        part1 += 1
print("Part 1: " + str(part1))

part2 = 0
for i in range(minimum, maximum):
    if validate2(str(i)):
        part2 += 1
print("Part 2: " + str(part2))
