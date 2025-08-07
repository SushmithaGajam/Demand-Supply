import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🧵 Telangana Clothes Demand vs Supply Dashboard")

# Constants
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
cloth_types = ['Cotton', 'Silk', 'Denim', 'Wool', 'Linen']
regions = ['North', 'South', 'East', 'West', 'Central']

# Generate Sample Data
data = {
    'Month': [],
    'Region': [],
    'Cloth_Type': [],
    'Demand_Units': [],
    'Supply_Units': [],
}

for month in months:
    for _ in range(10):  # 10 entries per month
        data['Month'].append(month)
        data['Region'].append(random.choice(regions))
        data['Cloth_Type'].append(random.choice(cloth_types))
        data['Demand_Units'].append(random.randint(500, 1500))
        data['Supply_Units'].append(random.randint(500, 1500))

# Create DataFrame
df = pd.DataFrame(data)

# ====== Section 1: Show Full Table ======
st.subheader("📋 Full Monthly Data (Simulated)")
st.dataframe(df)

# ====== Section 2: Monthly Demand vs Supply Bar Chart ======
st.subheader("📊 Monthly Total Demand vs Supply")
monthly_group = df.groupby('Month')[['Demand_Units', 'Supply_Units']].sum()

fig1, ax1 = plt.subplots(figsize=(10, 5))
monthly_group.plot(kind='bar', ax=ax1)
ax1.set_title("Monthly Demand vs Supply")
ax1.set_ylabel("Units")
ax1.set_xlabel("Month")
ax1.grid(True)
st.pyplot(fig1)

# ====== Section 3: Demand Share by Cloth Type ======
st.subheader("📈 Demand Share by Cloth Type")
demand_share = df.groupby('Cloth_Type')['Demand_Units'].sum()

fig2, ax2 = plt.subplots(figsize=(6, 6))
ax2.pie(demand_share, labels=demand_share.index, autopct='%1.1f%%', startangle=140)
ax2.set_title("Cloth Type Demand Share")
st.pyplot(fig2)

# ====== Section 4: Supply Distribution by Region ======
st.subheader("🏙️ Supply Distribution by Region")
supply_by_region = df.groupby('Region')['Supply_Units'].sum()

fig3, ax3 = plt.subplots(figsize=(8, 5))
ax3.bar(supply_by_region.index, supply_by_region.values)
ax3.set_title("Supply Distribution by Region")
ax3.set_ylabel("Supply Units")
ax3.set_xlabel("Region")
ax3.grid(True)
st.pyplot(fig3)

# ====== Section 5: Summary Tables ======
st.subheader("🧾 Summary Tables")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**📦 Monthly Demand Summary**")
    monthly_demand = df.groupby('Month')['Demand_Units'].sum().reset_index()
    st.dataframe(monthly_demand)

with col2:
    st.markdown("**🎨 Demand Share by Category**")
    demand_df = demand_share.reset_index().rename(columns={'Demand_Units': 'Demand_Share'})
    st.dataframe(demand_df)

with col3:
    st.markdown("**🌍 Supply by Region**")
    supply_df = supply_by_region.reset_index().rename(columns={'Supply_Units': 'Supply_By_Region'})
    st.dataframe(supply_df)

# Optional Download
st.download_button("📥 Download Full Dataset as CSV",
                   data=df.to_csv(index=False),
                   file_name='telangana_demand_supply.csv',
                   mime='text/csv')
