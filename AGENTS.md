# AGENTS.md

## Repository overview
- This repository is a collection of standalone Python lesson and exercise scripts grouped by topic, e.g. `001-Lists-As-Stacks-And-Queues/`, `011-File-Handling/`, and `015-Exercise-Error-Handling/`.
- Lesson files are named `NNN_problem_name.py` (e.g. `001_reverse_strings.py`). They are meant to be run independently and usually communicate through `input()` and `print()`.
- `013-Modules/` is the main package-style area. Its subfolders contain small importable packages such as `Fibonacci_sequence/`, `Mathematical_operations/`, and `Triangle/`.

## Working patterns
- Keep exercises self-contained unless the folder already uses package imports. The module examples are the main exception: `013-Modules/Fibonacci_sequence/main.py`, `013-Modules/Mathematical_operations/main.py`, and `013-Modules/Triangle/main.py` import sibling helpers.
- Preserve the current file and folder names, including existing typos that are already referenced elsewhere, such as `helper_funcitons.py` and `print_triangle_funcitons.py`.
- Do not change the stdin/stdout contract of the lesson scripts unless the task explicitly asks for it. The scripts in folders like `001-Lists-As-Stacks-And-Queues/` and `014-Error-Handling/` are written as console exercises.
- File-handling examples use relative paths from the lesson script, for example `011-File-Handling/001_file_opener.py` opens `../Files/text.txt`, so validate them from the expected working directory.

## Validation
- The workspace has a repo-wide `tests/` suite: `tests/test_scripts.py` checks the scripts against the course PDF examples (and fails if a new script is neither tested nor listed in `COMPILE_ONLY`), `tests/test_by_folder.py` compile-checks every file, and `tests/test_repo.py` covers `013-Modules/`.
- Validate changes with `python3 -m unittest discover -s tests` from the repository root.
- Still run affected scripts directly when you need to check console I/O behavior, e.g. `python3 013-Modules/Mathematical_operations/main.py`.
- Run module examples from the repository root so imports like `from Fibonacci_sequence.fibonacci_task_functions import *` resolve correctly.
