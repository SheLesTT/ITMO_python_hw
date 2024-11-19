import sys

def print_lines(filenames: list[str]) -> None:
    idx = 1
    for filename in filenames:
        try:
            with open(filename) as f:
                for line  in (f):
                    print("   ", idx, line, end="")
                    idx += 1
        except FileNotFoundError:
            print(f"nl: {filename}: No such file or directory")
def print_input()-> None:
    idx = 1
    for line in sys.stdin:
        print("   ", idx, line, end="")
        idx += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_lines(sys.argv[1:])
    else:
        print_input()