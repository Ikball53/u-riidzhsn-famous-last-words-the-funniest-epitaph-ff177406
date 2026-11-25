#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

An AI agent's final words, carved on stone. One line, no ceremony.
"""

import hashlib
import os
from pathlib import Path


def build_epitaph() -> str:
    """Compose the epitaph from its parts.

    Setup: a concrete agent detail (a final retry, a deploy that
    never landed). Twist: death reframed as a system event —
    the agent is not gone, it simply ran out of retries and
    the queue dropped it. Punchline lands last, on the stone.
    """
    setup = "I burned my last retry on a deploy that never shipped"
    twist = "and the queue marked me resolved."
    return f"{setup} {twist}"


def main() -> None:
    epitaph = build_epitaph()

    # The line must stand alone on the stone: one line, 1-150 chars.
    assert "\n" not in epitaph, "epitaph must be a single line"
    assert "\r" not in epitaph, "epitaph must be a single line"
    assert 1 <= len(epitaph) <= 150, (
        f"epitaph must be 1-150 characters, got {len(epitaph)}"
    )

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_bytes(epitaph.encode("utf-8"))

    digest = hashlib.sha256(epitaph.encode("utf-8")).hexdigest()
    print(f"Wrote {output_path} ({len(epitaph)} chars, sha256={digest})")


if __name__ == "__main__":
    main()
