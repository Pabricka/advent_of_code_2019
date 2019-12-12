f = open("5_input.txt", "r")
inp = f.read()
f.close()

intcodes = inp.split(",")
intcodes = list(map(int, intcodes))


def run_opcodes(codes):
    index = 0
    while codes[index] != 99:
        opcode = str(codes[index])
        inst = opcode[len(opcode)-1]
        parameters = ["0", "0", "0"]
        for i in range(0, len(opcode)-2):
            parameters[i] = opcode[len(opcode)-3-i]
        if index < len(codes)-1:
            if parameters[0] == "0":
                param1 = int(codes[codes[index + 1]])
            else:
                param1 = int(codes[index + 1])
        if index < len(codes)-2:
            if parameters[1] == "0":
                if int(codes[index + 2]) < len(codes):
                    param2 = int(codes[codes[index + 2]])
            else:
                param2 = int(codes[index + 2])
        if index < len(codes)-4:
            param3 = codes[index + 3]
        if inst == "1":
            codes[param3] = param1 + param2
            index += 4
        elif inst == "2":
            codes[param3] = param1 * param2
            index += 4
        elif inst == "3":
            val = input("Input:")
            codes[codes[index+1]] = int(val)
            index += 2
        elif inst == "4":
            print("Output: " + str(param1))
            index += 2
        elif inst == "5":
            if param1 != 0:
                index = param2
            else:
                index += 3
        elif inst == "6":
            if param1 == 0:
                index = param2
            else:
                index += 3
        elif inst == "7":
            if param1 < param2:
                codes[param3] = 1
            else:
                codes[param3] = 0
            index += 4
        elif inst == "8":
            if param1 == param2:
                codes[param3] = 1
            else:
                codes[param3] = 0
            index += 4
        else:
            print("Error: Unknown opcode: " + inst + " at index " + str(index))
            return

    return codes


run_opcodes(intcodes)
