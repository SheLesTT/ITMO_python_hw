import sys
from collections import deque


def tail_lines(filenames: list[str]) -> None:
    print_name = False
    if len(filenames) > 1:
        print_name = True
    for filename in filenames:
        try:
            with open(filename) as f:
                if print_name:
                    print( "==>", filename, "<==")
                for line in (f.readlines() [-10:]):
                    print(line, end ='')
                if filename != filenames[-1]:
                    print()
        except FileNotFoundError:
            print(f"tail: cannot open '{filename}' for reading: No such file or directory")
def print_input()-> None:
        lines = deque(sys.stdin, maxlen=17)
        for line in lines:
            print(line, end="")
        print()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        tail_lines(sys.argv[1:])
    else:
        print_input()
