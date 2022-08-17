# Senior Python Engineer: CyberGTX

This repository contains solutions to a hiring task (technical skills assessment) assigned by CyberGTX as part of an interview procedure for the role of Senior Python Engineer.
The materials contained here constitute a solution to Day 10 of the [Advent of Code](https://adventofcode.com/2021/day/10) calendar.
The contents are straightforward:

* [`corrupted.py`](corrupted.py): Python code to efficiently find corupted lines of input and compute a total score. This is the solution to Part One.
* [`incomplete.py`](incomplete.py): Python code to efficiently find incomplete lines of input, autocomplete them, and find the resulting middle score. This is the solution to Part Two.
* [`puzzle_input.txt`](puzzle_input.txt): The puzzle input provided by Advent of Code.

**Note:** all code was developed in a Conda environment running Python 3.10, entirely using builtin Python modules.

## Part One

The first half of the problem asks to find each corrupted line (i.e. a line with improperly closed chunks) and tally up the score. I also display the first improper closure on each corrupted line. From the command line:

```bash
❯ time python -m corrupted
line 1:	)	3
line 2:	]	57
line 3:	]	57
line 4:	)	3
line 5:	)	3
line 6:	}	1197
line 7:	}	1197
line 8:	]	57
line 9:	>	25137
line 10:	]	57
line 11:	>	25137
line 12:	}	1197
line 13:	]	57
line 14:	>	25137
line 15:	]	57
line 16:	}	1197
line 17:	}	1197
line 18:	]	57
line 19:	}	1197
line 20:	]	57
line 21:	]	57
line 22:	]	57
line 23:	]	57
line 24:	}	1197
line 25:	}	1197
line 26:	}	1197
line 27:	}	1197
line 28:	]	57
line 29:	}	1197
line 30:	>	25137
line 31:	}	1197
line 32:	]	57
line 33:	]	57
line 34:	>	25137
line 35:	)	3
line 36:	}	1197
line 37:	>	25137
line 38:	)	3
line 39:	>	25137
line 40:	)	3
line 41:	]	57
line 42:	]	57
line 43:	>	25137
line 44:	>	25137
line 45:	>	25137
line 46:	>	25137
line 47:	}	1197

FINAL SCORE:	294195
python -m corrupted  0.03s user 0.02s system 71% cpu 0.060 total
```

## Part Two

The second half asks to autocomplete each incomplete line, collect scores, and find the middle value of the sorted list. From the command line:

```bash
❯ time python -m incomplete
Middle autocompletion score: 3490802734
python -m incomplete  0.03s user 0.02s system 72% cpu 0.061 total
```
