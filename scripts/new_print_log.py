#!/usr/bin/env python3
"""
new_print_log.py

Create a dated print log file from the baseline template.

Usage:
  python3 new_print_log.py <model-name> [--dir docs/print_tests]

Example:
  python3 new_print_log.py benchy
  python3 new_print_log.py "20mm cube" --dir docs/print_tests
"""
import argparse
import datetime
import os
from pathlib import Path
import re
import sys

TEMPLATE_FILENAME = "baseline_print_log_template.md"

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return re.sub(r"_+", "_", s).strip("_")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model", help="Model name, e.g. benchy / 20mm cube / tall tower")
    parser.add_argument("--dir", default="docs/print_tests", help="Output directory for logs")
    args = parser.parse_args()

    out_dir = Path(args.dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.date.today().isoformat()
    model_slug = slugify(args.model)
    out_path = out_dir / f"{today}_{model_slug}.md"

    template_path = out_dir / TEMPLATE_FILENAME
    if not template_path.exists():
        # Try repo root docs/print_tests if run from elsewhere
        template_path = Path("docs/print_tests") / TEMPLATE_FILENAME

    if not template_path.exists():
        # Fallback minimal template if the baseline template is missing
        content = f"# Baseline Print Log\n\n- Date: {today}\n- Model: {args.model}\n\n## Notes\n"
    else:
        content = template_path.read_text(encoding="utf-8")
        # Inject today's date and model in placeholders if present
        content = content.replace("YYYY-MM-DD", today)
        content = content.replace("(Benchy / 20mm cube / tall tower / other)", args.model)

    out_path.write_text(content, encoding="utf-8")
    print(f"Created {out_path}")

if __name__ == "__main__":
    sys.exit(main())
