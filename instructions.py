from memory import mem_getl, mem_setl
def run_line(line, proc, mem):
    # Filter out comments
    i = 0
    for c in line:
        if c == ';':
            line = line[:i]
        i+=1
    del(i)
    if not line:
        return

    tokens = line.split(' ')
    instr = tokens[0]
    arg1 = tokens[1]
    arg2 = None
    if len(tokens)>2:
        arg2 = tokens[2]
    
    if arg2:
        arg1 = arg1[:-1]  # Get rid of comma

    if(instr == 'addl' or instr == 'subl'):
        r2 = arg2[1:]
        a = 0
        if(arg1[0] == '%'):
            a = proc[arg1[1:]]
        elif(arg1[0] == '('):
            r1_val = proc[arg1[2:-1]]
            a = mem_getl(mem, r1_val)
        elif(arg1[0].isnumeric() or arg1[0] == '-'):
            offset = ''
            for c in arg1:
                if c == '(':
                    break
                if c.isnumeric():
                    offset += c
            offset = int(offset)
            r1 = arg1[-4: -1]
            addr = proc[r1] + offset
            a = mem_getl(mem, addr)
        elif(arg1[0] == '$'):
            constant = int(arg1[1:])
            a = constant
        proc[r2] = proc[r2] + a if instr == 'addl' else proc[r2] - a

    elif instr == 'movl':
        value_from = 0
        move_to = ['REG/MEM', 'reg/addr']  # will be set to REG or MEM

        if arg1[0] == '%':  # movl %eax, ...
            value_from = proc[arg1[1:]]
        elif arg1[0] == '$':  # movl $10, ...
            value_from = int(arg1[1:])
        elif arg1[-1].isnumeric():  # movl 12, ... ; take from address 12
            value_from = mem_getl(mem, int(arg1))
        elif arg1[0].isnumeric(): # movl 8(%ebp), ...
            offset = ''
            for c in arg1:
                if c == '(':
                    break
                if c.isnumeric():
                    offset += c
            offset = int(offset) if offset else 0
            reg = arg1[-4:-1]
            addr = offset + proc[reg]
            value_from = mem_getl(mem, addr)

        # MOVE TO
        if arg2[0] == '%':
            dest_reg = arg2[1:]
            proc[dest_reg] = value_from
        elif arg2[0] == '-' or arg2[0].isnumeric() or arg2[0] == '(':
            offset = ''
            for c in arg2:
                if c == '(':
                    break
                if c.isnumeric():
                    offset += c
            offset = int(offset) if offset else 0
            r2 = arg2[-4:-1]
            addr = proc[r2]
            mem_setl(mem, offset + addr, value_from)

    elif instr == 'popl':
        run_line('movl (%esp), ' + arg1, proc, mem)
        run_line('addl $4, %esp', proc, mem)

    elif instr == 'pushl':
        run_line('subl $4, %esp', proc, mem)
        run_line('movl ' + arg1 + ', (%esp)', proc, mem)
    else:
        print('%s not supported' % (instr))
