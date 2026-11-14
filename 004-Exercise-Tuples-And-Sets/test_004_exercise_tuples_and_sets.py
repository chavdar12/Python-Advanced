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
STDIN_CASES = [('001_unique_usernames.py',
  [6, 'George', 'George', 'George', 'Peter', 'George', 'NiceGuy1234'],
  'George\nPeter\nNiceGuy1234',
  True),
 ('002_sets_of_elements.py', ['4 3', 1, 3, 5, 7, 3, 4, 5], '3\n5', True),
 ('002_sets_of_elements.py', ['2 2', 1, 3, 1, 5], '1', False),
 ('003_periodic_table.py', [4, 'Ce O', 'Mo O Ce', 'Ee', 'Mo'], 'Ce\nEe\nMo\nO', True),
 ('004_count_symbols.py',
  ['SoftUni rocks'],
  ' : 1 time/s\n'
  'S: 1 time/s\n'
  'U: 1 time/s\n'
  'c: 1 time/s\n'
  'f: 1 time/s\n'
  'i: 1 time/s\n'
  'k: 1 time/s\n'
  'n: 1 time/s\n'
  'o: 2 time/s\n'
  'r: 1 time/s\n'
  's: 1 time/s\n'
  't: 1 time/s',
  False),
 ('005_phonebook.py',
  ['Adam-0888080808', 2, 'Mery', 'Adam'],
  'Contact Mery does not exist.\nAdam -> 0888080808',
  False),
 ('006_longest_intersection.py',
  [3, '0,3-1,2', '2,10-3,5', '6,15-3,10'],
  'Longest intersection is [6, 7, 8, 9, 10] with length 5',
  False),
 ('007_longest_intersection_with_ranges.py',
  [3, '0,3-1,2', '2,10-3,5', '6,15-3,10'],
  'Longest intersection is [6, 7, 8, 9, 10] with length 5',
  False),
 ('008_battle_of_names.py', [4, 'Pesho', 'Stefan', 'Stamat', 'Gosho'], '304, 128, 206, 511', False)]


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


if __name__ == "__main__":
    unittest.main()
