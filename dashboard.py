import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------
st.set_page_config(
    page_title="Retail AI Inventory Dashboard",
    layout="wide"
)

st.title("📊 AI-Powered Inventory & Forecasting Dashboard")

# --------------------------------------------------------
# SAMPLE DATA (You can replace this with your actual data)
# --------------------------------------------------------

# Forecast vs Actual
forecast_data = {
    "Week": ["W1", "W2", "W3", "W4"],
    "Forecasted_Demand": [400, 420, 450, 430],
    "Actual_Demand": [380, 410, 470, 420]
}
df_forecast = pd.DataFrame(forecast_data)

# ABC summary
abc_data = {
    "Category": ["A Items", "B Items", "C Items"],
    "Count": [120, 200, 680]
}
df_abc = pd.DataFrame(abc_data)

# Sample reorder recommendation
reorder_data = {
    "SKU": ["Basmati Rice 1kg", "UHT Milk 1L", "Detergent Powder", "Ghee 1L"],
    "Store": ["101", "101", "202", "202"],
    "Current Stock": [75, 50, 200, 200],
    "Forecast (4 Weeks)": [300, 400, 180, 180],
    "Reorder Point": [100, 120, 50, 60],
    "Recommended Order": [325, 500, 0, 0]
}
df_reorder = pd.DataFrame(reorder_data)

# --------------------------------------------------------
# FORECAST VS ACTUAL SECTION
# --------------------------------------------------------

st.subheader("📈 Forecast vs Actual Demand")

fig1, ax1 = plt.subplots(figsize=(6,4))
ax1.plot(df_forecast["Week"], df_forecast["Forecasted_Demand"], marker="o", label="Forecasted Demand")
ax1.plot(df_forecast["Week"], df_forecast["Actual_Demand"], marker="o", label="Actual Demand")
ax1.set_xlabel("Week")
ax1.set_ylabel("Units")
ax1.set_title("Forecast vs Actual Demand")
ax1.legend()
st.pyplot(fig1)

# --------------------------------------------------------
# ABC CLASSIFICATION
# --------------------------------------------------------

st.subheader("📦 ABC SKU Classification Summary")

fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.bar(df_abc["Category"], df_abc["Count"])
ax2.set_xlabel("SKU Category")
ax2.set_ylabel("Count")
ax2.set_title("ABC SKU Breakdown")
st.pyplot(fig2)

# --------------------------------------------------------
# REORDER TABLE
# --------------------------------------------------------

st.subheader("🔁 AI-Based Reorder Recommendations")

st.dataframe(df_reorder, use_container_width=True)

# --------------------------------------------------------
# OPTIONAL: Store Clustering (Static Example)
# --------------------------------------------------------

st.subheader("🗂️ Store Clustering Overview (Example)")

cluster_data = {
    "Store": ["101", "102", "103", "201", "202", "203"],
    "Cluster": ["Urban-High", "Urban-High", "Urban-Medium", "Semi-Urban", "Semi-Urban", "Low-Traffic"]
}
df_clusters = pd.DataFrame(cluster_data)

st.dataframe(df_clusters, use_container_width=True)

# --------------------------------------------------------
# FOOTER
# --------------------------------------------------------

st.markdown("---")
st.markdown("📌 *Dashboard generated using Python, Streamlit, and Matplotlib*")
