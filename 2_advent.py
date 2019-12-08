f = open("2_input.txt", "r")
input = f.read()
f.close()

intcodes = input.split(",")
intcodes = list(map(int, intcodes))

def run_opcodes(codes):
    index = 0
    while codes[index] != 99:
        if codes[index] == 1:
            codes[codes[index + 3]] = codes[codes[index+1]] + codes[codes[index+2]]
        elif codes[index] == 2:
            codes[codes[index + 3]] = codes[codes[index+1]] * codes[codes[index+2]]
        else:
            print("Error: Unknown opcode")
            return
        index += 4
    return codes


def find_verb_and_noun(codes):
    for i in range(0, 99):
        for j in range(0, 99):
            codes_copy = codes.copy()
            codes_copy[1] = i
            codes_copy[2] = j
            answer = run_opcodes(codes_copy)
            if answer[0] == 19690720:
                return 100 * i + j
    return "Not found"


intcodes[1] = 12
intcodes[2] = 2
print("Part 1: " + str(run_opcodes(intcodes)[0]))
intcodes = input.split(",")
intcodes = list(map(int, intcodes))
print("Part 2: " + str(find_verb_and_noun(intcodes)))

