"""Smoke: installed package maps a function across a thread pool (PS-211).

Subprocess-driven (``sys.executable <tmp script>``) so this proves the
installed distribution resolves — an in-process import would not.
Hermetic: no network, no credentials, no writes outside tmp dirs.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.smoke

_PROBE = (
    "from scitex_parallel import run\n"
    "def _square(x):\n"
    "    return x * x\n"
    "print(run(_square, [(2,), (3,)], n_jobs=2))\n"
)


def test_subprocess_parallel_map_returns_ordered_results(tmp_path: Path) -> None:
    # Arrange
    probe = tmp_path / "probe_parallel.py"
    probe.write_text(_PROBE)
    argv = [sys.executable, str(probe)]

    # Act
    completed = subprocess.run(argv, capture_output=True, text=True, timeout=30)

    # Assert
    assert (completed.returncode, completed.stdout.split()) == (0, ["[4,", "9]"])
