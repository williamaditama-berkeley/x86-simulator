movl $252, %esp
movl %esp, %ebp

pushl %ebp ;CALLER
movl %esp, %ebp
pushl $4
pushl $3

pushl %eip
pushl %ebp ;CALLEE
movl %esp, %ebp
subl $16, %esp
movl 8(%ebp), %edx
movl 12(%ebp), %eax
addl %edx, %eax
movl %eax, -4($ebp)
movl -4(%ebp), %eax
addl $1, %eax
popl %eip

addl $8, %esp
