import math

class Monkey:

    def __init__(self):
        self.items=[]
        self.funcString = ''
        self.testDivisor = 0
        self.nextMonkey = [0,0]
        self.inspections = 0

    def inspect(self):
        self.func = lambda old: eval(self.funcString)
        for i in range(len(self.items)):
            print("Inspecting item with value {}".format(self.items[i]))
            self.items[i] = self.func(self.items[i])
            print("Worry level is now {}".format(self.items[i]))
            self.items[i] = math.floor(self.items[i] / 3)
            print("Bored! Worry level is now {}".format(self.items[i]))
            self.inspections += 1

    def throw(self):
        test = lambda test_value: (test_value % self.testDivisor)
        for item in self.items:
            if test(item) == 0:
                self.nextMonkey[0].items.append(item)
                print("Throwing item with worry level {} TRUE".format(item))
            else:
                self.nextMonkey[1].items.append(item)
                print("Throwing item with worry level {} FALSE".format(item))
        self.items = []


def do_round(monkeys):
    for m in monkeys:

        m.inspect()
        m.throw()


monkey = []
with open("input.txt",'r') as f:
    for line in f:
        if line.lstrip().startswith('Monkey'):
            monkey.append(Monkey())
        
#Rerun through for the rest
mIndex = -1
with open("input.txt",'r') as f:
    for line in f:
        if line.lstrip().startswith('Monkey'):
            mIndex += 1
        else:
            if line.lstrip().startswith('Starting items'):
                toks = line.split(':')
                item_tokens = toks[1].split(',')
                for item in item_tokens:
                    monkey[mIndex].items.append(int(item))
            elif line.lstrip().startswith('Operation'):
                #An evil eval, but it makes it easy.
                toks = line.split('=') 
                func = toks[1]
                monkey[mIndex].funcString = func
            elif line.lstrip().startswith('Test'):
                if 'divisible' in line:
                    monkey[mIndex].testDivisor = int(line.split(' ')[-1])
                else:
                    print("WARNING: Can't decode test!")
            elif line.lstrip().startswith('If true:'):
                monkey[mIndex].nextMonkey[0] = monkey[int(line.split(' ')[-1])]
            elif line.lstrip().startswith('If false:'):
                monkey[mIndex].nextMonkey[1] = monkey[int(line.split(' ')[-1])]

for j in range(len(monkey)):
    print("Monkey {}:".format(j),end='')
    print(monkey[j].items)


for i in range(20):
    do_round(monkey)
    for j in range(len(monkey)):
        print("Monkey {}:".format(j),end='')
        print(monkey[j].items)

insp = [0,0]

for m in monkey:
    if m.inspections > insp[1]:
        insp[1] = m.inspections
        if insp[1]> insp[0]:
            temp = insp[0]
            insp[0] = insp[1]
            insp[1] = temp

total = insp[0]*insp[1]

print(total)
                


