from PIL import Image

f = open("11_input.txt", "r")
inp = f.read()
f.close()

intcodes = inp.split(",")
intcodes = list(map(int, intcodes))

print(intcodes)


def run_opcodes(codes):

    inp_given = False
    codes += [0] * 100000
    index = 0
    relativebase = 0

    panels = [[0]*100 for i in range(100)]
    position_x = 50
    position_y = 50
    visited = {(position_x, position_y)}
    paint = True
    direction = 0

    while codes[index] != 99:
        opcode = str(codes[index])
        inst = opcode[len(opcode)-1]
        parameters = ["0", "0", "0"]
        for i in range(0, len(opcode)-2):
            parameters[i] = opcode[len(opcode)-3-i]
        if index < len(codes)-1:
            if parameters[0] == "0":
                param1 = int(codes[codes[index + 1]])
            elif parameters[0] == "1":
                param1 = int(codes[index + 1])
            elif parameters[0] == "2":
                param1 = int(codes[relativebase + codes[index + 1]])
        if index < len(codes)-2:
            if parameters[1] == "0":
                if int(codes[index + 2]) < len(codes):
                    param2 = int(codes[codes[index + 2]])
            elif parameters[1] == "1":
                param2 = int(codes[index + 2])
            elif parameters[1] == "2":
                param2 = int(codes[codes[index + 2] + relativebase])
        if index < len(codes)-3:
            if parameters[2] == "0":
                param3 = int(codes[index + 3])
            elif parameters[2] == "2":
                param3 = int(relativebase + codes[index + 3])
        if inst == "1":
            codes[param3] = param1 + param2
            index += 4
        elif inst == "2":
            codes[param3] = param1 * param2
            index += 4
        elif inst == "3":
            val = panels[position_y][position_x]
            if not inp_given:
                val = input("Starting color:")
                inp_given = True
            if parameters[0] == "0":
                codes[codes[index + 1]] = int(val)
            else:
                codes[relativebase + codes[index + 1]] = int(val)
            index += 2
        elif inst == "4":
            if paint:
                panels[position_y][position_x] = int(param1)
                visited.add((position_y, position_x))
                paint = False
            else:
                if param1 == 0:
                    direction -= 1
                    if direction < 0:
                        direction = 3
                else:
                    direction += 1
                    if direction > 3:
                        direction = 0
                if direction == 0:
                    position_y -= 1
                elif direction == 1:
                    position_x += 1
                elif direction == 2:
                    position_y += 1
                elif direction == 3:
                    position_x -= 1
                paint = True
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
        elif inst == "9":
            relativebase += param1
            index += 2
        else:
            print("Error: Unknown opcode: " + inst + " at index " + str(index))
            return
    print("Painted " + str(len(visited)) + " squares")
    return panels


panels = run_opcodes(intcodes)

print("Part 2:")

img = Image.new("RGB", (100, 100))
imgdata = []
for p in panels:
    for c in p:
        if c == 0:
            imgdata.append((255, 255, 255, 1))
        elif c == 1:
            imgdata.append((0, 0, 0, 1))
        elif c == 2:
            imgdata.append((0, 0, 0, 0))
img.putdata(imgdata)
img.show()
