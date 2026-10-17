# Python-Advanced

This repository contains standalone Python lesson scripts and a small package-style section under `013-Modules/`.

## Run the tests

```bash
python3 -m unittest discover -s tests
```

The test suite is grouped by lesson folder:
- `tests/test_by_folder.py` creates one compile test per Python file, grouped into folder-specific test classes
- `tests/test_repo.py` keeps the higher-level smoke tests for the reusable helpers and module entry points in `013-Modules/`

