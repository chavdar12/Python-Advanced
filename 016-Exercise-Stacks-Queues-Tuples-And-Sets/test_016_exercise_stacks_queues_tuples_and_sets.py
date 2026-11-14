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
STDIN_CASES = [('001_numbers.py',
  ['1 2 3 4 5', '1 2 3', 3, 'Add First 5 6', 'Remove Second 8 9 11', 'Check Subset'],
  'True\n1, 2, 3, 4, 5, 6\n1, 2, 3',
  False),
 ('001_numbers.py',
  ['5 4 2 9 9 5 4',
   '1 1 1 5 6 5',
   4,
   'Add First 5 6 9 3',
   'Add Second 1 2 3 3 3',
   'Check Subset',
   'Remove Second 1 2 3 4 5'],
  'False\n2, 3, 4, 5, 6, 9\n6',
  False),
 ('002_expression_evaluator.py', ['6 3 - 2 1 * 5 /'], '1', False),
 ('002_expression_evaluator.py', ['2 2 - 1 *'], '0', False),
 ('002_expression_evaluator.py', ['10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *'], '164', False),
 ('003_milkshakes.py',
  ['20, 24, -5, 17, 22, 60, 26', '26, 60, 22, 17, 24, 10, 55'],
  'Great! You made all the chocolate milkshakes needed!\nChocolate: 20\nMilk: 10, 55',
  False),
 ('003_milkshakes.py',
  ['-10, -2, -30, 10', '-5'],
  'Not enough milkshakes.\nChocolate: -10, -2, -30, 10\nMilk: empty',
  False),
 ('003_milkshakes.py',
  ['2, 3, 3, 7, 2', '2, 7, 3, 3, 2, 14, 6'],
  'Great! You made all the chocolate milkshakes needed!\nChocolate: empty\nMilk: 14, 6',
  False),
 ('004_honey.py',
  ['20 62 99 35 0 150', '120 60 10 1 70 10', '+ - + + / * - - /'],
  'Total honey made: 148\nBees left: 99, 35, 0, 150',
  False),
 ('004_honey.py',
  ['30', '15 9 5 150 8', '* + + * -'],
  'Total honey made: 4500\nNectar left: 15, 9, 5',
  False),
 ('005_santas_present_factory.py',
  ['10 -5 20 15 -30 10', '40 60 10 4 10 0'],
  'The presents are crafted! Merry Christmas!\nMaterials left: 20, -5, 10\nBicycle: 1\nTeddy bear: 2',
  False),
 ('005_santas_present_factory.py',
  ['30 5 15 60 0 30', '-15 10 5 -15 25'],
  'No presents this Christmas!\nMaterials left: 20, 30\nDoll: 1\nTeddy bear: 1',
  False),
 ('006_paint_colors.py', ['d yel blu e low redd'], "['yellow', 'blue', 'red']", False),
 ('006_paint_colors.py', ['r ue nge ora bl ed'], "['red', 'blue']", False),
 ('006_paint_colors.py', ['re ple blu pop e pur d'], "['red', 'purple', 'blue']", False)]


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


if __name__ == "__main__":
    unittest.main()
