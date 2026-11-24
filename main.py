#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning label (1-120 chars) to /output/entry.txt and prints it.
"""
import os

LINE = "WARNING: Do not meet yourself. If you do, do not lend yourself money. You will not pay yourself back."

assert 1 <= len(LINE) <= 120, f"line must be 1-120 chars, got {len(LINE)}"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(LINE)
