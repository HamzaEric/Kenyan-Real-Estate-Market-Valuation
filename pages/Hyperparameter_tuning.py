import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from pathlib import Path


st.set_page_config(layout="wide")
st.title("Model Building & Hyperparameter Tuning")
st.markdown("---")
col1,col2 = st.columns(2)
with col1:
    st.image("images/housing Market.jpg")
with col2:
    results_df = pd.DataFrame({
        "Model Strategy": [
            "Standard Linear Regression (OLS)",
            "Manual Ridge (α=0.1)",
            "Manual Lasso (α=0.1)",
            "Optimized RidgeCV",
            "Optimized LassoCV"
        ],
        "Train RMSE (KSh)": [
            24993041.79,
            24993107.33,
            24993041.79,
            25106404.76,
            24993120.13
        ],
        "Test RMSE (KSh)": [
            25084263.00,
            25081666.51,
            25084264.08,
            25294474.21,
            25078562.37
        ],
        "Generalization Gap (%)": [
            0.3650,
            0.3543,
            0.3650,
            0.7491,
            0.3419
        ]
    })

    st.subheader("Model Performance Comparison")

    st.dataframe(
        results_df.style.format({
            "Train RMSE (KSh)": "{:,.2f}",
            "Test RMSE (KSh)": "{:,.2f}",
            "Generalization Gap (%)": "{:.4f}%"
        }),
        use_container_width=True,
        hide_index=True
    )
st.markdown("---")
st.subheader("Jupyter Notebook")
html_file = Path(r"html_files/Model_Building & Hyperparameter _Tuning.html")
components.html(html_file.read_text(),height=1000,scrolling=True)
st.markdown("---")
