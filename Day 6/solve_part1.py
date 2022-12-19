
def is_start_marker(next_letter,reset = False):
    cur_buffer = ['' for i in range(4)]
    i = 0
    while True:
        if reset:
            cur_buffer = ['' for i in range(4)]
            i =  0
        cur_buffer[i] = next_letter
        i = (i+1) % 4
        if len(set(cur_buffer)) == 4 and '' not in cur_buffer:
            yield True
        else
            yield False

with open('input.txt','r') as f:
    data = f.read()
    for i,letter in enumerate(data):
        if is_start_marker(letter):
            print(i)
            break
        
