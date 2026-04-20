"""Test that every example runs without error.

Each example is exec'd in isolation. If it doesn't raise, it passes.
"""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"
EXAMPLE_FILES = sorted(EXAMPLES_DIR.glob("*.py"))
EXAMPLE_FILES = [f for f in EXAMPLE_FILES if f.name != "__init__.py"]


@pytest.mark.parametrize("script", EXAMPLE_FILES, ids=lambda f: f.stem)
def test_example_runs(script):
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True, text=True, timeout=30,
        cwd=str(EXAMPLES_DIR.parent),
    )
    assert result.returncode == 0, f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    assert len(result.stdout.strip()) > 0, "Example produced no output"
