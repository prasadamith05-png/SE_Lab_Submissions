# Software Engineering Lab: Data Version Control & Experiment Tracking

**Course:** Software Engineering (UE24CS341A / pesse A)  
**Institution:** PES University, Bengaluru  
**Student:** Amith Prasad | **Roll No:** 33 (`PES1UG24AM033`)  
**Upstream Source:** `https://github.com/anantha-bit/DVC_Assignment` & `https://github.com/anantha-bit/MLflow_Assignment`  
**Student GitHub Repos:** [prasadamith05-png/dvc](https://github.com/prasadamith05-png/dvc) & [prasadamith05-png/ML-FLOW](https://github.com/prasadamith05-png/ML-FLOW)  

---

## 1. Overview
Modern software engineering for intelligent and data-intensive systems requires rigorous version control not just for source code, but also for large data assets, pipeline steps, and model evaluation metrics. This lab assignment covers two industry-standard tools:
1. **Data Version Control (DVC):** Versioning large data files outside git while maintaining git-trackable pointer files.
2. **MLflow:** End-to-end machine learning lifecycle management, parameter logging, metric tracking, and model artifact registration.

---

## 2. Part A: DVC Assignment (`DVC_Assignment/`)
- **Key Concepts:**
  - Initializing DVC repository (`dvc init`).
  - Tracking data assets (`data.txt.dvc`).
  - Configuring remote storage cache (`.dvc/config`).
  - Reproducible data pipelines and git-dvc synchronization.

---

## 3. Part B: MLflow Assignment (`MLflow_Assignment/`)
- **Key Concepts:**
  - Tracking experiments with `mlflow.start_run()`.
  - Logging hyper-parameters: `n_estimators=100`, `max_depth=3`, `random_state=42`.
  - Logging metrics: `accuracy`.
  - Saving model artifacts (`mlflow.sklearn.log_model`).
  - Visualizing runs via MLflow Web UI (`mlflow ui`).

### Running MLflow:
```bash
cd MLflow_Assignment
python train.py
mlflow ui
```
