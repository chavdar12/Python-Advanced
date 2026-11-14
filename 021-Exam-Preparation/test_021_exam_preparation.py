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
STDIN_CASES = [('001_fireworks_show.py',
  ['5, 6, 4, 16, 11, 5, 30, 2, 3, 27', '1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22'],
  'Congrats! You made the perfect firework show!\n'
  'Palm Fireworks: 4\n'
  'Willow Fireworks: 3\n'
  'Crossette Fireworks: 3',
  False),
 ('001_fireworks_show.py',
  ['-15, -8, 0, -16, 0, -22', '10, 5'],
  "Sorry. You can't make the perfect firework show.\n"
  'Explosive Power left: 10, 5\n'
  'Palm Fireworks: 0\n'
  'Willow Fireworks: 0\n'
  'Crossette Fireworks: 0',
  False),
 ('002_darts.py',
  ['Ivan, Peter',
   '12 21 18 4 20 7 11',
   '9 D D D D D 10',
   '15 D T T T D 3',
   '2 D T B T D 19',
   '17 D T T T D 6',
   '22 D D D D D 14',
   '5 8 23 13 16 1 24',
   '(3, 3)'],
  'Ivan won the game with 1 throws!',
  False),
 ('002_darts.py',
  ['George, Hristo',
   '17 8 21 6 13 3 24',
   '16 D D D D D 14',
   '7 D T T T D 15',
   '23 D T B T D 2',
   '9 D T T T D 22',
   '19 D D D D D 10',
   '12 18 4 20 5 11 1',
   '(1, 0)',
   '(2, 3)',
   '(0, 0)',
   '(4, 2)',
   '(5, 1)',
   '(3, 1)',
   '(0, 0)',
   '(2, 3)'],
  'Hristo won the game with 4 throws!',
  False)]


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


# (script, expression evaluated against the script's namespace, expected value)
FUNCTION_CASES = [('003_cupcake_shop.py',
  'stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry")',
  ['choco', 'vanilla', 'banana', 'caramel', 'berry']),
 ('003_cupcake_shop.py',
  'stock_availability(["chocolate", "vanilla", "banana"], "sell")',
  ['vanilla', 'banana']),
 ('003_cupcake_shop.py', 'stock_availability(["chocolate", "vanilla", "banana"], "sell", 3)', []),
 ('003_cupcake_shop.py',
  'stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate")',
  ['banana']),
 ('003_cupcake_shop.py',
  'stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie")',
  ['chocolate', 'vanilla', 'banana'])]


class TestFunctions(unittest.TestCase):
    def test_examples(self):
        for script, expression, expected in FUNCTION_CASES:
            with self.subTest(script=script, expression=expression):
                with contextlib.redirect_stdout(io.StringIO()):
                    namespace = runpy.run_path(str(HERE / script), run_name="lesson")
                    self.assertEqual(eval(expression, namespace), expected)


if __name__ == "__main__":
    unittest.main()
