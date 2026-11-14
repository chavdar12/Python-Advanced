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
STDIN_CASES = [('001_reverse_strings.py', ['I Love Python'], 'nohtyP evoL I', False),
 ('001_reverse_strings.py', ['Stacks and Queues'], 'seueuQ dna skcatS', False),
 ('002_matching_brackets.py',
  ['1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'],
  '(2 + 3)\n(3 + 1)\n(2 - (2 + 3) * 4 / (3 + 1))',
  False),
 ('002_matching_brackets.py', ['(2 + 3) - (2 + 3)'], '(2 + 3)\n(2 + 3)', False),
 ('003_supermarket.py',
  ['George', 'Peter', 'William', 'Paid', 'Michael', 'Oscar', 'Olivia', 'Linda', 'End'],
  'George\nPeter\nWilliam\n4 people remaining.',
  False),
 ('003_supermarket.py', ['Anna', 'Emma', 'Alexander', 'End'], '3 people remaining.', False),
 ('004_water_dispenser.py',
  [2, 'Peter', 'Amy', 'Start', 2, 'refill 1', 1, 'End'],
  'Peter got water\nAmy got water\n0 liters left',
  False),
 ('004_water_dispenser.py',
  [10, 'Peter', 'George', 'Amy', 'Alice', 'Start', 2, 3, 3, 3, 'End'],
  'Peter got water\nGeorge got water\nAmy got water\nAlice must wait\n2 liters left',
  False),
 ('005_hot_potato.py', ['Tracy Emily Daniel', 2], 'Removed Emily\nRemoved Tracy\nLast is Daniel', False),
 ('005_hot_potato.py',
  ['George Peter Michael William Thomas', 10],
  'Removed Thomas\nRemoved Peter\nRemoved Michael\nRemoved George\nLast is William',
  False)]


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


if __name__ == "__main__":
    unittest.main()
