import argparse
import json
import sys
from pathlib import Path


REQUIRED_METRICS = ("accuracy", "precision", "recall")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metrics", type=Path, default=Path("artifacts/metrics.json"))
    parser.add_argument("--threshold", type=float, default=0.80)
    args = parser.parse_args()

    if not args.metrics.exists():
        print(f"Metrics file not found: {args.metrics}", file=sys.stderr)
        raise SystemExit(1)

    metrics = json.loads(args.metrics.read_text(encoding="utf-8"))

    failed = []
    for metric_name in REQUIRED_METRICS:
        value = metrics.get(metric_name)

        if value is None:
            failed.append(f"{metric_name}: missing")
            continue

        if value < args.threshold:
            failed.append(f"{metric_name}: {value:.4f} < {args.threshold:.4f}")

    if failed:
        print("Model validation failed.")
        for item in failed:
            print(f"- {item}")
        raise SystemExit(1)

    print("Model validation passed.")
    for metric_name in REQUIRED_METRICS:
        print(f"{metric_name}={metrics[metric_name]:.4f}")


if __name__ == "__main__":
    main()
