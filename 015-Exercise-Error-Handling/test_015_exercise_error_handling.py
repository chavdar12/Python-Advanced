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
STDIN_CASES = [('001_numbers_dictionary.py',
  ['one', 1, 'two', 2, 'Search', 'one', 'Remove', 'two', 'End'],
  "1\n{'one': 1}",
  False),
 ('001_numbers_dictionary.py',
  ['one', 'two', 'Search', 'Remove', 'End'],
  'The variable number must be an integer\n{}',
  False),
 ('001_numbers_dictionary.py',
  ['one', 1, 'Search', 'one', 'Remove', 'two', 'End'],
  "1\nNumber does not exist in dictionary\n{'one': 1}",
  False)]


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


# (script, stdin lines, expected stdout before the error, exception name)
RAISES_CASES = [('002_email_validator.py', ['abc@abv.bg'], '', 'NameTooShortError'),
 ('002_email_validator.py',
  ['peter@gmail.com', 'petergmail.com'],
  'Email is valid',
  'MustContainAtSymbolError'),
 ('002_email_validator.py', ['peter@gmail.hotmail'], '', 'InvalidDomainError')]


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
