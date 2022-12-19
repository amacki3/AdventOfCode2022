with open('input.txt','r') as f:
    data = f.read()
    cur_buffer = ['' for i in range(4)]
    for i in range(len(data)):
        cur_buffer[i%4] = data[i]
        if len(set(cur_buffer)) == 4 and '' not in cur_buffer:
            print(i+1)
            break

