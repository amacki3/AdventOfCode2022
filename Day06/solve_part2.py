BUFFER_LEN = 14

with open('input.txt','r') as f:
    data = f.read()
    cur_buffer = ['' for i in range(BUFFER_LEN)]
    for i in range(len(data)):
        cur_buffer[i%BUFFER_LEN] = data[i]
        if len(set(cur_buffer)) == BUFFER_LEN and '' not in cur_buffer:
            print(i+1)
            break

