"""E2E: fan a 20-item workload out to real pool threads, gather in order (PS-212).

The full story — ``run()`` spreads twenty tuple-args across four real
worker threads with auto CPU-count fallback available, and the gathered
list preserves input order with the correct checksum. Real threads, real
filesystem, no network. Gated on ``RUN_E2E=1`` (skipped by default).
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = [
    pytest.mark.e2e,
    pytest.mark.skipif(
        os.environ.get("RUN_E2E") != "1",
        reason="e2e: set RUN_E2E=1 to run end-to-end workflows",
    ),
]

_PROBE = (
    "from scitex_parallel import run\n"
    "def _square(x):\n"
    "    return x * x\n"
    "results = run(_square, [(i,) for i in range(20)], n_jobs=4)\n"
    "print(list(results))\n"
    "print(sum(results))\n"
)


def test_parallel_map_preserves_order_over_twenty_items(tmp_path: Path) -> None:
    # Arrange
    probe = tmp_path / "probe_e2e.py"
    probe.write_text(_PROBE)
    argv = [sys.executable, str(probe)]
    expected = [str(list(i * i for i in range(20))), "2470"]

    # Act
    completed = subprocess.run(argv, capture_output=True, text=True, timeout=60)

    # Assert
    assert (completed.returncode, completed.stdout.splitlines()) == (0, expected)
