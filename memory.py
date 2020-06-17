def init_memory(mem_size):
    from random import random
    memory = []
    for i in range(mem_size):
        memory.append(int(random() * (2**8)))
    return memory


def str_memory(mem, width=4, by='lw'):
    out = ''
    def align(word, number):
        return "{:<4s}: {:>10s}".format(word, number)
    # for (addr, m) in enumerate(mem):
    #     if addr % width == 0:
    #         out += '\n'
    #     out += align(hex(addr), hex(m)) +'\t'
    # return out
    for addr in range(len(mem)-16, -1, -16):
        for i in range(addr, addr + 16, 4):
            out += align(hex(i), hex(mem_getl(mem, i))) + '\t'
        out += '\n'
        # if addr % 16 == 0:
        #     out += '\n'
    return out

def mem_getl(mem, addr):
    result =  mem[addr] << 3 * 8
    result += mem[addr+1] << 2 * 8
    result += mem[addr+2] << 8
    result += mem[addr+3]
    return result

def mem_setl(mem, addr, value):
    mem[addr+0] = value & 0x0ff000000
    mem[addr+1] = value & 0x0ff0000
    mem[addr+2] = value & 0x0ff00
    mem[addr+3] = value & 0x0ff