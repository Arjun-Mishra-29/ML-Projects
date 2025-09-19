# Copilot Instructions for ML_Project

## Project Overview
This is an end-to-end machine learning project structured for modularity and reproducibility. The codebase is organized into distinct components for data ingestion, transformation, model training, and prediction, following a pipeline architecture.

## Key Directories & Files
- `src/componenets/`: Core ML logic
  - `data_ingestion.py`: Loads and splits raw data
  - `data_transformation.py`: Cleans, preprocesses, and transforms data
  - `Model_trainer.py`: Trains and evaluates models
  - `pipeline/`: Orchestrates end-to-end workflows (`predict_pipeline.py`, `trai_pipeline.py`)
- `notebook/`: Jupyter notebooks for EDA and model experimentation
- `artifacts/`: Stores datasets and model artifacts
- `logs/`: Timestamped log files for debugging and audit trails
- `requirements.txt`, `setup.py`: Dependency management

## Architectural Patterns
- **Pipeline-first design:** Each ML stage is encapsulated in a module and orchestrated via pipeline scripts.
- **Artifacts directory:** All outputs (data splits, models) are saved to `artifacts/` for reproducibility.
- **Logging:** All major operations log to timestamped files in `logs/`.
- **Exception handling:** Custom exceptions are defined in `src/exception.py` and used across modules.

## Developer Workflows
- **Run pipelines:** Execute scripts in `src/pipeline/` to run full data-to-prediction workflows.
- **Experiment in notebooks:** Use `notebook/EDA.ipynb` and `notebook/Model_Trainig.ipynb` for interactive analysis.
- **Debugging:** Check `logs/` for detailed error and process logs.
- **Dependencies:** Install with `pip install -r requirements.txt`.

## Project-Specific Conventions
- **File naming:** Consistent use of underscores and camel case for module names (e.g., `Model_trainer.py`).
- **Data location:** All input data is expected in `artifacts/` or `notebook/data/`.
- **Component boundaries:** Each ML stage is a separate Python module; avoid mixing responsibilities.
- **Custom logging:** Use `src/logger.py` for all logging needs.

## Integration Points
- **External data:** Data is loaded from CSV files in `artifacts/` and `notebook/data/`.
- **No cloud or external APIs** are referenced in the current structure.

## Example Patterns
- To add a new preprocessing step, update `data_transformation.py` and ensure outputs are saved to `artifacts/`.
- To extend model training, modify `Model_trainer.py` and update pipeline scripts accordingly.
