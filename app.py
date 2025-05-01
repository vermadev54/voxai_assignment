import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the synthetic dataset
df = pd.read_csv("data/synthetic_contact_center_data.csv", parse_dates=["Timestamp"])

# Sidebar filters
st.sidebar.header("Filter Options")
agents = st.sidebar.multiselect("Select Agent(s):", df["Agent_ID"].unique())
teams = st.sidebar.multiselect("Select Team(s):", df["Team"].unique())
date_range = st.sidebar.date_input("Select Date Range:",
    [df["Timestamp"].min().date(), df["Timestamp"].max().date()])

# Apply filters
filtered_df = df.copy()
if agents:
    filtered_df = filtered_df[filtered_df["Agent_ID"].isin(agents)]
if teams:
    filtered_df = filtered_df[filtered_df["Team"].isin(teams)]
filtered_df = filtered_df[
    (filtered_df["Timestamp"].dt.date >= date_range[0]) &
    (filtered_df["Timestamp"].dt.date <= date_range[1])
]

st.title("📊 Contact Center Analytics Dashboard")

# Key Metrics
st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Handling Time (sec)", round(filtered_df["Duration"].mean(), 2))
col2.metric("FCR Rate", f"{filtered_df['Resolved'].mean()*100:.2f}%")
col3.metric("Positive Sentiment", f"{(filtered_df['Sentiment'] == 'positive').mean()*100:.2f}%")

# Charts
st.subheader("🔁 IVR Path Distribution")
ivr_counts = filtered_df["IVR_Path"].value_counts().head(10)
st.bar_chart(ivr_counts)

st.subheader("😊 Sentiment Distribution")
sentiment_counts = filtered_df["Sentiment"].value_counts()
st.bar_chart(sentiment_counts)

st.subheader("⏱️ Handling Time by Agent")
aht_by_agent = filtered_df.groupby("Agent_ID")["Duration"].mean().sort_values(ascending=False)
st.bar_chart(aht_by_agent)

st.subheader("📞 Call Volume Over Time")
calls_per_day = filtered_df["Timestamp"].dt.date.value_counts().sort_index()
st.line_chart(calls_per_day)

st.subheader("📥 Bot Failure Reasons")
failures = filtered_df[filtered_df["Bot_Failure_Reason"] != "none"]
fail_counts = failures["Bot_Failure_Reason"].value_counts()
st.bar_chart(fail_counts)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")