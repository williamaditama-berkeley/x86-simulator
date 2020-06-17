# x86-simulator

This is a simulator to help people learn what happens inside a processor with an x86 architecture.

## Starting up
Run `python3 main.py <FILENAME.S>` where `<FILENAME.S>` is the .s file that contains all the assembly instructions.
A sample .s file is given (test.s)

## Commands
Once you start the program, you will see  
```> ```  
You can type in the following commands:
* **help**: Print the help screen
* **next or n**: Next instruction
* **proc <register:optional> or p**: Print the state of the processor
* **mem <addr:optional> or m**: Print the state of main memory
* **exit/quit/q** : Quit the program
