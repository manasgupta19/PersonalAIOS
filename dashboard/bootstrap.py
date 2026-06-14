from pathlib import Path
import sys


ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

root = str(ROOT)

if root not in sys.path:

    sys.path.insert(
        0,
        root
    )