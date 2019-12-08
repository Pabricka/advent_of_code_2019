f = open("1_input.txt", "r")
input = f.read().splitlines()
f.close()


def sum_of_fuel_requirements(lines):
    answer = 0
    for i in lines:
        answer += int(int(i)/3)-2
    return answer


def sum_of_fuel_requirements2(lines):
    answer = 0
    for i in lines:
        answer += fuel_requirement(int(i))
    return answer


def fuel_requirement(mass):
    fuel = int((mass / 3)) - 2
    if fuel > 0:
        fuel += fuel_requirement(fuel)
    if fuel > 0:
        return fuel
    else:
        return 0


print("part 1: " + str(sum_of_fuel_requirements(input)))
print("part 2: " + str(sum_of_fuel_requirements2(input)))
