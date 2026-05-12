\# MLOps CI/CD Model Monitoring



!\[Pipeline](https://github.com/AtinareDev/mlops-ci-cd-model-monitoring/actions/workflows/mlops.yml/badge.svg)



Pipeline MLOps orientado a producción para entrenar, validar y monitorizar modelos de machine learning mediante un flujo CI/CD automatizado.



El proyecto valida automáticamente cada ejecución del modelo y solo publica resultados cuando se cumplen los criterios mínimos de calidad.



\## Enlaces



\- Repositorio: https://github.com/AtinareDev/mlops-ci-cd-model-monitoring

\- Reporte en GitHub Pages: https://atinaredev.github.io/mlops-ci-cd-model-monitoring/



\## Descripción



Este proyecto implementa un pipeline CI/CD para un modelo de machine learning.



El flujo automatizado ejecuta controles de calidad, pruebas unitarias, entrenamiento del modelo, validación de métricas y generación de un reporte HTML publicado en GitHub Pages.



El modelo solo se considera válido si supera los umbrales mínimos de accuracy, precision y recall.



\## Características principales



\- Pipeline CI/CD con GitHub Actions.

\- Gestión del entorno con `uv`.

\- Ejecución con Python 3.14.

\- Linting con `ruff`.

\- Validación de formato con `ruff format`.

\- Chequeo estático de tipos con `ty`.

\- Tests unitarios con `pytest`.

\- Entrenamiento automático del modelo.

\- Validación automática de métricas.

\- Generación de reporte HTML.

\- Despliegue automático en GitHub Pages.



\## Criterios de aceptación



Un modelo solo se acepta si todas las etapas del pipeline se ejecutan correctamente.



| Etapa | Requisito |

|---|---|

| Linting | `ruff check` debe pasar sin errores |

| Formato | `ruff format --check` debe pasar correctamente |

| Tipos | `ty check` debe pasar sin errores |

| Tests | `pytest` debe pasar correctamente |

| Entrenamiento | Debe generarse una nueva versión del modelo |

| Validación | Accuracy, precision y recall deben ser al menos 80% |

| Reporte | Debe generarse y publicarse el reporte HTML |



Si cualquier etapa falla, el pipeline se detiene y el modelo queda rechazado.



\## Flujo del pipeline



```text

Push o Pull Request

&#x20;       |

&#x20;       v

Calidad de código

&#x20;       |

&#x20;       v

Pruebas unitarias

&#x20;       |

&#x20;       v

Entrenamiento del modelo

&#x20;       |

&#x20;       v

Validación de métricas

&#x20;       |

&#x20;       v

Generación del reporte HTML

&#x20;       |

&#x20;       v

Despliegue en GitHub Pages

```



\## Métricas mínimas requeridas



| Métrica | Umbral mínimo |

|---|---:|

| Accuracy | 80% |

| Precision | 80% |

| Recall | 80% |



Ejemplo de archivo de métricas generado:



```json

{

&#x20; "accuracy": 1.0,

&#x20; "precision": 1.0,

&#x20; "recall": 1.0

}

```



\## Estructura del proyecto



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



Clonar el repositorio:



```bash

git clone https://github.com/AtinareDev/mlops-ci-cd-model-monitoring.git

cd mlops-ci-cd-model-monitoring

```



Ejecutar tests:



```bash

uv run pytest -q

```



Ejecutar controles de calidad:



```bash

uv run --with ruff ruff check .

uv run --with ruff ruff format --check .

uv run --with ty ty check .

```



Entrenar y validar el modelo:



```bash

uv run python scripts/run\_model\_pipeline.py

uv run python scripts/validate\_metrics.py --threshold 0.80

```



Generar el reporte HTML:



```bash

uv run python scripts/build\_report.py

```



El reporte se genera en:



```text

public/index.html

```



\## CI/CD



El workflow se ejecuta automáticamente en cada push o pull request hacia la rama `main`.



Etapas del workflow:



1\. Validación de calidad de código.

2\. Validación de formato.

3\. Chequeo estático de tipos.

4\. Ejecución de pruebas unitarias.

5\. Entrenamiento del modelo.

6\. Validación de métricas mínimas.

7\. Generación del reporte HTML.

8\. Despliegue automático en GitHub Pages.



Solo las ejecuciones exitosas generan un reporte publicado.



\## GitHub Pages



El reporte de resultados se publica automáticamente en:



```text

https://atinaredev.github.io/mlops-ci-cd-model-monitoring/

```



La página muestra la última ejecución aprobada del pipeline, incluyendo las métricas del modelo y detalles de validación.



\## Tecnologías utilizadas



\- Python

\- uv

\- GitHub Actions

\- GitHub Pages

\- pytest

\- ruff

\- ty

\- HTML

\- JSON

\- MLOps

\- CI/CD



\## Resultado



El proyecto demuestra un flujo MLOps automatizado donde los modelos se prueban, validan y publican únicamente cuando cumplen los criterios mínimos de calidad definidos.



\## Autor



Proyecto desarrollado por \[AtinareDev](https://github.com/AtinareDev).

