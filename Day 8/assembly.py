assemblyInput = [line.strip('\n') for line in open("input.txt", "r")]
instructions = {}
accumulator = 0

for index, x in enumerate(assemblyInput):
    temp = {}
    temp['instruction'], temp['value'] = x.split()
    temp['visited'] = False
    instructions[index] = temp


def evalInstruction(instruction):
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


evalInstruction(0)
