"""Repo-wide tests for the Python-Advanced exercises."""

from __future__ import annotations

import builtins
import contextlib
import io
import pathlib
import py_compile
import runpy
import sys
import types
import unittest
from unittest import mock


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_ROOT = REPO_ROOT / "013-Modules"
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from Fibonacci_sequence.fibonacci_task_functions import (  # noqa: E402
    create_fibonacci_sequence,
    locate_num_in_fibonacci,
)
from Mathematical_operations import mapper as math_mapper  # noqa: E402
from Mathematical_operations.helper_funcitons import (  # noqa: E402
    add,
    divide,
    multiply,
    power,
    subtract,
)
from Triangle.print_triangle_funcitons import (  # noqa: E402
    print_lower_part,
    print_upper_part,
    print_whole,
)


class TestRepositoryCompilation(unittest.TestCase):
    def test_all_python_files_compile(self):
        for path in REPO_ROOT.rglob("*.py"):
            if ".venv" in path.parts:
                continue
            py_compile.compile(str(path), doraise=True)


class TestReusableModules(unittest.TestCase):
    def test_fibonacci_helpers(self):
        self.assertEqual(create_fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(
            locate_num_in_fibonacci(3, [0, 1, 1, 2, 3]),
            "The number - 3 is at index 4",
        )
        self.assertEqual(
            locate_num_in_fibonacci(4, [0, 1, 1, 2, 3]),
            "The number 4 is not in the sequence",
        )

    def test_math_helpers(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(add(10, 3), 13)
        self.assertEqual(multiply(10, 3), 30)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(power(2, 3), 8)

    def test_math_mapper(self):
        self.assertSetEqual(set(math_mapper.mapper), {"-", "+", "*", "/", "^"})
        self.assertEqual(math_mapper.mapper["+"](4, 5), 9)
        self.assertEqual(math_mapper.mapper["^"](2, 4), 16)

    def test_triangle_helpers(self):
        self.assertEqual(self._capture_stdout(print_upper_part, 3), "*\n**\n***\n")
        self.assertEqual(self._capture_stdout(print_lower_part, 3), "**\n*\n")
        self.assertEqual(
            self._capture_stdout(print_whole, 3),
            "*\n**\n***\n**\n*\n",
        )

    @staticmethod
    def _capture_stdout(func, *args, **kwargs):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            func(*args, **kwargs)
        return buffer.getvalue()


class TestModuleEntryPoints(unittest.TestCase):
    def test_calculate_logarithm_natural(self):
        ns, output = self._run_path(
            REPO_ROOT / "013-Modules" / "1.Calculate_logarithm.py",
            ["10", "natural"],
        )
        self.assertIn("get_result", ns)
        self.assertEqual(output, "2.30\n")

    def test_calculate_logarithm_custom_base(self):
        _, output = self._run_path(
            REPO_ROOT / "013-Modules" / "1.Calculate_logarithm.py",
            ["8", "2"],
        )
        self.assertEqual(output, "3.00\n")

    def test_ascii_art_script_and_function(self):
        fake_pyfiglet = types.ModuleType("pyfiglet")

        def figlet_format(message):
            return f"art:{message}"

        class FakeFiglet:
            def renderText(self, text):
                return f"render:{text}"

        fake_pyfiglet.figlet_format = figlet_format
        fake_pyfiglet.Figlet = FakeFiglet

        with mock.patch.dict(sys.modules, {"pyfiglet": fake_pyfiglet}):
            ns, output = self._run_path(
                REPO_ROOT / "013-Modules" / "2.ASCII_Art.py",
                ["hello"],
            )

        self.assertIn("print_art", ns)
        self.assertIn("art:hello", output)
        self.assertIn("render:text to render", output)

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            ns["print_art"]("bye")
        self.assertEqual(buffer.getvalue(), "art:bye\n")

    def test_fibonacci_main(self):
        output = self._run_module(
            "Fibonacci_sequence.main",
            ["Create sequence 5", "Locate 3", "Stop"],
        )
        self.assertEqual(output, "0 1 1 2 3\nThe number - 3 is at index 4\n")

    def test_mathematical_operations_main(self):
        output = self._run_module("Mathematical_operations.main", ["2 + 3"])
        self.assertEqual(output, "5.00\n")

    def test_triangle_main(self):
        output = self._run_module("Triangle.main", ["3"])
        self.assertEqual(output, "*\n**\n***\n**\n*\n")

    def _run_path(self, path: pathlib.Path, inputs: list[str]):
        buffer = io.StringIO()
        with mock.patch.object(builtins, "input", side_effect=inputs):
            with contextlib.redirect_stdout(buffer):
                ns = runpy.run_path(str(path), run_name="__main__")
        return ns, buffer.getvalue()

    def _run_module(self, module_name: str, inputs: list[str]):
        buffer = io.StringIO()
        with mock.patch.object(builtins, "input", side_effect=inputs):
            with contextlib.redirect_stdout(buffer):
                runpy.run_module(module_name, run_name="__main__")
        return buffer.getvalue()

