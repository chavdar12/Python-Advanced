"""Folder-grouped compile tests for every Python file in the repo."""

from __future__ import annotations

import pathlib
import py_compile
import unittest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".idea", ".venv", "tests"}


def compile_source(path: pathlib.Path) -> None:
    py_compile.compile(str(path), doraise=True)


def sanitize(text: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in text).strip("_")


def make_compile_test(path: pathlib.Path):
    def test(self):
        compile_source(path)

    return test


def build_test_class(folder: pathlib.Path):
    attrs = {}
    for py_file in sorted(folder.rglob("*.py"), key=lambda p: str(p.relative_to(folder))):
        method_name = f"test_{sanitize(str(py_file.relative_to(REPO_ROOT)))}"
        attrs[method_name] = make_compile_test(py_file)

    class_name = f"Test{sanitize(folder.name)}Files"
    return type(class_name, (unittest.TestCase,), attrs)


for folder in sorted(
    [p for p in REPO_ROOT.iterdir() if p.is_dir() and p.name not in SKIP_DIRS],
    key=lambda p: p.name,
):
    test_class = build_test_class(folder)
    globals()[test_class.__name__] = test_class

del test_class

