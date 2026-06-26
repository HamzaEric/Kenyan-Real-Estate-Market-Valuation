# Houses Price Prediction

## Kenyan Real Estate Valuation Engine

An end-to-end machine learning application that predicts residential property market values in Kenya using regularized linear regression modeling. The architecture features an automated data preprocessing pipeline and a cascading user interface built with Streamlit, deployed to serve real-time baseline valuations.

---


## Project Architecture & Machine Learning Pipeline

This repository transitions a raw real estate dataset through feature engineering, rigorous statistical optimization, and web serialization:

1. **Data Cleaning & Harmonization:** Standardizes noisy, street-level geographic fields using regex-based cleaning operations.
2. **Feature Engineering:** Maps precise local coordinates and neighborhoods into broad macroeconomic development sectors (**Zoning Tiers**) using deterministic rule-based mapping blocks.
3. **Preprocessing Pipeline:** Employs a Scikit-Learn `ColumnTransformer` to seamlessly apply `OneHotEncoder` to categorical string metrics and scale numerical dimensions.
4. **Regularization Optimization:** Combines 5-fold cross-validation with an $L_1$ penalty (**LassoCV**) to drive redundant, low-signal sparse feature weights completely to absolute zero, successfully defeating the Bias-Variance tradeoff.

###  Model Evaluation Scoreboard
Our structural validation curves yielded an incredibly tight generalization profile across linear strategies:

| Model Strategy | Train RMSE | Test RMSE | Generalization Gap (%) | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Simple Mean Baseline** | 40,183,897.19 KSh | 40,183,897.19 KSh | 0.00% | Benchmark Floor |
| **Standard Linear Regression** | 24,993,041.79 KSh | 25,084,263.00 KSh | 0.3650% | Unconstrained Baseline |
| **Optimized RidgeCV ($\alpha=10$)** | 25,106,404.76 KSh | 25,294,474.21 KSh | 0.7491% | Over-smoothed Weights |
| **Optimized LassoCV ($\alpha=1000$)** | **24,993,120.13 KSh** | **25,078,562.37 KSh** | **0.3419%** |  **Production Champion** |

---
