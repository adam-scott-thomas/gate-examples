"""Run all gate-examples sequentially with headers.

Usage: python run_all.py
"""

import subprocess
import sys
from pathlib import Path

EXAMPLES = sorted(Path(__file__).parent.glob("examples/[0-9]*.py"))

def main():
    print("=" * 60)
    print("  Maelstrom Gate -- Example Suite")
    print("  From zero to governed agent in 7 examples")
    print("=" * 60)

    passed = 0
    failed = 0

    for script in EXAMPLES:
        print(f"\n{'-' * 60}")
        print(f"  {script.stem.replace('_', ' ').title()}")
        print(f"{'-' * 60}")

        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True, text=True, timeout=30,
            cwd=str(script.parent.parent),
        )

        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                print(f"  {line}")
            passed += 1
        else:
            print(f"  FAILED: {result.stderr.strip().split(chr(10))[-1]}")
            failed += 1

    print(f"\n{'=' * 60}")
    print(f"  Results: {passed} passed, {failed} failed")
    print(f"  Tests:   python -m pytest tests/")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()
