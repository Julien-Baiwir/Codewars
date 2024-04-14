"""Testing 1-2-3
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.
Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]"""

lines = ["a", "b", "c"] 
def add_line_numbers(lines):
    numbered_lines = []
    for i, line in enumerate(lines, start=1):
        numbered_lines.append(f"{i}: {line}")
    return numbered_lines

print(add_line_numbers(lines))


def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]