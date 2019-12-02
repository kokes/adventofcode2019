def compute(inp):
    opcodes = [int(j) for j in inp.split(',')]

    pos = 0
    while True:
        opc = opcodes[pos]
        if opc == 1:
            result = opcodes[opcodes[pos+1]] + opcodes[opcodes[pos+2]]
            opcodes[opcodes[pos+3]] = result
            pos += 4
        elif opc == 2:
            result = opcodes[opcodes[pos+1]] * opcodes[opcodes[pos+2]]
            opcodes[opcodes[pos+3]] = result
            pos += 4
        elif opc == 99:
            break
        else:
            raise ValueError(opc)

    return ','.join(map(str, opcodes))


def prep(inp, noun, verb):
    opcodes = [int(j) for j in inp.split(',')]
    opcodes[1] = noun
    opcodes[2] = verb
    return ','.join(map(str, opcodes))


tests = [
    ('1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50'),
    ('1,0,0,0,99', '2,0,0,0,99'),
    ('2,3,0,3,99', '2,3,0,6,99'),
    ('2,4,4,5,99,0', '2,4,4,5,99,9801'),
    ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'),
]

for inp, outp in tests:
    assert compute(inp) == outp

# -----
# TASK 1
with open('day2_data.txt') as f:
    inp = f.read()

result = compute(prep(inp, 12, 2))


print(result.partition(',')[0])

# TASK 2

desired = '19690720'
for noun in range(100):
    for verb in range(100):
        result = compute(prep(inp, noun, verb))
        first = result.partition(',')[0]
        if first == desired:
            print(100*noun + verb)
