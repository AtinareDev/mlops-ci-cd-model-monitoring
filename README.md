\# MLOps CI/CD Model Monitoring



!\[Pipeline](https://github.com/AtinareDev/mlops-ci-cd-model-monitoring/actions/workflows/mlops.yml/badge.svg)



Pipeline MLOps orientado a producción para entrenar, validar y monitorizar modelos de machine learning mediante un flujo CI/CD automatizado.



El proyecto automatiza el ciclo de validación de un modelo, bloqueando ejecuciones inválidas y publicando únicamente los resultados aprobados en GitHub Pages.



\## Enlaces



\- \*\*Repositorio:\*\* https://github.com/AtinareDev/mlops-ci-cd-model-monitoring

\- \*\*Reporte en GitHub Pages:\*\* https://atinaredev.github.io/mlops-ci-cd-model-monitoring/



\## Descripción general



Este proyecto implementa un pipeline CI/CD para un modelo de machine learning con foco en calidad, reproducibilidad y validación automática.



El flujo ejecuta controles de calidad de código, pruebas unitarias, entrenamiento del modelo, validación de métricas y generación de un reporte HTML desplegado automáticamente en GitHub Pages.



El modelo solo se considera apto cuando supera los umbrales mínimos definidos para `accuracy`, `precision` y `recall`.



\## Características principales



\- Pipeline CI/CD automatizado con GitHub Actions.

\- Gestión del entorno con `uv`.

\- Ejecución con Python 3.14.

\- Validación de calidad de código con `ruff`.

\- Validación de formato con `ruff format`.

\- Chequeo estático de tipos con `ty`.

\- Pruebas unitarias con `pytest`.

\- Entrenamiento automático del modelo.

\- Validación automática de métricas.

\- Generación de reporte HTML.

\- Despliegue automático en GitHub Pages.

\- Proyecto preparado para portfolio técnico.



\## Criterios de aceptación



Un modelo solo se acepta si todas las etapas del pipeline se ejecutan correctamente.



| Etapa | Requisito |

|---|---|

| Calidad de código | `ruff check` debe pasar sin errores |

| Formato | `ruff format --check` debe pasar correctamente |

| Tipos | `ty check` debe pasar sin errores |

| Tests | `pytest` debe ejecutar todas las pruebas correctamente |

| Entrenamiento | Debe generarse una nueva versión del modelo |

| Validación | `accuracy`, `precision` y `recall` deben ser al menos 80% |

| Reporte | Debe generarse y publicarse el reporte HTML |



Si cualquier etapa falla, el pipeline se detiene y el modelo queda rechazado.



\## Flujo del pipeline



El pipeline sigue este orden:



```text

Push o Pull Request

&#x20;       |

&#x20;       v

Validación de calidad de código

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

Despliegue automático en GitHub Pages

```



\## Métricas mínimas requeridas



Para que un modelo sea aceptado, debe cumplir estos umbrales mínimos:



| Métrica | Umbral mínimo |

|---|---:|

| Accuracy | 80% |

| Precision | 80% |

| Recall | 80% |



Ejemplo de archivo de métricas generado por el pipeline:



```json

{

&#x20; "accuracy": 1.0,

&#x20; "precision": 1.0,

&#x20; "recall": 1.0

}

```



\## Reporte publicado



El pipeline genera automáticamente un reporte HTML con la última ejecución aprobada.



El reporte incluye:



\- Estado de validación del modelo.

\- Métricas principales.

\- Identificador del modelo entrenado.

\- Fecha de entrenamiento.

\- Detalles de clasificación.

\- Confirmación de que el modelo supera los umbrales mínimos.



Reporte disponible en:



```text

https://atinaredev.github.io/mlops-ci-cd-model-monitoring/

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

│       ├── \_\_init\_\_.py

│       ├── \_\_main\_\_.py

│       ├── metrics.py

│       ├── ml.py

│       ├── utils.py

│       └── pipelines/

│           ├── \_\_init\_\_.py

│           ├── train\_pipeline.py

│           └── validate\_pipeline.py

├── tests/

│   ├── test\_metrics.py

│   ├── test\_ml.py

│   ├── test\_pipelines.py

│   └── test\_utils.py

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



El workflow se ejecuta automáticamente en cada `push` o `pull request` hacia la rama `main`.



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



Este proyecto demuestra un flujo MLOps automatizado en el que los modelos se prueban, validan y publican únicamente cuando cumplen criterios mínimos de calidad.



El pipeline permite iterar sobre nuevas configuraciones del modelo de forma segura, manteniendo controles automáticos antes de considerar una versión como válida para producción.



\## Autor



Proyecto desarrollado por \[AtinareDev](https://github.com/AtinareDev).

