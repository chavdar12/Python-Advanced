"""Runs this lesson's scripts with the examples from the course PDF."""
import contextlib
import io
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(script, stdin, cwd=HERE):
    return subprocess.run([sys.executable, str(cwd / script)], input="\n".join(map(str, stdin)) + "\n",
                          capture_output=True, text=True, timeout=10, cwd=cwd)


def lines(text, unordered=False):
    result = [line.rstrip() for line in text.strip().splitlines()]
    return sorted(result) if unordered else result


# (script, stdin lines, expected stdout, compare lines unordered?)
STDIN_CASES = [('001_sum_matrix_elements.py',
  ['3, 6', '7, 1, 3, 3, 2, 1', '1, 3, 9, 8, 5, 6', '4, 6, 7, 9, 1, 0'],
  '76\n[[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]',
  False),
 ('002_sum_matrix_columns.py',
  ['3, 6', '7 1 3 3 2 1', '1 3 9 8 5 6', '4 6 7 9 1 0'],
  '12\n10\n19\n20\n8\n7',
  False),
 ('002_sum_matrix_columns.py', ['3, 3', '1 2 3', '4 5 6', '7 8 9'], '12\n15\n18', False),
 ('003_primary_diagonal.py', [3, '11 2 4', '4 5 6', '10 8 -12'], '4', False),
 ('003_primary_diagonal.py', [3, '1 2 3', '4 5 6', '7 8 9'], '15', False),
 ('004_symbol_in_matrix.py', [3, 'ABC', 'DEF', 'X!@', '!'], '(2, 1)', False),
 ('004_symbol_in_matrix.py', [4, 'asdd', 'xczc', 'qwee', 'qefw', 4], '4 does not occur in the matrix', False),
 ('005_square_with_maximum_sum.py',
  ['3, 6', '7, 1, 3, 3, 2, 1', '1, 3, 9, 8, 5, 6', '4, 6, 7, 9, 1, 0'],
  '9 8\n7 9\n33',
  False),
 ('005_square_with_maximum_sum.py', ['2, 4', '10, 11, 12, 13', '14, 15, 16, 17'], '12 13\n16 17\n58', False)]


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


if __name__ == "__main__":
    unittest.main()
