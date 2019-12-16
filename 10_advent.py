import math

f = open("10_input.txt", "r")
inp = f.read().splitlines()
f.close()
asteroids = []

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "#":
            asteroids.append((i, j))


most_detected = 0

for asteroid in asteroids:
    directions = set()
    for station in asteroids:
        if asteroid == station:
            continue

        vec = (asteroid[0] - station[0], asteroid[1] - station[1])
        gcd = math.gcd(vec[0], vec[1])
        vec = (vec[0] // gcd, vec[1] // gcd)

        directions.add(vec)

    if len(directions) > most_detected:
        most_detected = len(directions)

print("Part 1: " + str(most_detected))