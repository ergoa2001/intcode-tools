from itertools import permutations
import time

with open("intcode.txt") as fp:
    originaldata = fp.read().strip().split(",")

data = originaldata[:]

def readvalue(position):
    if position >= len(data):
        for x in range(1, position + 1):
            data.append("0")
    value = data[position]
    return value

def writevalue(value, position):
    if position >= len(data):
        for x in range(1, position + 1):
            data.append("0")
    data[position] = value

def intpc():
    relativebase = 0
    pos = 0

    while data[pos] != "99":
        tempopcode = data[pos]
        opcode = tempopcode[-2:]
        param1 = tempopcode[-3:-2]
        param2 = tempopcode[-4:-3]
        param3 = tempopcode[-6:-4]
        #DEBUG
        #print(opcode, param1, param2, param3, "relativebase = ", relativebase, pos)

        if opcode == "1":
            sum = int(readvalue(int(data[pos+1]))) + int(readvalue(int(data[pos+2])))
            writevalue(str(sum), int(data[pos+3]))
            pos += 4

        elif opcode == "01":
            if param1 == "0" or param1 == "":
                num1 = int(readvalue(int(data[pos+1])))
            elif param1 == "1":
                num1 = int(data[pos+1])
            elif param1 == "2":
                num1 = int(readvalue(int(data[pos+1]) + relativebase))
            else:
                print("Incorrect parameter", param1)

            if param2 == "0" or param2 == "":
                num2 = int(readvalue(int(data[pos+2])))
            elif param2 == "1":
                num2 = int(data[pos+2])
            elif param2 == "2":
                num2 = int(readvalue(int(data[pos+2]) + relativebase))
            else:
                print("Incorrect parameter", param2)

            if param3 == "2":
                writepos = int(data[pos+3]) + relativebase
            else:
                writepos = int(data[pos+3])

            sum = num1 + num2
            writevalue(str(sum), writepos)
            pos += 4

        elif opcode == "2":
            sum = int(readvalue(int(data[pos+1]))) * int(readvalue(int(data[pos+2])))
            writevalue(str(sum), int(data[pos+3]))
            pos += 4

        elif opcode == "02":
            if param1 == "0" or param1 == "":
                num1 = int(readvalue(int(data[pos+1])))
            elif param1 == "1":
                num1 = int(data[pos+1])
            elif param1 == "2":
                num1 = int(readvalue(int(data[pos+1]) + relativebase))
            else:
                print("Incorrect parameter", param1)

            if param2 == "0" or param2 == "":
                num2 = int(readvalue(int(data[pos+2])))
            elif param2 == "1":
                num2 = int(data[pos+2])
            elif param2 == "2":
                num2 = int(readvalue(int(data[pos+2]) + relativebase))
            else:
                print("Incorrect parameter", param2)

            if param3 == "2":
                writepos = int(data[pos+3]) + relativebase
            else:
                writepos = int(data[pos+3])

            sum = num1 * num2
            writevalue(str(sum), writepos)
            pos += 4

        elif opcode == "3":
            writedata = input("Integer input: ")
            writevalue(writedata, int(data[pos+1]))
            pos += 2

        elif opcode == "03":
            if param1 == "0":
                writepos = int(data[pos+1])
            if param1 == "2":
                writepos = int(data[pos+1]) + relativebase

            writedata = input("Integer input: ")
            writevalue(writedata, writepos)
            pos += 2

        elif opcode == "4":
            outputdata = readvalue(int(data[pos+1]))
            print(chr(int(outputdata)), end ="")
            pos += 2

        elif opcode == "04":
            if param1 == "0":
                readpos = int(data[pos+1])
                outputdata = readvalue(readpos)
            elif param1 == "1":
                readpos = pos+1
                outputdata = data[readpos]
            elif param1 == "2":
                readpos = int(data[pos+1]) + relativebase
                outputdata = readvalue(readpos)
            else:
                print("Incorrect parameter", param1)
            print(chr(int(outputdata)), end ="")
            pos += 2

        elif opcode == "5":
            if readvalue(int(data[int(data[pos+1])])) != "0":
                pos = int(data[int(data[pos+2])])
            else:
                pos += 3

        elif opcode == "05":
            if param1 == "0" or param1 == "":
                checknum = readvalue(int(data[pos+1]))
            elif param1 == "1":
                checknum = data[pos+1]
            elif param1 == "2":
                checknum = readvalue(int(data[pos+1]) + relativebase)
            else:
                print("Incorrect parameter", param1)

            if param2 == "0" or param2 == "":
                gopos = int(data[int(data[pos+2])])
            elif param2 == "1":
                gopos = int(data[pos+2])
            elif param2 == "2":
                gopos = int(data[int(data[pos+2]) + relativebase])
            else:
                print("Incorrect parameter", param2)

            if checknum != "0":
                pos = gopos
            else:
                pos += 3

        elif opcode == "6":
            if readvalue(int(data[pos+1])) == "0":
                pos = int(data[int(data[pos+2])])
            else:
                pos += 3

        elif opcode == "06":
            if param1 == "0" or param1 == "":
                checknum = readvalue(int(data[pos+1]))
            elif param1 == "1":
                checknum = data[pos+1]
            elif param1 == "2":
                checknum = readvalue(int(data[pos+1]) + relativebase)
            else:
                print("Incorrect parameter", param1)

            if param2 == "0" or param2 == "":
                gopos = int(data[int(data[pos+2])])
            elif param2 == "1":
                gopos = int(data[pos+2])
            elif param2 == "2":
                gopos = int(data[int(data[pos+2]) + relativebase])
            else:
                print("Incorrect parameter", param2)

            if checknum == "0":
                pos = gopos
            else:
                pos += 3

        elif opcode == "7":
            if int(readvalue(int(data[pos+1]))) < int(readvalue(int(data[pos+2]))):
                writevalue("1", int(data[pos+3]))
            else:
                writevalue("0", int(data[pos+3]))
            pos += 4

        elif opcode == "07":
            if param1 == "0" or param1 == "":
                num1 = int(readvalue(int(data[pos+1])))
            elif param1 == "1":
                num1 = int(data[pos+1])
            elif param1 == "2":
                num1 = int(readvalue(int(data[pos+1]) + relativebase))
            else:
                print("Incorrect parameter", param1)

            if param2 == "0" or param2 == "":
                num2 = int(readvalue(int(data[pos+2])))
            elif param2 == "1":
                num2 = int(data[pos+2])
            elif param2 == "2":
                num2 = int(readvalue(int(data[pos+2]) + relativebase))
            else:
                print("Incorrect parameter", param2)

            if param3 == "2":
                writepos = int(data[pos+3]) + relativebase
            else:
                writepos = int(data[pos+3])

            if num1 < num2:
                writevalue("1", writepos)
            else:
                writevalue("0", writepos)
            pos += 4

        elif opcode == "8":
            if int(readvalue(int(data[pos+1]))) == int(readvalue(int(data[pos+2]))):
                writevalue("1", int(data[pos+3]))
            else:
                writevalue("0", int(data[pos+3]))
            pos += 4

        elif opcode == "08":
            if param1 == "0" or param1 == "":
                num1 = int(readvalue(int(data[pos+1])))
            elif param1 == "1":
                num1 = int(data[pos+1])
            elif param1 == "2":
                num1 = int(readvalue(int(data[pos+1]) + relativebase))
            else:
                print("Incorrect parameter", param1)

            if param2 == "0" or param2 == "":
                num2 = int(readvalue(int(data[pos+2])))
            elif param2 == "1":
                num2 = int(data[pos+2])
            elif param2 == "2":
                num2 = int(readvalue(int(data[pos+2]) + relativebase))
            else:
                print("Incorrect parameter", param2)

            if param3 == "2":
                writepos = int(data[pos+3]) + relativebase
            else:
                writepos = int(data[pos+3])

            if num1 == num2:
                writevalue("1", writepos)
            else:
                writevalue("0", writepos)
            pos += 4

        elif opcode == "9":
            relativebase += int(data[int(data[pos+1])])
            pos += 2

        elif opcode == "09":
            if param1 == "0" or param1 == "":
                relativebase += int(data[int(data[pos+1])])
            elif param1 == "1":
                relativebase += int(data[pos+1])
            elif param1 == "2":
                relativebase += int(data[int(data[pos+1]) + relativebase])
            else:
                print("Incorrect parameter", param1)
            pos += 2
        else:
            print("Incorrect opcode")
    #DEBUG
        #time.sleep(0.5)
        #print(" ".join(data))
        #print(pos)
intpc()
