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
STDIN_CASES = [('001_flatten_lists.py', ['1 2 3 |4 5 6 |  7  88'], '7 88 4 5 6 1 2 3', False),
 ('001_flatten_lists.py', ['7 | 4  5|1 0| 2 5 |3'], '3 2 5 1 0 4 5 7', False),
 ('002_matrix_modification.py',
  [3, '1 2 3', '4 5 6', '7 8 9', 'Add 0 0 5', 'Subtract 1 1 2', 'END'],
  '6 2 3\n4 3 6\n7 8 9',
  False),
 ('002_matrix_modification.py',
  [4,
   '1 2 3 4',
   '5 6 7 8',
   '8 7 6 5',
   '4 3 2 1',
   'Add 4 4 100',
   'Add 3 3 100',
   'Subtract -1 -1 42',
   'Subtract 0 0 42',
   'END'],
  'Invalid coordinates\nInvalid coordinates\n-41 2 3 4\n5 6 7 8\n8 7 6 5\n4 3 2 101',
  False),
 ('003_knight_game.py', [2, 'KK', 'KK'], '0', False),
 ('004_easter_bunny.py',
  [5, '1 3 7 9 11', 'X 5 4 X 63', '7 3 21 95 1', 'B 1 73 4 9', '9 2 33 2 0'],
  'right\n[3, 1]\n[3, 2]\n[3, 3]\n[3, 4]\n87',
  False),
 ('004_easter_bunny.py',
  [8,
   '4 18 9 7 24 41 52 11',
   '54 21 19 X 6 34 75 57',
   '76 67 7 44 76 27 56 37',
   '92 35 25 37 52 34 56 72',
   '35 X 1 45 4 X 37 63',
   '105 X B 2 12 43 5 19',
   '48 19 35 20 32 27 42 4',
   '73 88 78 32 37 52 X 22'],
  'down\n[6, 2]\n[7, 2]\n113',
  False),
 ('005_alice_in_wonderland.py',
  [5,
   '. A . . 1',
   'R . 2 . .',
   '4 7 . 1 .',
   '. . . 2 .',
   '. 3 . . .',
   'down',
   'right',
   'left',
   'down',
   'up',
   'left'],
  "Alice didn't make it to the tea party.\n. * . . 1\n* * * . .\n4 * . 1 .\n. . . 2 .\n. 3 . . .",
  False),
 ('005_alice_in_wonderland.py',
  [7,
   '. A . 1 1 . .',
   '9 . . . 6 . 5',
   '. 6 . R . . .',
   '. 3 . . 1 . .',
   '. . . 2 . . 2',
   '. 3 . . 1 . .',
   '. 8 3 . . . 2',
   'left',
   'down',
   'down',
   'right'],
  'She did it! She went to the party.\n'
  '* * . 1 1 . .\n'
  '* . . . 6 . 5\n'
  '* * . R . . .\n'
  '. 3 . . 1 . .\n'
  '. . . 2 . . 2\n'
  '. 3 . . 1 . .\n'
  '. 8 3 . . . 2',
  False),
 ('006_range_day.py',
  ['. . . . .',
   'x . . . .',
   '. A . . .',
   '. . . x .',
   '. x . . x',
   3,
   'shoot down',
   'move right 4',
   'move left 1'],
  'Training not completed! 3 targets left.\n[4, 1]',
  False),
 ('006_range_day.py',
  ['. . . . .', '. . . . .', '. A x . .', '. . . . .', '. x . . .', 2, 'shoot down', 'shoot right'],
  'Training completed! All 2 targets hit.\n[4, 1]\n[2, 2]',
  False),
 ('006_range_day.py',
  ['. . . . .',
   '. . . . .',
   '. . x . .',
   '. . . . .',
   '. x . . A',
   3,
   'shoot down',
   'move right 2',
   'shoot left'],
  'Training not completed! 1 targets left.\n[4, 1]',
  False),
 ('007_present_delivery.py',
  [5, 4, '- X V -', '- S - V', '- - - -', 'X - - -', 'up', 'right', 'down', 'right', 'Christmas morning'],
  '- - - -\n- - - S\n- - - -\nX - - -\nGood job, Santa! 2 happy nice kid/s.',
  False),
 ('007_present_delivery.py',
  [3, 4, '- - - -', 'V - X -', '- V C V', '- - - S', 'left', 'up'],
  'Santa ran out of presents!\n- - - -\nV - - -\n- - S -\n- - - -\nNo presents for 1 nice kid/s.',
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
