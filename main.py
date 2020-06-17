import sys

from random import random
from processor import init_processor, str_proc
from memory import init_memory, str_memory
from instructions import run_line

if len(sys.argv) == 1:
    print('Please enter file you want to debug as argument')
    sys.exit()

print("Welcome to Aditama's x86 assembly emulator.")
help = "Instructions: help, next or n, proc <register:optional> or p, mem <addr:optional> or m, exit/quit/q"
print(help)

filename = sys.argv[1]
f = open(filename, "r")
f = f.read().split('\n')

memory = init_memory(2**8)
processor = init_processor(2**8)

lineNo = 1
line = f[lineNo-1]
if(line == None):
    print('======END OF FILE======')
else:
    print(str(lineNo) + '   ' + line)

while(True):
    user_in = input("> ")
    if(user_in == 'reset' or user_in == 'r'):
        f = open(filename, "r")
        f = f.read().split('\n')
        memory = init_memory(2**8)
        processor = init_processor(2**8)

        lineNo = 1
        line = f[lineNo-1]
        if(line == None):
            print('======END OF FILE======')
        else:
            print(str(lineNo) + '   ' + line)
    elif(user_in == 'help' or user_in == 'h'):
        print(help)
    elif(user_in[:3] == 'mem' or user_in[0] == 'm'):
        if len(user_in) <= 3:
            print(str_memory(memory))
        else:
            _, addr = user_in.split(' ')
            addr = int(addr[2:], 16)
            print("{:<4s}: {:>4s}".format(hex(addr), hex(memory[addr])))
    elif(user_in[:4] == 'proc' or user_in[0] == 'p'):
        if len(user_in) <= 4:
            print(str_proc(processor))
        else:
            _, reg = user_in.split(' ')
            contents = processor[reg]
            print('{:<3s}'.format(reg) + ': ' + f"{contents:#0{10}x}")
    elif(user_in == 'next' or user_in == 'n'):
        if line == None:
            continue
        if line:
            print("RUNNING LINE", line,'\n')
            run_line(line, processor, memory)
            if lineNo == len(f):
                line=None
                print('======END OF FILE======')
            else:
                line=f[lineNo]
                lineNo += 1
        while(not line):
            if lineNo == len(f):
                line=None
                break
            line=f[lineNo]
            lineNo += 1
        print(str(lineNo) + '   ' + line)
    elif user_in == 'exit' or user_in == 'quit' or user_in == 'q':
        break
    else:
        print('Invalid statement')
        continue
