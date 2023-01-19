# Brainfuck 2 Fython assembly

This python scripts converts a Brainfuck code into an equivalent Fython assembly. Fython is a esolang I created, and its specifications and an interpreter can be found in [this repo](https://github.com/charon25/FythonProgrammingLanguage).

This interpreter assumes the Brainfuck memory array is unbounded on the right, but bounded on the left. Furthermore, using `<` when the pointer is at the left border won't do anything.

Usage (tested with Python 3.9.7 but probably works with earlier versions):

```
python bf2fy.py <input file path> [output file path] [--cell-size CELL_SIZE]
```

Where the parameters are :
 - `input file path` : required argument containing the input of the interpreter ;
 - `output file path` : the output of the interpreter. If not specified, will use the same as the input file with a `.txt` extension added ;
 - `-cell-size` (or `-c`) : the maximum size in bytes of a memory cell of the Brainfuck memory array. Needs to be a positive integer, and defaults to 8.

The output program can then be run by the Fython interpreter with parameter `-i a`.

## 'Hello world' example

Input Brainfuck code :

```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```

Output Fython assembly :

<details>
    <summary>Click to expand (670 lines)</summary>
    ```
    push 1
    push 1
    push 0

    push 8
    add
    push 256
    mod

    copy 2
    pop 1
    jmpz 339

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 4
    add
    push 256
    mod

    copy 2
    pop 1
    jmpz 153

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 2
    add
    push 256
    mod

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 3
    add
    push 256
    mod

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 3
    add
    push 256
    mod

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 1
    add
    push 256
    mod

    pick -2
    push 1
    sub
    jmpz 6
    place -2
    place -3
    push 1
    pop 1
    jmpnz 4
    pop 1
    push 1
    place -2

    pick -2
    push 1
    sub
    jmpz 6
    place -2
    place -3
    push 1
    pop 1
    jmpnz 4
    pop 1
    push 1
    place -2

    pick -2
    push 1
    sub
    jmpz 6
    place -2
    place -3
    push 1
    pop 1
    jmpnz 4
    pop 1
    push 1
    place -2

    pick -2
    push 1
    sub
    jmpz 6
    place -2
    place -3
    push 1
    pop 1
    jmpnz 4
    pop 1
    push 1
    place -2

    push 1
    sub
    push 256
    mod

    copy 2
    pop 1
    jmpnz -157

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 1
    add
    push 256
    mod

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 1
    add
    push 256
    mod

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 1
    sub
    push 256
    mod

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 1
    add
    push 256
    mod

    copy 2
    pop 1
    jmpz 13

    pick -2
    push 1
    sub
    jmpz 6
    place -2
    place -3
    push 1
    pop 1
    jmpnz 4
    pop 1
    push 1
    place -2

    copy 2
    pop 1
    jmpnz -17

    pick -2
    push 1
    sub
    jmpz 6
    place -2
    place -3
    push 1
    pop 1
    jmpnz 4
    pop 1
    push 1
    place -2

    push 1
    sub
    push 256
    mod

    copy 2
    pop 1
    jmpnz -343

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    copy 2
    print 1

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 3
    sub
    push 256
    mod

    copy 2
    print 1

    push 7
    add
    push 256
    mod

    copy 2
    print 1

    copy 2
    print 1

    push 3
    add
    push 256
    mod

    copy 2
    print 1

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    copy 2
    print 1

    pick -2
    push 1
    sub
    jmpz 6
    place -2
    place -3
    push 1
    pop 1
    jmpnz 4
    pop 1
    push 1
    place -2

    push 1
    sub
    push 256
    mod

    copy 2
    print 1

    pick -2
    push 1
    sub
    jmpz 6
    place -2
    place -3
    push 1
    pop 1
    jmpnz 4
    pop 1
    push 1
    place -2

    copy 2
    print 1

    push 3
    add
    push 256
    mod

    copy 2
    print 1

    push 6
    sub
    push 256
    mod

    copy 2
    print 1

    push 8
    sub
    push 256
    mod

    copy 2
    print 1

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 1
    add
    push 256
    mod

    copy 2
    print 1

    pick -2
    copy 2
    pick -1
    copy 2
    pick 2
    sub
    pop 1
    jmpnz 9
    push 1
    add
    place -1
    push 1
    add
    place -2
    push 0
    jmpz 6
    place -1
    push 1
    add
    place -2
    pick -3

    push 2
    add
    push 256
    mod

    copy 2
    print 1
    ```
</details>
<br>
Interpreter output :

```bash
> python main.py examples\helloworld.txt -i a
Program execution:
==========
Hello World!

==========
Execution complete!
```
