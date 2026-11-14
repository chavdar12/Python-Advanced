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
STDIN_CASES = [('001_absolute_values.py', ['1 2.5 -3 -4.5'], '[1.0, 2.5, 3.0, 4.5]', False),
 ('002_rounding.py', ['1.0 2.5 3.0 4.5'], '[1, 2, 3, 4]', False),
 ('006_character_combinations.py', ['abc'], 'abc\nacb\nbac\nbca\ncba\ncab', True),
 ('007_character_combinations_with_perm.py', ['abc'], 'abc\nacb\nbac\nbca\ncba\ncab', True),
 ('008_character_combinations_with_permutations.py', ['abc'], 'abc\nacb\nbac\nbca\ncba\ncab', True),
 ('009_character_combinations_printing.py', ['abc'], 'abc\nacb\nbac\nbca\ncba\ncab', True),
 ('010_chairs.py', ['Peter, George, Amy', 2], 'Peter, George\nPeter, Amy\nGeorge, Amy', False),
 ('011_expressions.py',
  ['1, 1, 1, 1'],
  '+1+1+1+1=4\n'
  '+1+1+1-1=2\n'
  '+1+1-1+1=2\n'
  '+1+1-1-1=0\n'
  '+1-1+1+1=2\n'
  '+1-1+1-1=0\n'
  '+1-1-1+1=0\n'
  '+1-1-1-1=-2\n'
  '-1+1+1+1=2\n'
  '-1+1+1-1=0\n'
  '-1+1-1+1=0\n'
  '-1+1-1-1=-2\n'
  '-1-1+1+1=0\n'
  '-1-1+1-1=-2\n'
  '-1-1-1+1=-2\n'
  '-1-1-1-1=-4',
  False)]


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


# (script, expression evaluated against the script's namespace, expected value)
FUNCTION_CASES = [('003_multiplication_function.py', 'multiply(1, 4, 5)', 20),
 ('003_multiplication_function.py', 'multiply(4, 5, 6, 1, 3)', 360),
 ('003_multiplication_function.py', 'multiply(2, 0, 1000, 5000)', 0),
 ('004_operate.py', 'operate("+", 1, 2, 3)', 6),
 ('004_operate.py', 'operate("*", 3, 4)', 12),
 ('005_person_info.py',
  'get_info(**{"name": "George", "town": "Sofia", "age": 20})',
  'This is George from Sofia and he is 20 years old')]


class TestFunctions(unittest.TestCase):
    def test_examples(self):
        for script, expression, expected in FUNCTION_CASES:
            with self.subTest(script=script, expression=expression):
                with contextlib.redirect_stdout(io.StringIO()):
                    namespace = runpy.run_path(str(HERE / script), run_name="lesson")
                    self.assertEqual(eval(expression, namespace), expected)


if __name__ == "__main__":
    unittest.main()
