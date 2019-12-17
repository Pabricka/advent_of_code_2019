import copy
import math
f = open("12_input.txt", "r")
inp = f.read().splitlines()
f.close()

moons = []
velocities = []
for line in inp:
    x = ""
    y = ""
    z = ""
    c = 3
    while line[c].isdigit() or line[c] == "-":
        x += line[c]
        c += 1
    c += 4
    while line[c].isdigit() or line[c] == "-":
        y += line[c]
        c += 1
    c += 4
    while line[c].isdigit() or line[c] == "-":
        z += line[c]
        c += 1

    moons.append([int(x), int(y), int(z)])
    velocities.append([0, 0, 0])


def simulate(moons, velocities):
    for i in range(len(moons)):
        for j in range(i+1, len(moons)):
            if moons[i][0] > moons[j][0]:
                velocities[i][0] -= 1
                velocities[j][0] += 1
            elif moons[i][0] < moons[j][0]:
                velocities[i][0] += 1
                velocities[j][0] -= 1
            if moons[i][1] > moons[j][1]:
                velocities[i][1] -= 1
                velocities[j][1] += 1
            elif moons[i][1] < moons[j][1]:
                velocities[i][1] += 1
                velocities[j][1] -= 1
            if moons[i][2] > moons[j][2]:
                velocities[i][2] -= 1
                velocities[j][2] += 1
            elif moons[i][2] < moons[j][2]:
                velocities[i][2] += 1
                velocities[j][2] -= 1
        moons[i][0] += velocities[i][0]
        moons[i][1] += velocities[i][1]
        moons[i][2] += velocities[i][2]


def lcm(a, b):
    return (a*b)//math.gcd(a, b)

step = 0
og_moons = copy.deepcopy(moons)
og_velocities = copy.deepcopy(velocities)
while step < 1000:
    simulate(moons, velocities)
    step += 1

energy = 0

for i, m in enumerate(moons):
    pot = abs(m[0]) + abs(m[1]) + abs(m[2])
    kin = abs(velocities[i][0]) + abs(velocities[i][1]) + abs(velocities[i][2])
    energy += pot * kin

print("Part 1: " + str(energy))

steps_to_repeat = [0, 0, 0]

for i in range(3):
    moons = copy.deepcopy(og_moons)
    velocities = copy.deepcopy(og_velocities)
    step = 0
    seen = set()
    while True:
        state = []
        simulate(moons, velocities)
        for j, m in enumerate(moons):
            state.append(m[i])
            state.append(velocities[j][i])
        state = str(state)
        if state in seen:
            print("Found repeat period for axis " + str(i) + " which is " + str(step))
            steps_to_repeat[i] = step
            break

        seen.add(state)
        step += 1

print("Part 2: " + str(lcm(lcm(steps_to_repeat[0], steps_to_repeat[1]), steps_to_repeat[2])))
