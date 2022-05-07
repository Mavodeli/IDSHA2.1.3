def MakePrettyRaw():
    arr = []
    possible3bit = []
    for x in range(0,8):
        possible3bit.append(format(x, '03b'))
    for x in range(0,2):
        for temp in possible3bit:
            for temp2 in possible3bit:
                arr.append(str(x) + " " + temp + " " + temp2)
    return arr

def MakePrettyFiltered():
    arr = []
    possible3bit = []
    for x in range(0,8):
        possible3bit.append(format(x, '03b'))
    for x in range(0,2):
        for temp in possible3bit[:-1]:
            for temp2 in possible3bit:
                arr.append(str(x) + " " + temp + " " + temp2)
    return arr

def MakeRawFiltered():
    arr = []
    possible3bit = []
    for x in range(0,8):
        possible3bit.append(format(x, '03b'))
    for x in range(0,2):
        for temp in possible3bit[:-1]:
            for temp2 in possible3bit:
                arr.append(str(x) + temp + temp2)
    return arr

def binToDec(input):
    return int(input , 2)

def calculateIEEE754(input):
    ebits = 3
    mbits = 3
    offset = (2 ** (ebits - 1)) - 1
        
    expobits = input[1:(ebits + 1)]
    mantisbits = input[(ebits + 1):(ebits + mbits + 1)]
    
    sign = (-1) ** int(input[0])
    expo = binToDec(expobits) - offset
    mantis = 1 + (binToDec(mantisbits) / (2 ** mbits))

    result = sign * mantis * (2 ** expo)
    return str(result)

lines = []
lines.append("Erstes fancy Output:")
for line in MakePrettyRaw():
    lines.append(line)
lines.append("Gefiltertes (ohne NaN und +/- Unendlich) fancy Output:")
for line in MakePrettyFiltered():
    lines.append(line)
lines.append("Gefiltertes (ohne NaN und +/- Unendlich) rohes Output:")
for line in MakeRawFiltered():
    lines.append(line)
lines.append("Dezimalwert der gefilterten (ohne NaN und +/- Unendlich) IEEE754 Zahlen:")
for line in MakeRawFiltered():
    lines.append(calculateIEEE754(line))
lines.append("Hier nochmal mit , statt . :")
for line in MakeRawFiltered():
    lines.append(calculateIEEE754(line).replace(".", ","))


with open('output.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')