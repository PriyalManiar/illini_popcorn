from __future__ import annotations

import argparse
import csv
import math
import random
from datetime import datetime
from pathlib import Path

COLS = ("realdate", "svalue_1", "svalue_2", "svalue_3", "svalue_4")


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


def _curve(dt: datetime, *, peak_hour: float, sigma_hours: float) -> float:
    t = dt.hour + dt.minute / 60.0
    x = (t - peak_hour) / sigma_hours
    return math.exp(-(x * x))


def _day_mod(day_of_year: int) -> float:
    return 1.0 + 0.10 * math.sin(2 * math.pi * (day_of_year / 31.0))


def _gen_value(
    rng: random.Random,
    dt: datetime,
    *,
    amplitude: float,
    base: float,
    peak_hour: float,
    sigma_hours: float,
) -> float:
    c = _curve(dt, peak_hour=peak_hour, sigma_hours=sigma_hours)
    dm = _day_mod(dt.timetuple().tm_yday)

    v = base + amplitude * c * dm + rng.gauss(0.0, amplitude * 0.035)

    if c < 0.12:
        v = base + rng.gauss(0.0, base * 0.15)
        if rng.random() < 0.01:
            v -= rng.uniform(0.005, 0.03)

    return v


def synthesize_file(path_in: Path, path_out: Path, *, seed: int, amplitude: float) -> None:
    rows: list[dict[str, str]] = []
    with path_in.open("r", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or any(c not in reader.fieldnames for c in COLS):
            raise ValueError(f"{path_in} must have header: {','.join(COLS)}")
        for row in reader:
            dt = _parse_realdate(row.get("realdate", ""))
            if dt is None:
                continue
            rows.append({"realdate": _format_realdate(dt)})

    rng1 = random.Random(seed + 1)
    rng2 = random.Random(seed + 2)
    rng3 = random.Random(seed + 3)
    rng4 = random.Random(seed + 4)

    out_rows: list[list[str]] = []
    for r in rows:
        dt = _parse_realdate(r["realdate"])
        assert dt is not None
        v1 = _gen_value(rng1, dt, amplitude=amplitude * 0.90, base=0.01, peak_hour=14.0, sigma_hours=4.5)
        v2 = _gen_value(rng2, dt, amplitude=amplitude * 0.75, base=0.01, peak_hour=14.0, sigma_hours=4.5)
        v3 = _gen_value(rng3, dt, amplitude=amplitude * 0.40, base=0.01, peak_hour=14.0, sigma_hours=4.5)
        v4 = _gen_value(rng4, dt, amplitude=amplitude * 0.55, base=0.01, peak_hour=14.0, sigma_hours=4.5)
        out_rows.append(
            [
                r["realdate"],
                f"{v1:.9g}",
                f"{v2:.9g}",
                f"{v3:.9g}",
                f"{v4:.9g}",
            ]
        )

    path_out.parent.mkdir(parents=True, exist_ok=True)
    with path_out.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(COLS)
        writer.writerows(out_rows)


def main() -> int:
    p = argparse.ArgumentParser(description="Generate synthetic raw sap sensor CSVs.")
    p.add_argument("--input-dir", default="sensor_data", help="Directory containing sensor1.csv and sensor2.csv")
    p.add_argument("--output-dir", default="data/sap/raw", help="Output directory for raw sensor CSVs")
    p.add_argument("--seed", type=int, default=1337, help="Random seed for reproducibility")
    args = p.parse_args()

    root = Path(__file__).resolve().parents[2]
    input_dir = (root / args.input_dir).resolve()
    output_dir = (root / args.output_dir).resolve()

    synthesize_file(
        input_dir / "sensor1.csv",
        output_dir / "sensor1.csv",
        seed=args.seed,
        amplitude=0.28,
    )
    synthesize_file(
        input_dir / "sensor2.csv",
        output_dir / "sensor2.csv",
        seed=args.seed + 100,
        amplitude=0.70,
    )

    nb_in = input_dir / "sensor_preprocessing.ipynb"
    if nb_in.exists():
        (output_dir / "sensor_preprocessing.ipynb").write_bytes(nb_in.read_bytes())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

