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
STDIN_CASES = [('001_diagonal_difference.py', [3, '11 2 4', '4 5 6', '10 8 -12'], '15', False),
 ('002_squares_in_matrix.py', ['3 4', 'A B B D', 'E B B B', 'I J B B'], '2', False),
 ('002_squares_in_matrix.py', ['2 2', 'a b', 'c d'], '0', False),
 ('003_maximal_sum.py',
  ['4 5', '1 5 5 2 4', '2 1 4 14 3', '3 7 11 2 8', '4 8 12 16 4'],
  'Sum = 75\n1 4 14\n7 11 2\n8 12 16',
  False),
 ('004_matrix_shuffling.py',
  ['2 3', '1 2 3', '4 5 6', 'swap 0 0 1 1', 'swap 10 9 8 7', 'swap 0 1 1 0', 'END'],
  '5 2 3\n4 1 6\nInvalid input!\n5 4 3\n2 1 6',
  False),
 ('004_matrix_shuffling.py',
  ['1 2', 'Hello World', '0 0 0 1', 'swap 0 0 0 1', 'swap 0 1 0 0', 'END'],
  'Invalid input!\nWorld Hello\nHello World',
  False),
 ('005_snake_moves.py', ['5 6', 'SoftUni'], 'SoftUn\nUtfoSi\nniSoft\nfoSinU\ntUniSo', False),
 ('006_knight_game.py', [5, '0K0K0', 'K000K', '00K00', 'K000K', '0K0K0'], '1', False),
 ('006_knight_game.py', [2, 'KK', 'KK'], '0', False),
 ('006_knight_game.py',
  [8, '0K0KKK00', '0K00KKKK', '00K0000K', 'KKKKKK0K', 'K0K0000K', 'KK00000K', '00K0K000', '000K00KK'],
  '12',
  False),
 ('008_miner.py',
  [5, 'up right right up right', '* * * c *', '* * * e *', '* * c * *', 's * * c *', '* * c * *'],
  'Game over! (1, 3)',
  False),
 ('009_miner_with_game_over_flag.py',
  [5, 'up right right up right', '* * * c *', '* * * e *', '* * c * *', 's * * c *', '* * c * *'],
  'Game over! (1, 3)',
  False),
 ('008_miner.py',
  [4, 'up right right right down', '* * * e', '* * c *', '* s * c', '* * * *'],
  'You collected all coals! (2, 3)',
  False),
 ('009_miner_with_game_over_flag.py',
  [4, 'up right right right down', '* * * e', '* * c *', '* s * c', '* * * *'],
  'You collected all coals! (2, 3)',
  False),
 ('008_miner.py',
  [6,
   'left left down right up left left down down down',
   '* * * * * *',
   'e * * * c *',
   '* * c s * *',
   '* * * * * *',
   'c * * * c *',
   '* * c * * *'],
  '3 coals left. (5, 0)',
  False),
 ('009_miner_with_game_over_flag.py',
  [6,
   'left left down right up left left down down down',
   '* * * * * *',
   'e * * * c *',
   '* * c s * *',
   '* * * * * *',
   'c * * * c *',
   '* * c * * *'],
  '3 coals left. (5, 0)',
  False),
 ('010_radioactive_mutant_vampire_bunnies.py',
  ['5 8', '.......B', '...B....', '....B..B', '........', '..P.....', 'ULLL'],
  'BBBBBBBB\nBBBBBBBB\nBBBBBBBB\n.BBBBBBB\n..BBBBBB\nwon: 3 0',
  False),
 ('010_radioactive_mutant_vampire_bunnies.py',
  ['4 5', '.....', '.....', '.B...', '...P.', 'LLLLLLLL'],
  '.B...\nBBB..\nBBBB.\nBBB..\ndead: 3 1',
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
