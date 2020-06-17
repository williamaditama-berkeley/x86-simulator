def init_processor(mem_size):
    from random import randint
    proc = {}
    for r in ALL_REGISTERS:
        proc[r] = randint(0, 2**32-1)
    proc['esp'] = mem_size - 1
    proc['ebp'] = mem_size - 1
    proc['eip'] = 0
    return proc


def str_proc(proc, in_hex=True):
    out = ''

    def align(word, number):
        if in_hex:
            return '{:<3s}'.format(word) + ': ' + f"{number:#0{10}x}"
        return "{:<3s}: {:>4d}".format(word, number)

    for i in range(min(len(GPR), len(SEG_REGS))):
            out += align(GPR[i], proc[GPR[i]]) \
                + '\t\t' + align(SEG_REGS[i], proc[SEG_REGS[i]])\
                + '\n'
    # got kinda lazy
    out += align(GPR[7], proc[GPR[7]])
    return out


GPR = ['eax', 'ebx', 'ecx', 'edx', 'esi', 'edi',
       'esp', 'ebp']
SEG_REGS = ['cs', 'ds', 'es', 'fs', 'gs', 'ss',
            'eip']
ALL_REGISTERS = GPR + SEG_REGS
