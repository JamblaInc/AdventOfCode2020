assemblyInput = [line.strip('\n') for line in open("input.txt", "r")]
instructions = {}
accumulator = 0
prevInstruction = 0

for index, x in enumerate(assemblyInput):
    temp = {}
    temp['instruction'], temp['value'] = x.split()
    temp['visited'] = False
    instructions[index] = temp


def getAccum(instruction):
    global accumulator

    if instructions[instruction]['visited'] is True:
        print('Accumulator: ', accumulator, 'Instruction: ', instruction)
    else:
        instructions[instruction]['visited'] = True
        if instructions[instruction]['instruction'] == 'acc':
            # ACC
            if instructions[instruction]['value'][0] == '+':
                accumulator += int(instructions[instruction]['value'][1:])
                evalInstruction(instruction+1)
            else:
                accumulator -= int(instructions[instruction]['value'][1:])
                evalInstruction(instruction+1)
        elif instructions[instruction]['instruction'] == 'jmp':
            # JMP
            if instructions[instruction]['value'][0] == '+':
                evalInstruction(
                    instruction+int(instructions[instruction]['value'][1:]))
            else:
                evalInstruction(
                    instruction-int(instructions[instruction]['value'][1:]))
        else:
            # NOP
            evalInstruction(instruction+1)


def evalInstruction(instruction):
    global prevInstruction

    if instructions[instruction]['visited'] is True:
        if instructions[prevInstruction]['instruction'] == 'jmp':
            # Change to NOP
            instructions[prevInstruction]['instruction'] == 'nop'
        elif instructions[prevInstruction]['instruction'] == 'nop':
            # Change to JMP
            instructions[prevInstruction]['instruction'] == 'jmp'
        print(f"changing instruction {prevInstruction}")
        instructions[instruction]['visited'] = False
        instructions[prevInstruction]['visited'] = False
        resetVisited()

    else:
        instructions[instruction]['visited'] = True
        if instructions[instruction]['instruction'] == 'acc':
            # ACC
            if instructions[instruction]['value'][0] == '+':
                evalInstruction(instruction+1)
            else:
                evalInstruction(instruction+1)
        elif instructions[instruction]['instruction'] == 'jmp':
            # JMP
            prevInstruction = instruction
            if instructions[instruction]['value'][0] == '+':
                evalInstruction(
                    instruction+int(instructions[instruction]['value'][1:]))
            else:
                evalInstruction(
                    instruction-int(instructions[instruction]['value'][1:]))
        else:
            # NOP
            prevInstruction = instruction
            evalInstruction(instruction+1)


def resetVisited():
    for key in instructions:
        instructions[key]['visited'] = False


evalInstruction(0)


getAccum(0)
print(accumulator, prevInstruction)
