# Python-Advanced

This repository contains standalone Python lesson scripts and a small package-style section under `013-Modules/`.

## Run the tests

Every lesson folder is self-contained and carries its own tests. Run them from inside the lesson:

```bash
cd 001-Lists-As-Stacks-And-Queues
python3 -m unittest
```

Each lesson's `test_*.py` runs the scripts against the examples from the course PDF (stdin/stdout, functions,
expected exceptions and file handling). Lessons without PDF examples (Comprehension, the File Handling exercise)
are only compile-checked in CI.

