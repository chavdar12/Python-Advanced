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
STDIN_CASES = [('001_count_same_values.py',
  ['-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'],
  '-2.5 - 3 times\n4.0 - 2 times\n3.0 - 4 times\n-5.5 - 1 times',
  False),
 ('002_average_student_grades.py',
  [7, 'Peter 5.20', 'Mark 5.50', 'Peter 3.20', 'Mark 2.50', 'Alex 2.00', 'Mark 3.46', 'Alex 3.00'],
  'Peter -> 5.20 3.20 (avg: 4.20)\nMark -> 5.50 2.50 3.46 (avg: 3.82)\nAlex -> 2.00 3.00 (avg: 2.50)',
  True),
 ('003_record_unique_names.py',
  [8, 'Lee', 'Joey', 'Lee', 'Joe', 'Alan', 'Alan', 'Peter', 'Joey'],
  'Lee\nJoey\nJoe\nAlan\nPeter',
  True),
 ('004_parking_lot.py',
  [10,
   'IN, CA2844AA',
   'IN, CA1234TA',
   'OUT, CA2844AA',
   'IN, CA9999TT',
   'IN, CA2866HI',
   'OUT, CA1234TA',
   'IN, CA2844AA',
   'OUT, CA2866HI',
   'IN, CA9876HH',
   'IN, CA2822UU'],
  'CA2844AA\nCA9999TT\nCA2822UU\nCA9876HH',
  True),
 ('004_parking_lot.py',
  [4, 'IN, CA2844AA', 'IN, CA1234TA', 'OUT, CA2844AA', 'OUT, CA1234TA'],
  'Parking Lot is Empty',
  False),
 ('005_softuni_party.py',
  [5, '7IK9Yo0h', '9NoBUajQ', 'Ce8vwPmE', 'SVQXQCbc', 'tSzE5t0p', '9NoBUajQ', 'Ce8vwPmE', 'SVQXQCbc', 'END'],
  '2\n7IK9Yo0h\ntSzE5t0p',
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
