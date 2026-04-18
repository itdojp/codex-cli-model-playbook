#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_MODELS = [
    "gpt-5.4",
    "gpt-5.4-mini",
    "gpt-5.3-codex",
    "gpt-5.3-codex-spark",
    "gpt-5.2",
    "gpt-5.2-codex",
    "gpt-5.1-codex-max",
    "gpt-5.1-codex-mini",
]

ERROR_RE = re.compile(r'"message":"([^"]+)"')


def extract_note(stdout: str, stderr: str) -> str | None:
    combined = (stdout or "") + "\n" + (stderr or "")
    match = ERROR_RE.search(combined)
    if match:
        return match.group(1)
    if "OK" in combined:
        return "OK"
    return None


def check_model(model: str, timeout: int, summary_only: bool) -> dict:
    cmd = [
        "codex",
        "exec",
        "-m",
        model,
        "--skip-git-repo-check",
        "Reply with OK only.",
    ]
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    combined = (proc.stdout or "") + (proc.stderr or "")
    supported = proc.returncode == 0 and "OK" in combined
    note = extract_note(proc.stdout, proc.stderr)
    result = {
        "model": model,
        "supported": supported,
        "returncode": proc.returncode,
        "note": note,
    }
    if not summary_only:
        result["stdout"] = proc.stdout
        result["stderr"] = proc.stderr
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Check which Codex models are actually runnable in the current account.")
    parser.add_argument("--models", nargs="*", default=DEFAULT_MODELS)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--summary-only", action="store_true", help="Write only model, support status, return code, and extracted note.")
    args = parser.parse_args()

    results = []
    for model in args.models:
        try:
            result = check_model(model, args.timeout, args.summary_only)
        except subprocess.TimeoutExpired:
            result = {
                "model": model,
                "supported": False,
                "returncode": None,
                "note": f"timeout after {args.timeout} seconds",
            }
        results.append(result)
        status = "SUPPORTED" if result["supported"] else "UNSUPPORTED"
        print(f"[{status}] {model}")

    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": "check_codex_model_support.py",
        "summary_only": args.summary_only,
        "results": results,
    }

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"wrote: {args.output}")
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
