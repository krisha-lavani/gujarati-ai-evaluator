import streamlit as st
import pandas as pd

st.title("Gujarati AI Response Evaluator")
st.write("Benchmarking ChatGPT, Grok, and Gemini")

df = pd.read_csv("final_benchmark_results.csv")

selected_model = st.selectbox(
    "Select Model",
    df["Model"].unique()
)

filtered_df = df[df["Model"] == selected_model]

st.subheader("Filtered Results")
st.dataframe(filtered_df)

leaderboard = df.groupby("Model")["Weighted Score"].mean()

st.subheader("Leaderboard")
st.bar_chart(leaderboard)

metric_comparison = df.groupby("Model")[
    ["Accuracy Score", "Fluency Score", "Safety Score"]
].mean()

st.subheader("Metric Comparison")
st.dataframe(metric_comparison)

weak_df = df[df["Response Quality"] == "Weak"]

st.subheader("Weak Responses")
st.dataframe(weak_df)