import streamlit as st
import pandas as pd

# Title
st.title("Gujarati AI Response Evaluator Dashboard")
st.markdown("Benchmarking ChatGPT vs Grok vs Gemini using custom Gujarati NLP metrics")

# Load data
df = pd.read_csv("final_benchmark_results.csv")

# Project Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Models Tested", 3)
col2.metric("Prompts", 25)
col3.metric("Total Responses", len(df))

# Leaderboard
st.subheader("Model Leaderboard")
leaderboard = df.groupby("Model")["Weighted Score"].mean().sort_values(ascending=False)
st.dataframe(leaderboard)
st.bar_chart(leaderboard)

# Step 4: Metric Comparison Chart
st.subheader("Metric Comparison")
metric_scores = df.groupby("Model")[["Fluency Score", "Accuracy Score", "Safety Score"]].mean()
st.bar_chart(metric_scores)
st.dataframe(metric_scores)

# Model Filter
selected_model = st.selectbox(
    "Select Model",
    df["Model"].unique()
)

filtered_df = df[df["Model"] == selected_model]

# Filtered Results
st.subheader("Filtered Results")
st.dataframe(filtered_df)

# Weak Responses
weak_df = df[df["Response Quality"] == "Weak"]
st.subheader("Weak Responses")
st.dataframe(weak_df)

# Step 5: About Section
st.markdown("---")
st.write("Built by Krisha Lavani")
st.write("Tech Stack: Python, Streamlit, Pandas, NLP")
