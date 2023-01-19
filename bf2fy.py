import argparse
import re


def read_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to the brainfuck file.')
    parser.add_argument('-s', '--cellsize', help='Size of a memory cell in bits. Defaults to 8.', default='8')
    parser.add_argument('-o', '--outputpath', help='Path of the output Fython file. Defaults to the same as the brainfuck file with a ".py" extension.', default=None)

    return parser.parse_args()


def get_fython_from_character(character: str):
    if character == '+':
        return ['push %n', 'add', 'push %c', 'mod']
    elif character == '-':
        return ['push %n', 'sub', 'push %c', 'mod']
    elif character == '.':
        return ['copy 2', 'print 1']
    elif character == ',':
        return ['copy 2', 'read 1']
    elif character == '<':
        return ['pick -2', 'push 1', 'sub', 'jmpz 6', 'place -2', 'place -3', 'push 1', 'pop 1', 'jmpnz 4', 'pop 1', 'push 1', 'place -2']
    elif character == '>':
        return ['pick -2', 'copy 2', 'pick -1', 'copy 2', 'pick 2', 'sub', 'pop 1', 'jmpz 3', 'push 1', 'add', 'place -1', 'push 1', 'add', 'place -2']
    elif character == '[':
        return ['copy 2', 'pop 1', 'jmpz %j']
    elif character == ']':
        return ['copy 2', 'pop 1', 'jmpnz %j']


def get_brackets_pairs(bf_code: str):
    brackets: dict[int, list[int]] = dict()
    depth = 0
    for i, c in enumerate(bf_code):
        if c == '[':
            depth += 1
            if not depth in brackets:
                brackets[depth] = []
            brackets[depth].append(i)
        elif c == ']':
            if not depth in brackets:
                brackets[depth] = []
            brackets[depth].append(i)
            depth -= 1
    
    pairs = []
    for _, indexes in brackets.items():
        pairs.extend([(indexes[i], indexes[i+1]) for i in range(0, len(indexes), 2)])
    
    return pairs


if __name__ == '__main__':
    arguments = read_arguments()

    try:
        with open(arguments.filepath, 'r') as fi:
            bf_code = fi.read()
    except IOError:
        print(f"bf2fy.py: error: can't open file '{arguments.filepath}'.")
        exit()
    
    # Remove everything which is not a brainfuck instruction
    bf_code = re.sub(r'[^+.,<>\[\]-]', '', bf_code)


