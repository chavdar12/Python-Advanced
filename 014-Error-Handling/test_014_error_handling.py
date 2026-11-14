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
STDIN_CASES = [('001_so_many_exceptions.py', ['1, 4, 5'], '20', False),
 ('001_so_many_exceptions.py', ['4, 5, 6, 1, 3'], '10', False),
 ('001_so_many_exceptions.py', ['2, 5, 10'], '1', False),
 ('003_repeat_text.py', ['Hello', 'Bye'], 'Variable times must be an integer', False),
 ('003_repeat_text.py', ['Hello', 2], 'HelloHello', False)]


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


# (script, stdin lines, expected stdout before the error, exception name)
RAISES_CASES = [('002_value_cannot_be_negative.py', [1, 4, -5, 3, 10], '', 'ValueCannotBeNegative')]


class TestRaises(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, error in RAISES_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(error, result.stderr)
                self.assertEqual(lines(result.stdout), lines(expected))


if __name__ == "__main__":
    unittest.main()
