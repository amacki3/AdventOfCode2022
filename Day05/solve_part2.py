#This is a simple exercise of parsing the input and then moving data around a set of stacks.
#This time stacks are a challenge, we could rewrite the code to just use lists and negative indexing - a benefit of python.
# but here lets instead just change the move method to store a temporary deque to allow for reveresed return order onto the next stack when needed.

from collections import deque
NUM_STACKS = 9
stacks = [deque() for i in range(NUM_STACKS)]

def parse_input_setup(data,line):
    if line[1] == '1':
        #Reached the end, our stacks need inverting. We assume the 1 indicates this and the input file is fixed in schema
        #Luckily we have selected a deque, so there is a nice function that should be O(1), but we don't know under the hood.
        # not that it matters. this is a quick to solution not a quick solution exercise
        for i in range(NUM_STACKS):
            data[i].reverse()
        return data
    else:
        #Loop over all available elements and add if it exists
        for i in range(NUM_STACKS):
            if line[4*i + 1] != ' ':
                data[i].append(line[4*i+1])
        return data


def parse_next_instruction(line):
    #Could use regex but input is very uniform
    #Lets just split on a blank space char and infer what is numeric and what isn't based on position

    #Remove one from start,end so they act as zero-indexed locations.

    split_tokens = line.split()
    num_to_move = int(split_tokens[1])
    start_location = int(split_tokens[3]) - 1
    end_location = int(split_tokens[5]) - 1
    return num_to_move,start_location,end_location

def do_move(stacks,num,start,end):
    #a move can now be multiple parts moved to another
    # so lets just use a temproray deque and it handles the maintaining of order 'transparently'
    # but does add overhead.
    tempDeque = deque()
    for _ in range(num):
        tempDeque.append(stacks[start].pop())
    for _ in range(num):
        stacks[end].append(tempDeque.pop())


    return stacks


with open('input.txt','r') as f:
    for line in f:
        if 'move' in line:
            n,s,e = parse_next_instruction(line)
            stacks = do_move(stacks,n,s,e)
        elif len(line) > 2:
            stacks = parse_input_setup(stacks,line)

for i in range(len(stacks)):
    print(stacks[i].pop())