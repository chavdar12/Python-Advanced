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
STDIN_CASES = [('001_reverse_numbers.py', ['1 2 3 4 5'], '5 4 3 2 1', False),
 ('002_maximum_and_minimum_element.py',
  [9, '1 97', 2, '1 20', 2, '1 26', '1 20', 3, '1 91', 4],
  '26\n20\n91, 20, 26',
  False),
 ('002_maximum_and_minimum_element.py',
  [10, 2, '1 47', '1 66', '1 32', 4, 3, '1 25', '1 16', '1 8', 4],
  '32\n66\n8\n8, 16, 25, 32, 66, 47',
  False),
 ('003_fast_food.py', [348, '20 54 30 16 7 9'], '54\nOrders complete', False),
 ('003_fast_food.py', [499, '57 45 62 70 33 90 88 76'], '90\nOrders left: 76', False),
 ('004_fashion_boutique.py', ['5 4 8 6 3 8 7 7 9', 16], '5', False),
 ('004_fashion_boutique.py', ['1 7 8 2 5 4 7 8 9 6 3 2 5 4 6', 20], '5', False),
 ('005_truck_tour.py', [3, '1 5', '10 3', '3 4'], '1', False),
 ('006_balanced_parentheses.py', ['{[()]}'], 'YES', False),
 ('006_balanced_parentheses.py', ['{[(])}'], 'NO', False),
 ('006_balanced_parentheses.py', ['{{[[(())]]}}'], 'YES', False),
 ('007_robotics.py',
  ['ROB-15;SS2-10;NX8000-3', '8:00:00', 'detail', 'glass', 'wood', 'apple', 'End'],
  'ROB - detail [08:00:01]\nSS2 - glass [08:00:02]\nNX8000 - wood [08:00:03]\nNX8000 - apple [08:00:06]',
  False),
 ('008_robotics_with_functions.py',
  ['ROB-15;SS2-10;NX8000-3', '8:00:00', 'detail', 'glass', 'wood', 'apple', 'End'],
  'ROB - detail [08:00:01]\nSS2 - glass [08:00:02]\nNX8000 - wood [08:00:03]\nNX8000 - apple [08:00:06]',
  False),
 ('007_robotics.py',
  ['ROB-60', '7:59:59', 'detail', 'glass', 'wood', 'sock', 'End'],
  'ROB - detail [08:00:00]\nROB - sock [08:01:00]\nROB - wood [08:02:00]\nROB - glass [08:03:00]',
  False),
 ('008_robotics_with_functions.py',
  ['ROB-60', '7:59:59', 'detail', 'glass', 'wood', 'sock', 'End'],
  'ROB - detail [08:00:00]\nROB - sock [08:01:00]\nROB - wood [08:02:00]\nROB - glass [08:03:00]',
  False),
 ('009_crossroads.py',
  [10, 5, 'Mercedes', 'green', 'Mercedes', 'BMW', 'Skoda', 'green', 'END'],
  'Everyone is safe.\n3 total cars passed the crossroads.',
  False),
 ('009_crossroads.py',
  [9, 3, 'Mercedes', 'Hummer', 'green', 'Hummer', 'Mercedes', 'green', 'END'],
  'A crash happened!\nHummer was hit at e.',
  False),
 ('010_key_revolver.py',
  [50, 2, '11 10 5 11 10 20', '15 13 16', 1500],
  'Ping!\nBang!\nReloading!\nBang!\nBang!\nReloading!\n2 bullets left. Earned $1300',
  False),
 ('010_key_revolver.py',
  [20, 6, '14 13 12 11 10 5', '13 3 11 10', 800],
  "Bang!\nPing!\nPing!\nPing!\nPing!\nPing!\nCouldn't get through. Locks left: 3",
  False),
 ('011_cups_and_bottles.py', ['4 2 10 5', '3 15 15 11 6'], 'Bottles: 3\nWasted litters of water: 26', False),
 ('011_cups_and_bottles.py',
  ['1 5 28 1 4', '3 18 1 9 30 4 5'],
  'Cups: 4\nWasted litters of water: 35',
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
