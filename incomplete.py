# re-use utilities from part 1
from corrupted import (CLOSE, strip_legal_chunks)

# -- global variables

# bracket pairs
PAIR = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

# scoring system
POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


# -- utilities ---------------------------------------------------------------


def get_incomplete_lines(text):
    """Return a list of incomplete lines in the body of given text"""
    lines = text.splitlines()
    residuals = [strip_legal_chunks(line) for line in lines]
    return [
        line
        for (line, residual) in zip(lines, residuals)
        # merely incomplete lines have residuals but no closing brackets
        if residual and not set(residual).intersection(CLOSE)
    ]


def autocompletion_score(line):
    """Compute the autocompletion score for a given line of input"""
    score = 0

    # the autocompletion is simply closing brackets
    # corresponding to each residual, in reverse order
    completion = "".join([PAIR[x] for x in strip_legal_chunks(line)[::-1]])

    # tally up and return the score
    for close in completion:
        score = score * 5 + POINTS[close]
    return score


# -- main body ---------------------------------------------------------------

if __name__ == "__main__":
    with open("puzzle_input.txt", "r") as fobj:
        puzzle = fobj.read()

    # compute autocompletion scores
    scores = [
        autocompletion_score(line)
        for line in get_incomplete_lines(puzzle)
    ]

    # find the middle of this list:
    # first, sort the list by ascending values
    # then return the value at the midpoint of the list
    middle = sorted(scores)[len(scores) // 2]
    print(f"Middle autocompletion score: {middle}")
