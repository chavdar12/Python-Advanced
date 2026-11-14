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
STDIN_CASES = [('001_even_numbers.py', ['1 2 3 4'], '[2, 4]', False),
 ('002_sort.py', ['6 2 4'], '[2, 4, 6]', False),
 ('003_min_max_and_sum.py',
  ['2 4 6'],
  'The minimum number is 2\nThe maximum number is 6\nThe sum number is: 12',
  False),
 ('004_negative_vs_positive.py',
  ['1 2 -3 -4 65 -98 12 57 -84'],
  '-189\n137\nThe negatives are stronger than the positives',
  False),
 ('005_odd_or_even.py', ['Odd', '1 3 5 34 7 9 12 11 13 10'], '490', False)]


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


# (script, expression evaluated against the script's namespace, expected value)
FUNCTION_CASES = [('006_arguments_length.py', 'args_length(1, 32, 5)', 3),
 ('006_arguments_length.py', 'args_length([1, 2, 3])', 1),
 ('007_concatenate.py', 'concatenate("Soft", "Uni", "Is", "Great", "!")', 'SoftUniIsGreat!'),
 ('008_even_or_odd.py', 'even_odd(1, 2, 3, 4, 5, 6, "even")', [2, 4, 6]),
 ('008_even_or_odd.py', 'even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd")', [1, 3, 5, 7, 9]),
 ('009_function_executor.py',
  'func_executor((lambda a, b: a + b, (1, 2)), (lambda a, b: a * b, (2, 4)))',
  [3, 8]),
 ('010_keyword_arguments_length.py', "kwargs_length(**{'name': 'Peter', 'age': 25})", 2),
 ('011_age_assignment.py', 'age_assignment("Peter", "George", G=26, P=19)', {'George': 26, 'Peter': 19}),
 ('012_recursion_palindrome.py', 'palindrome("abcba", 0)', 'abcba is a palindrome'),
 ('012_recursion_palindrome.py', 'palindrome("peter", 0)', 'peter is not a palindrome'),
 ('013_recursive_power.py', 'recursive_power(2, 10)', 1024),
 ('013_recursive_power.py',
  'recursive_power(10, 100)',
  10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)]


class TestFunctions(unittest.TestCase):
    def test_examples(self):
        for script, expression, expected in FUNCTION_CASES:
            with self.subTest(script=script, expression=expression):
                with contextlib.redirect_stdout(io.StringIO()):
                    namespace = runpy.run_path(str(HERE / script), run_name="lesson")
                    self.assertEqual(eval(expression, namespace), expected)


if __name__ == "__main__":
    unittest.main()
