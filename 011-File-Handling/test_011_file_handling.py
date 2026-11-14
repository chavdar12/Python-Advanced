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


class TestFileHandling(unittest.TestCase):
    """Runs the scripts in a temporary copy of this lesson, so files they create never touch the repo."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.lesson = shutil.copytree(HERE, self.tmp / HERE.name)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_script(self, name):
        return run(name, [], cwd=self.lesson)

    def test_opener_and_reader(self):
        self.assertEqual(self.run_script("001_file_opener.py").stdout.strip(), "File found")
        self.assertEqual(self.run_script("002_file_reader.py").stdout.strip(), "15")

    def test_writer_and_delete(self):
        self.run_script("003_file_writer.py")
        self.assertEqual((self.lesson / "my_first_file.txt").read_text(), "I just created my first file!")
        self.assertEqual(self.run_script("004_file_delete.py").stdout, "")
        self.assertEqual(self.run_script("004_file_delete.py").stdout.strip(), "File already deleted!")
        self.assertEqual(self.run_script("005_file_delete_if_exists.py").returncode, 0)

    def test_word_count(self):
        for name in ("006_word_count.py", "007_word_count_with_functions.py"):
            with self.subTest(name=name):
                self.run_script(name)
                self.assertEqual(lines((self.lesson / "output.txt").read_text()), ["is - 3", "quick - 2", "fault - 1"])


if __name__ == "__main__":
    unittest.main()
