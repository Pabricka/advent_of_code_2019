def run_opcodes(codes, inp1, inp2):
    index = 0
    first = True
    while codes[index] != 99:
        opcode = str(codes[index])
        inst = opcode[len(opcode)-1]
        parameters = ["0", "0", "0"]
        output = ""
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
            if first:
                val = inp1
                first = False
            else:
                val = inp2
            codes[codes[index+1]] = int(val)
            index += 2
        elif inst == "4":
            output = param1
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

    return output


class Amplifier:
    index = 0
    codes = None
    inp = None
    out = None
    next = None

    def __init__(self, codes, phase):
        self.codes = codes[:]
        self.phase = phase

    def setnext(self, next):
        self.next = next

    def run(self):
        codes = self.codes
        while self.codes[self.index] != 99:
            opcode = str(codes[self.index])
            inst = opcode[len(opcode) - 1]
            parameters = ["0", "0", "0"]
            for i in range(0, len(opcode) - 2):
                parameters[i] = opcode[len(opcode) - 3 - i]
            if self.index < len(codes) - 1:
                if parameters[0] == "0":
                    param1 = int(codes[codes[self.index + 1]])
                else:
                    param1 = int(codes[self.index + 1])
            if self.index < len(codes) - 2:
                if parameters[1] == "0":
                    if int(codes[self.index + 2]) < len(codes):
                        param2 = int(codes[codes[self.index + 2]])
                else:
                    param2 = int(codes[self.index + 2])
            if self.index < len(codes) - 4:
                param3 = codes[self.index + 3]
            if inst == "1":
                codes[param3] = param1 + param2
                self.index += 4
            elif inst == "2":
                codes[param3] = param1 * param2
                self.index += 4
            elif inst == "3":
                if self.phase is not None:
                    codes[codes[self.index + 1]] = int(self.phase)
                    self.phase = None
                    self.index += 2
                elif self.inp is not None:
                    codes[codes[self.index + 1]] = int(self.inp)
                    self.inp = None
                    self.index += 2
                else:
                    break
            elif inst == "4":
                self.out = param1
                self.index += 2
                self.next.inp = param1
                self.next.run()
            elif inst == "5":
                if param1 != 0:
                    self.index = param2
                else:
                    self.index += 3
            elif inst == "6":
                if param1 == 0:
                    self.index = param2
                else:
                    self.index += 3
            elif inst == "7":
                if param1 < param2:
                    codes[param3] = 1
                else:
                    codes[param3] = 0
                    self.index += 4
            elif inst == "8":
                if param1 == param2:
                    codes[param3] = 1
                else:
                    codes[param3] = 0
                    self.index += 4
            else:
                print("Error: Unknown opcode: " + inst + " at index " + str(self.index))
                return
        return self.out


f = open("7_input.txt", "r")
inp = f.read()
f.close()

intcodes = inp.split(",")
intcodes = list(map(int, intcodes))
maxSignal = 0

for a in range(5):
    for b in range(5):
        for c in range(5):
            for d in range(5):
                for e in range(5):
                    if not len({a, b, c, d, e}) < 5:
                        inp_copy = intcodes[:]
                        signal = 0
                        signal = run_opcodes(inp_copy, a, signal)
                        signal = run_opcodes(inp_copy, b, signal)
                        signal = run_opcodes(inp_copy, c, signal)
                        signal = run_opcodes(inp_copy, d, signal)
                        signal = run_opcodes(inp_copy, e, signal)

                        if signal > maxSignal:
                            maxSignal = signal
print("Part 1: " + str(maxSignal))

maxSignal = 0
for a in range(5, 10):
    for b in range(5, 10):
        for c in range(5, 10):
            for d in range(5, 10):
                for e in range(5, 10):
                    if not len({a, b, c, d, e}) < 5:
                        inp_copy = intcodes[:]
                        amplifier_a = Amplifier(inp_copy, a)
                        amplifier_b = Amplifier(inp_copy, b)
                        amplifier_c = Amplifier(inp_copy, c)
                        amplifier_d = Amplifier(inp_copy, d)
                        amplifier_e = Amplifier(inp_copy, e)

                        amplifier_a.setnext(amplifier_b)
                        amplifier_b.setnext(amplifier_c)
                        amplifier_c.setnext(amplifier_d)
                        amplifier_d.setnext(amplifier_e)
                        amplifier_e.setnext(amplifier_a)

                        amplifier_a.inp = 0
                        amplifier_a.run()
                        signal = amplifier_e.out
                        if signal > maxSignal:
                            maxSignal = signal

print("Part 2: " + str(maxSignal))
