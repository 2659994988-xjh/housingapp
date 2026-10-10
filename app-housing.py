import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Title (replace [Your Name] with your own name)
st.title("California Housing Data (1990) by XuJinghan")

# Load the dataset
df = pd.read_csv("housing.csv")

# 2. Slider: filter by minimal median house value
min_value = st.slider("Minimal Median House Value", 0, 500001, 200000)
filtered = df[df["median_house_value"] >= min_value]

# 3. Subheader pointing to the sidebar
st.subheader("See more filters in the sidebar:")

# 4. Sidebar multiselect: filter by ocean_proximity (all selected by default)
location_types = list(df["ocean_proximity"].unique())
selected_types = st.sidebar.multiselect(
    "Choose the location type",
    location_types,
    location_types,
)
filtered = filtered[filtered["ocean_proximity"].isin(selected_types)]

# 5. Sidebar radio: filter by income level using an if statement
income_level = st.sidebar.radio("Choose income level", ["Low", "Medium", "High"])
if income_level == "Low":
    filtered = filtered[filtered["median_income"] <= 2.5]
elif income_level == "Medium":
    filtered = filtered[(filtered["median_income"] > 2.5) & (filtered["median_income"] < 4.5)]
else:
    filtered = filtered[filtered["median_income"] >= 4.5]

# 6. Map of the filtered districts
st.map(filtered)

# 7. Histogram of median_house_value for the filtered districts (30 bins)
fig, ax = plt.subplots()
ax.hist(filtered["median_house_value"], bins=30)
ax.set_xlabel("Median House Value (US dollars)")
ax.set_ylabel("Number of Districts")
st.pyplot(fig)
#（注：内容由AI生成）
