import argparse
import html
import json
from datetime import datetime, timezone
from pathlib import Path


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def percent(value: float | int | None) -> str:
    if value is None:
        return "N/A"
    return f"{float(value) * 100:.2f}%"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metrics", type=Path, default=Path("artifacts/metrics.json"))
    parser.add_argument(
        "--model-info", type=Path, default=Path("artifacts/model_info.json")
    )
    parser.add_argument("--output-dir", type=Path, default=Path("public"))
    args = parser.parse_args()

    metrics = load_json(args.metrics)
    model_info = load_json(args.model_info)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    accuracy = percent(metrics.get("accuracy"))
    precision = percent(metrics.get("precision"))
    recall = percent(metrics.get("recall"))

    model_id = html.escape(str(model_info.get("model_id", "N/A")))
    trained_at = html.escape(str(model_info.get("trained_at", "N/A")))
    generated_at = datetime.now(timezone.utc).isoformat()

    html_content = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>MLOps Model Report</title>
  <style>
    body {{
      margin: 0;
      font-family: Arial, sans-serif;
      background: #0f172a;
      color: #e5e7eb;
    }}
    main {{
      max-width: 1000px;
      margin: 0 auto;
      padding: 48px 24px;
    }}
    .hero {{
      background: linear-gradient(135deg, #1e293b, #334155);
      border: 1px solid #475569;
      border-radius: 24px;
      padding: 32px;
      box-shadow: 0 20px 50px rgba(0,0,0,.35);
    }}
    h1 {{
      margin: 0 0 12px;
      font-size: 42px;
    }}
    .subtitle {{
      color: #cbd5e1;
      font-size: 18px;
      line-height: 1.6;
    }}
    .status {{
      display: inline-block;
      margin-top: 24px;
      padding: 10px 16px;
      border-radius: 999px;
      background: #14532d;
      color: #bbf7d0;
      font-weight: bold;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 18px;
      margin-top: 24px;
    }}
    .card {{
      background: #111827;
      border: 1px solid #374151;
      border-radius: 18px;
      padding: 24px;
    }}
    .label {{
      color: #94a3b8;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: .08em;
    }}
    .value {{
      margin-top: 10px;
      font-size: 34px;
      font-weight: bold;
    }}
    .section {{
      margin-top: 24px;
      background: #111827;
      border: 1px solid #374151;
      border-radius: 18px;
      padding: 24px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 12px;
    }}
    th, td {{
      text-align: left;
      padding: 12px;
      border-bottom: 1px solid #374151;
    }}
    th {{
      color: #cbd5e1;
    }}
    code {{
      color: #93c5fd;
    }}
    footer {{
      margin-top: 32px;
      color: #94a3b8;
      font-size: 14px;
    }}
  </style>
</head>
<body>
  <main>
    <section class="hero">
      <h1>MLOps CI/CD Model Monitoring</h1>
      <p class="subtitle">
        Reporte automático de validación del modelo generado por el pipeline CI/CD.
        El modelo solo se acepta cuando supera los umbrales mínimos de calidad.
      </p>
      <div class="status">Modelo aprobado</div>
    </section>

    <section class="grid">
      <article class="card">
        <div class="label">Accuracy</div>
        <div class="value">{accuracy}</div>
      </article>
      <article class="card">
        <div class="label">Precision</div>
        <div class="value">{precision}</div>
      </article>
      <article class="card">
        <div class="label">Recall</div>
        <div class="value">{recall}</div>
      </article>
    </section>

    <section class="section">
      <h2>Información del modelo</h2>
      <table>
        <tr><th>Campo</th><th>Valor</th></tr>
        <tr><td>Model ID</td><td><code>{model_id}</code></td></tr>
        <tr><td>Fecha de entrenamiento</td><td>{trained_at}</td></tr>
        <tr><td>Fuente de métricas</td><td>{html.escape(str(model_info.get("metrics_source", "N/A")))}</td></tr>
        <tr><td>Seed</td><td>{html.escape(str(model_info.get("seed", "N/A")))}</td></tr>
      </table>
    </section>

    <section class="section">
      <h2>Detalles de validación</h2>
      <table>
        <tr><th>Métrica</th><th>Valor</th></tr>
        <tr><td>Total</td><td>{html.escape(str(metrics.get("total", "N/A")))}</td></tr>
        <tr><td>True Positives</td><td>{html.escape(str(metrics.get("tp", "N/A")))}</td></tr>
        <tr><td>False Positives</td><td>{html.escape(str(metrics.get("fp", "N/A")))}</td></tr>
        <tr><td>False Negatives</td><td>{html.escape(str(metrics.get("fn", "N/A")))}</td></tr>
        <tr><td>True Negatives</td><td>{html.escape(str(metrics.get("tn", "N/A")))}</td></tr>
      </table>
    </section>

    <footer>
      Reporte generado automáticamente: {html.escape(generated_at)}
    </footer>
  </main>
</body>
</html>
"""

    output_file = args.output_dir / "index.html"
    output_file.write_text(html_content, encoding="utf-8")
    print(f"report_saved={output_file}")


if __name__ == "__main__":
    main()
