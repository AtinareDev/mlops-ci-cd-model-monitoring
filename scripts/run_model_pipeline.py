import argparse
import json
import random
from datetime import datetime, timezone
from pathlib import Path

from revolutionary_mlops.pipelines.train_pipeline import run_training_pipeline
from revolutionary_mlops.pipelines.validate_pipeline import run_validation_pipeline


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--metrics-output", type=Path, default=Path("artifacts/metrics.json")
    )
    parser.add_argument(
        "--model-info-output", type=Path, default=Path("artifacts/model_info.json")
    )
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    random.seed(args.seed)

    model_id = run_training_pipeline()
    validation_metrics = run_validation_pipeline(model_id=model_id)

    metrics = dict(validation_metrics)

    model_info = {
        "model_id": model_id,
        "trained_at": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "metrics_source": "validation",
    }

    write_json(args.metrics_output, metrics)
    write_json(args.model_info_output, model_info)

    print(f"metrics_saved={args.metrics_output}")
    print(f"model_info_saved={args.model_info_output}")


if __name__ == "__main__":
    main()
