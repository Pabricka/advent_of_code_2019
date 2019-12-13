from PIL import Image

f = open("8_input.txt", "r")
input = f.read().splitlines()
input = input[0]
f.close()


layers = [[]]
digits = []
wide = 0
tall = 0

layers[len(layers) - 1].append([])
digits.append([0, 0, 0])
for c in input:
    digit = int(c)

    if wide < 25:
        layers[len(layers)-1][tall].append(digit)
        digits[len(layers)-1][digit] += 1
        wide += 1
    else:
        if tall < 5:
            tall += 1
            wide = 0
        else:
            layers.append([])
            tall = 0
            wide = 0
        layers[len(layers) - 1].append([])
        digits.append([0, 0, 0])
        layers[len(layers)-1][tall].append(digit)
        digits[len(layers)-1][digit] += 1
        wide += 1

fewest = digits[0][0]
index = 0
for i in range(len(layers)-1):
    if digits[i][0] < fewest:
        fewest = digits[i][0]
        index = i

print("Part 1: " + str(digits[index][1] * digits[index][2]))

print("Part 2:")
img = Image.new("RGB", (25, 6))
imgdata = []
for row in range(6):
    s = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    for col in range(25):
        for i in range(len(layers)):
            if s[col] == 2:
                digit = layers[i][row][col]
                s[col] = digit
    for c in s:
        if c == 0:
            imgdata.append((255, 255, 255, 1))
        elif c == 1:
            imgdata.append((0, 0, 0, 1))
        elif c == 2:
            imgdata.append((0, 0, 0, 0))
img.putdata(imgdata)
img.show()

