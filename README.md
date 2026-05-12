\# MLOps CI/CD Model Monitoring



Pipeline MLOps orientado a producción para entrenar, validar y monitorizar modelos de machine learning mediante un flujo CI/CD automatizado.



El proyecto implementa un sistema de validación que bloquea modelos inválidos antes de su despliegue y publica un reporte HTML con los últimos resultados aprobados en GitHub Pages.



!\[Pipeline](https://github.com/AtinareDev/mlops-ci-cd-model-monitoring/actions/workflows/mlops.yml/badge.svg)



\## Reporte en vivo



\[Ver reporte en GitHub Pages](https://atinaredev.github.io/mlops-ci-cd-model-monitoring/)



\## Repositorio



\[Ver repositorio en GitHub](https://github.com/AtinareDev/mlops-ci-cd-model-monitoring)



\## Descripción general



Este proyecto implementa un flujo MLOps automatizado para validar modelos de machine learning antes de considerarlos aptos para producción.



El pipeline ejecuta controles de calidad de código, pruebas unitarias, entrenamiento del modelo, validación de métricas y generación de un reporte visual publicado automáticamente.



El objetivo principal es asegurar que solo los modelos que cumplen criterios mínimos de calidad puedan ser aceptados.



\## Características principales



\- Pipeline CI/CD automatizado con GitHub Actions

\- Gestión del entorno con `uv`

\- Ejecución con Python 3.14

\- Validación de calidad de código con `ruff`

\- Validación de formato con `ruff format`

\- Chequeo estático de tipos con `ty`

\- Pruebas unitarias con `pytest`

\- Entrenamiento automático del modelo

\- Validación automática de métricas

\- Control de aceptación basado en accuracy, precision y recall

\- Generación de reporte HTML

\- Despliegue automático en GitHub Pages

\- Proyecto preparado para portfolio técnico



\## Criterios de aceptación del modelo



Un modelo se considera válido solo si todas las etapas del pipeline se ejecutan correctamente.



| Etapa | Requisito |

|---|---|

| Linting | `ruff check` debe pasar sin errores |

| Formato | `ruff format --check` debe pasar correctamente |

| Tipos | `ty check` debe pasar sin errores |

| Tests | `pytest` debe ejecutar todas las pruebas correctamente |

| Entrenamiento | Debe generarse una nueva versión del modelo |

| Validación | Accuracy, precision y recall deben ser al menos 80% |

| Reporte | Debe generarse y publicarse el reporte HTML |



Si cualquier etapa falla, el pipeline se detiene y el modelo queda rechazado.



\## Flujo del pipeline



```mermaid

flowchart LR

&#x20;   A\[Push o Pull Request] --> B\[Calidad de código]

&#x20;   B --> C\[Pruebas unitarias]

&#x20;   C --> D\[Entrenamiento del modelo]

&#x20;   D --> E\[Validación de métricas]

&#x20;   E --> F\[Generación del reporte HTML]

&#x20;   F --> G\[Despliegue en GitHub Pages]



&#x20;   B -. fallo .-> X\[Pipeline fallido]

&#x20;   C -. fallo .-> X

&#x20;   D -. fallo .-> X

&#x20;   E -. fallo .-> X

```



\## Puerta de validación de métricas



Para que un modelo sea aceptado, debe cumplir los siguientes umbrales mínimos:



| Métrica | Mínimo requerido |

|---|---:|

| Accuracy | 80% |

| Precision | 80% |

| Recall | 80% |



Ejemplo del archivo de métricas generado:



```json

{

&#x20; "accuracy": 1.0,

&#x20; "precision": 1.0,

&#x20; "recall": 1.0

}

```



\## Estructura del repositorio



```text

.

├── .github/

│   └── workflows/

│       └── mlops.yml

├── data/

│   ├── train.csv

│   ├── test.csv

│   └── validate.csv

├── scripts/

│   ├── build\_report.py

│   ├── run\_model\_pipeline.py

│   └── validate\_metrics.py

├── src/

│   └── revolutionary\_mlops/

│       ├── metrics.py

│       ├── ml.py

│       ├── utils.py

│       └── pipelines/

├── tests/

├── pyproject.toml

├── uv.lock

└── README.md

```



\## Ejecución local



\### 1. Clonar el repositorio



```bash

git clone https://github.com/AtinareDev/mlops-ci-cd-model-monitoring.git

cd mlops-ci-cd-model-monitoring

```



\### 2. Ejecutar tests



```bash

uv run pytest -q

```



\### 3. Ejecutar controles de calidad



```bash

uv run --with ruff ruff check .

uv run --with ruff ruff format --check .

uv run --with ty ty check .

```



\### 4. Entrenar y validar el modelo



```bash

uv run python scripts/run\_model\_pipeline.py

uv run python scripts/validate\_metrics.py --threshold 0.80

```



\### 5. Generar el reporte HTML



```bash

uv run python scripts/build\_report.py

```



El reporte se genera en:



```text

public/index.html

```



\## CI/CD con GitHub Actions



El workflow se ejecuta automáticamente en cada push o pull request hacia la rama `main`.



Etapas del workflow:



1\. Validación de calidad de código

2\. Validación de formato

3\. Chequeo estático de tipos

4\. Ejecución de pruebas unitarias

5\. Entrenamiento del modelo

6\. Validación de métricas mínimas

7\. Generación de reporte HTML

8\. Despliegue automático en GitHub Pages



Solo las ejecuciones exitosas generan un reporte publicado.



\## GitHub Pages



El reporte de resultados se publica automáticamente en:



```text

https://atinaredev.github.io/mlops-ci-cd-model-monitoring/

```



La página muestra información de la última ejecución aprobada, incluyendo métricas del modelo, estado de validación y detalles del pipeline.



\## Tecnologías utilizadas



\- Python

\- uv

\- GitHub Actions

\- GitHub Pages

\- Pytest

\- Ruff

\- Ty

\- HTML

\- JSON

\- MLOps

\- CI/CD



\## Resultado esperado



Al finalizar una ejecución correcta del pipeline:



\- El código pasa los controles de calidad.

\- Las pruebas unitarias se ejecutan correctamente.

\- El modelo se entrena automáticamente.

\- Las métricas superan el umbral mínimo del 80%.

\- Se genera un reporte HTML.

\- El reporte queda disponible públicamente en GitHub Pages.



\## Autor



Proyecto desarrollado por \[AtinareDev](https://github.com/AtinareDev).

