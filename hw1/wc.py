import sys
import os
from collections import deque

def tail_lines(filenames: list[str]) -> None:
    total_bytes = 0
    total_words = 0
    total_lines = 0

    file_counts = []
    max_length =0
    for filename in filenames:
        try:
            with open(filename) as f:
                lines = f.readlines()
                bytes_count = os.path.getsize(filename)
                line_count =0
                word_count = 0

                for line in (lines):
                    word_count += len(line.split())
                    for char in line :
                        if char == '\n':
                            line_count += 1

                total_lines += line_count
                total_words += word_count
                total_bytes += bytes_count

            file_counts.append((filename, line_count, word_count, bytes_count))

        except FileNotFoundError:

            file_counts.append((filename,-1 , -1, -1))
    for count in (total_lines, total_words, total_bytes):
        digits = len(str(count))
        if digits > max_length:
            max_length = digits
    for filename, line_count, word_count, bytes_count in file_counts:
        if line_count == -1:
            print(f"wc: {filename}: No such file or directory")
        else:
            print(f"{line_count:{max_length}} {word_count:{max_length}} {bytes_count:{max_length}} {filename}")

    if len(filenames) > 1:
        print(f"{total_lines:{max_length}} {total_words:{max_length}} {total_bytes:{max_length}} total")

def print_input()-> None:
    bytes_count = 0
    line_count = 0
    word_count = 0
    for line in sys.stdin:
        bytes_count += len(line)
        line_count += 1
        word_count += len(line.split())
    print(f"   {line_count}    {word_count}    {bytes_count}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        tail_lines(sys.argv[1:])
    else:
        print_input()
