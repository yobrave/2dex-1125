"""2dex-1125: one-line AI excuse, two-day window; gate 200 chars."""

import json
import os
import pathlib
import sys

CEILING = 200


def open_ledger():
    desk = pathlib.Path(__file__).resolve().parent
    sheet = (desk / "entry.txt").read_text(encoding="utf-8")
    return desk, [e for e in (row.strip() for row in sheet.splitlines()) if e]


def book_entry(line):
    if not line:
        sys.exit("ledger error: nothing booked")
    if len(line) > CEILING:
        sys.exit("ledger error: %d chars over ceiling %d" % (len(line), CEILING))
    return line


def file_copy(desk, line):
    drawer = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or desk)
    drawer.mkdir(parents=True, exist_ok=True)
    stub = drawer / "entry.txt"
    stub.write_text(line + "\n", encoding="utf-8", newline="\n")
    return stub


desk, rows = open_ledger()
line = book_entry(rows[0] if rows else "")
stub = file_copy(desk, line)
print(json.dumps({"stub": stub.as_posix(), "chars": len(line), "over_ceiling": len(line) > CEILING, "entry_type": "excuse", "booked": True}))
