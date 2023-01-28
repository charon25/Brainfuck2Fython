import argparse
import re


def check_positive_int(number: str):
    try:
        number = int(number)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{number}' is an invalid positive integer value.")
    if number < 0:
        raise argparse.ArgumentTypeError(f"{number} is an invalid positive integer value.")
    return number

def read_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', help='Path to the brainfuck file.')
    parser.add_argument('output_path', nargs='?', default=None, help='Path of the output Fython file. Defaults to the same as the brainfuck file with a ".txt" extension.')
    parser.add_argument( '--cell-size', '-c', type=check_positive_int, default='8', help='Size of a memory cell in bits. Defaults to 8.')

    return parser.parse_args()


def get_fython_from_character(character: str) -> list[str]:
    if character == '+':
        return ['push %n', 'add', 'push %c', 'mod']
    elif character == '-':
        return ['push %n', 'sub', 'push %c', 'mod']
    elif character == '.':
        return ['copy 2', 'print 1']
    elif character == ',':
        return ['pop 1', 'read 1']
    elif character == '<':
        return ['pick -2', 'push 1', 'sub', 'jmpz 6', 'place -2', 'place -3', 'push 1', 'pop 1', 'jmpnz 4', 'pop 1', 'push 1', 'place -2']
    elif character == '>':
        return ['pick -2', 'copy 2', 'pick -1', 'copy 2', 'pick 2', 'sub', 'pop 1', 'jmpnz 9', 'push 1', 'add', 'place -1', 'push 1', 'add', 'place -2', 'push 0', 'jmpz 6', 'place -1', 'push 1', 'add', 'place -2', 'pick -3']
    elif character == '[':
        return ['copy 2', 'pop 1', 'jmpz %j']
    elif character == ']':
        return ['copy 2', 'pop 1', 'jmpnz %j']


def get_brackets_pairs(bf_code: str):
    brackets: dict[int, list[int]] = dict()
    depth = 0
    for index, c in enumerate(bf_code):
        if c == '[':
            depth += 1
            if not depth in brackets:
                brackets[depth] = []
            brackets[depth].append(index)
        elif c == ']':
            if not depth in brackets:
                brackets[depth] = []
            brackets[depth].append(index)
            depth -= 1
    
    pairs = []
    for _, indexes in brackets.items():
        pairs.extend([(indexes[i], indexes[i+1]) for i in range(0, len(indexes), 2)])
    
    return pairs

def get_brackets_jump_length(fython_code: list[list[str]], start_index: int, end_index: int) -> tuple[int, int]:
    instruction_count = sum(len(instructions) for instructions in fython_code[start_index+1:end_index])
    return (instruction_count + 1, instruction_count + len(fython_code[start_index]) + len(fython_code[end_index]) - 1)


if __name__ == '__main__':
    arguments = read_arguments()

    try:
        with open(arguments.input_path, 'r') as fi:
            bf_code = fi.read()
    except IOError:
        print(f"bf2fy.py: error: can't read file '{arguments.filepath}'.")
        exit()

    cell_size = 2 ** arguments.cell_size

    # Remove everything which is not a brainfuck instruction
    bf_code = re.sub(r'[^+.,<>\[\]-]', '', bf_code)

    brackets_pairs = get_brackets_pairs(bf_code)

    fython_code: list[list[str]] = []
    index = 0
    # Split on every character except for streak of + or - which are taken as one block
    for characters in re.findall(r'([.,<>\[\]]|\++|-+)', bf_code):
        fython = get_fython_from_character(characters[0])
        # For + and - instructions, replace the %n by the number of + or - and the %c by the cell size
        fython = [instruction.replace('%n', str(len(characters))).replace('%c', str(cell_size)) for instruction in fython]
        fython_code.append(fython)
        # For + and - streaks, add empty lists to keep indexes synchronized
        fython_code.extend([] for _ in range(len(characters) - 1))
        index += len(characters)

    # Replace %j by the correct jump length for every [ and ]
    for start_index, end_index in brackets_pairs:
        open_jump_length, close_jump_length = get_brackets_jump_length(fython_code, start_index, end_index)
        fython_code[start_index] = [instruction.replace('%j', str(open_jump_length)) for instruction in fython_code[start_index]]
        fython_code[end_index] = [instruction.replace('%j', str(-close_jump_length)) for instruction in fython_code[end_index]]

    fython_code.insert(0, ['push 1', 'push 1', 'push 0'])
    output_path = arguments.input_path + '.txt' if arguments.output_path is None else arguments.output_path
    try:
        with open(output_path, 'w') as fo:
            fo.write("\n\n".join("\n".join(instruction for instruction in instructions) for instructions in fython_code if instructions))
    except IOError:
        print(f"bf2fy.py: error: can't write to file '{arguments.filepath}'.")
        exit()
