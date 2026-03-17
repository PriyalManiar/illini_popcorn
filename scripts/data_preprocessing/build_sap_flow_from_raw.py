from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


RAW_COLS = ("realdate", "svalue_1", "svalue_2", "svalue_3", "svalue_4")


def _parse_realdate(s: str) -> datetime | None:
    s = (s or "").strip()
    if not s:
        return None
    try:
        return datetime.strptime(s, "%m/%d/%y %H:%M")
    except ValueError:
        return None


def _format_realdate(dt: datetime) -> str:
    return f"{dt.month}/{dt.day}/{dt.year % 100:02d} {dt.hour}:{dt.minute:02d}"


def _safe_float(x: str) -> float | None:
    try:
        return float(x)
    except Exception:
        return None


def convert_one(raw_path: Path, out_path: Path) -> None:
    with raw_path.open("r", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or any(c not in reader.fieldnames for c in RAW_COLS):
            raise ValueError(f"{raw_path} must have header: {','.join(RAW_COLS)}")

        out_rows: list[list[str]] = []
        for row in reader:
            dt = _parse_realdate(row.get("realdate", ""))
            if dt is None:
                continue

            vals = [_safe_float(row.get(c, "")) for c in RAW_COLS[1:]]
            vals2 = [v for v in vals if v is not None]
            if not vals2:
                continue
            sap_flow_mean = sum(vals2) / len(vals2)

            out_rows.append([_format_realdate(dt), f"{sap_flow_mean:.9g}"])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("realdate", "sap_flow_mean"))
        w.writerows(out_rows)


def main() -> int:
    p = argparse.ArgumentParser(description="Build sap_flow_sensor CSVs from raw sensor CSVs.")
    p.add_argument("--raw-dir", default="data/sap/raw", help="Directory containing sensor1.csv and sensor2.csv")
    p.add_argument("--out-dir", default="data/sap", help="Output directory for sap_flow_sensor1/2.csv")
    args = p.parse_args()

    root = Path(__file__).resolve().parents[2]
    raw_dir = (root / args.raw_dir).resolve()
    out_dir = (root / args.out_dir).resolve()

    convert_one(raw_dir / "sensor1.csv", out_dir / "sap_flow_sensor1.csv")
    convert_one(raw_dir / "sensor2.csv", out_dir / "sap_flow_sensor2.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

