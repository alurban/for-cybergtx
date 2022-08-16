import re

# -- global variables

# regular expression pattern
PATTERN = "\(\)|\[\]|\{\}|\<\>"

# scoring system
POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

# legal closing brackets
CLOSE = set(POINTS.keys())


# -- utilities ---------------------------------------------------------------


def strip_legal_chunks(line):
    """Strip legal chunks from a given line of text"""
    out = re.sub(PATTERN, "", line)
    if re.findall(PATTERN, out):
        # call recursively until legal chunks are gone
        out = strip_legal_chunks(out)
    return out


def get_corrupted_lines(text):
    """Return a list of corrupted lines in the body of given text"""
    return [
        line
        for line in text.splitlines()
        # merely incomplete lines have no residual closing brackets,
        # and complete but non-corrupted lines have no residual at all,
        # so both can be safely ignored
        if set(strip_legal_chunks(line)).intersection(CLOSE)
    ]


def get_illegal_closes(text):
    """Return a linewise list of the first illegal close on each line"""

    def first_illegal_closes(line):
        """Find the first illegal close on a given line"""
        residual = list(strip_legal_chunks(line))
        first = [i for (i, x) in enumerate(residual) if x in CLOSE][0]
        return residual[first]

    # return a list of the first illegal close on each corrupted line
    return [first_illegal_closes(line) for line in get_corrupted_lines(text)]


# -- main body ---------------------------------------------------------------

if __name__ == "__main__":
    score = 0
    with open("puzzle_input.txt", "r") as fobj:
        puzzle = fobj.read()

    # report the score on each corrupted line
    for (i, close) in enumerate(get_illegal_closes(puzzle)):
        print(f"line {i + 1}:\t{close}\t{POINTS[close]}")
        score += POINTS[close]

    # report the final tally
    print(f"\nFINAL SCORE:\t{score}")
