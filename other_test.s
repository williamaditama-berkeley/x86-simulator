callee:
    pushl %ebp
    movl %esp, %ebp
    subl $16, %esp
    movl 8(%ebp), %edx
    movl 12(%ebp), %eax
    addl %edx, %eax
    movl %eax, -4(%ebp)
    movl -4(%ebp), %eax
    addl $1, %eax
    leave
    ret
global:
    pushl %ebp
    movl %esp, %ebp
    pushl $4
    pushl $3
    call callee
    addl $8, %esp
    movl %eax, global
    nop
    leave
    ret