import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Nassau Candy Profitability Dashboard",
    page_icon="🍬",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🍬 Nassau Candy Distributor")
st.subheader("Product Line Profitability & Margin Performance Analysis")

st.markdown("---")

# -----------------------------
# LOAD DATA
# -----------------------------
# -----------------------------
# LOAD DATA
# -----------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("Nassau Candy Distributor.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        dayfirst=True
    )

    return df

df = load_data()

# -----------------------------
# KPI CALCULATIONS
# -----------------------------

df["Gross Margin %"] = (
    df["Gross Profit"] /
    df["Sales"]
) * 100

df["Profit per Unit"] = (
    df["Gross Profit"] /
    df["Units"]
)

df["Revenue Contribution"] = (
    df["Sales"] /
    df["Sales"].sum()
) * 100

df["Profit Contribution"] = (
    df["Gross Profit"] /
    df["Gross Profit"].sum()
) * 100

daily_margin = (
    df.groupby("Order Date")["Gross Margin %"]
    .mean()
)

margin_volatility = daily_margin.std()

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.header("Dashboard Filters")

# Date Filter

start_date = st.sidebar.date_input(
    "Start Date",
    df["Order Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["Order Date"].max()
)

# Division Filter

division = st.sidebar.multiselect(
    "Select Division",
    options=df["Division"].unique(),
    default=df["Division"].unique()
)

# Product Search

product = st.sidebar.text_input(
    "Search Product"
)

# Margin Slider

margin = st.sidebar.slider(
    "Minimum Gross Margin (%)",
    0,
    100,
    20
)

# -----------------------------
# APPLY FILTERS
# -----------------------------

filtered_df = df[
    (df["Order Date"] >= pd.to_datetime(start_date)) &
    (df["Order Date"] <= pd.to_datetime(end_date))
]

filtered_df = filtered_df[
    filtered_df["Division"].isin(division)
]

if product != "":

    filtered_df = filtered_df[
        filtered_df["Product Name"]
        .str.contains(product, case=False)
    ]

filtered_df = filtered_df[
    filtered_df["Gross Margin %"] >= margin
]

# -----------------------------
# CHECK DATA
# -----------------------------

st.success(
    f"Showing {len(filtered_df)} records"
)
# ======================================================
# KPI SECTION
# ======================================================

st.markdown("## 📊 Key Performance Indicators")

gross_margin = filtered_df["Gross Profit"].sum() / filtered_df["Sales"].sum() * 100
profit_per_unit = filtered_df["Gross Profit"].sum() / filtered_df["Units"].sum()
revenue_contribution = filtered_df["Sales"].sum() / df["Sales"].sum() * 100
profit_contribution = filtered_df["Gross Profit"].sum() / df["Gross Profit"].sum() * 100

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Gross Margin (%)", f"{gross_margin:.2f}%")
col2.metric("Profit per Unit", f"${profit_per_unit:.2f}")
col3.metric("Revenue Contribution", f"{revenue_contribution:.2f}%")
col4.metric("Profit Contribution", f"{profit_contribution:.2f}%")
col5.metric("Margin Volatility", f"{margin_volatility:.2f}")

st.markdown("---")

# ======================================================
# PRODUCT PROFITABILITY
# ======================================================

st.header("📦 Product Profitability Overview")

col1, col2 = st.columns(2)

# Top Profit Products

top_profit = (
    filtered_df.groupby("Product Name")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    top_profit,
    x="Gross Profit",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Gross Profit"
)

col1.plotly_chart(fig1, use_container_width=True)

# Top Margin Products

top_margin = (
    filtered_df.groupby("Product Name")["Gross Margin %"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    top_margin,
    x="Gross Margin %",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Gross Margin"
)

col2.plotly_chart(fig2, use_container_width=True)

st.subheader("Product Performance Table")

table = filtered_df[
    [
        "Product Name",
        "Sales",
        "Gross Profit",
        "Gross Margin %",
        "Profit per Unit",
        "Revenue Contribution",
        "Profit Contribution",
    ]
]

st.dataframe(table, use_container_width=True)
st.markdown("---")

st.header("🏢 Division Performance Dashboard")

col1, col2 = st.columns(2)

division_summary = (
    filtered_df.groupby("Division")[["Sales", "Gross Profit"]]
    .sum()
    .reset_index()
)

fig3 = px.bar(
    division_summary,
    x="Division",
    y=["Sales", "Gross Profit"],
    barmode="group",
    title="Revenue vs Gross Profit by Division"
)

col1.plotly_chart(fig3, use_container_width=True)

division_margin = (
    filtered_df.groupby("Division")["Gross Margin %"]
    .mean()
    .reset_index()
)

fig4 = px.bar(
    division_margin,
    x="Division",
    y="Gross Margin %",
    title="Average Gross Margin by Division"
)

col2.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# ======================================================
# COST DIAGNOSTICS
# ======================================================

st.header("💰 Cost Structure Diagnostics")

col1, col2 = st.columns(2)

fig5 = px.scatter(
    filtered_df,
    x="Cost",
    y="Sales",
    color="Division",
    hover_name="Product Name",
    size="Units",
    title="Cost vs Sales"
)

col1.plotly_chart(fig5, use_container_width=True)

filtered_df["Cost to Sales Ratio"] = (
    filtered_df["Cost"] / filtered_df["Sales"]
)

ratio = (
    filtered_df.groupby("Product Name")["Cost to Sales Ratio"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig6 = px.bar(
    ratio,
    x="Cost to Sales Ratio",
    y="Product Name",
    orientation="h",
    title="Cost to Sales Ratio"
)

col2.plotly_chart(fig6, use_container_width=True)

st.subheader("Margin Risk Table")

risk_table = filtered_df[
    [
        "Product Name",
        "Cost",
        "Sales",
        "Gross Profit",
        "Gross Margin %",
        "Cost to Sales Ratio",
    ]
]

st.dataframe(risk_table, use_container_width=True)
st.markdown("---")

st.header("📈 Profit Concentration Analysis")

col1, col2 = st.columns(2)

revenue = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig7 = px.bar(
    revenue,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Revenue Contribution by Product"
)

col1.plotly_chart(fig7, use_container_width=True)

profit = (
    filtered_df.groupby("Product Name")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig8 = px.bar(
    profit,
    x="Gross Profit",
    y="Product Name",
    orientation="h",
    title="Profit Contribution by Product"
)

col2.plotly_chart(fig8, use_container_width=True)

st.subheader("Dependency Analysis")

dependency = (
    filtered_df.groupby("Product Name")[["Sales", "Gross Profit"]]
    .sum()
    .sort_values(by="Gross Profit", ascending=False)
)

st.dataframe(dependency, use_container_width=True)

st.markdown("---")

st.success("Analysis Completed Successfully")

st.caption(
    "Developed by Tiger Kamble | Nassau Candy Distributor Profitability Dashboard"
)
