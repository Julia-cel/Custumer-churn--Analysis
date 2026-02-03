import streamlit as st

import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Customer Churn Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Customer Churn Analysis Dashboard")
st.markdown(
    "##### Business-focused dashboard to identify key drivers of customer churn and support retention strategies."
)

@st.cache_data
def load_data():
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return df

df = load_data()
st.sidebar.header("Filters")

##Adding filters

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Payment Method",
    options=df["PaymentMethod"].unique(),
    default=df["PaymentMethod"].unique()
)

filtered_df = df[
    (df["Contract"].isin(contract_filter)) &
    (df["PaymentMethod"].isin(payment_filter))
]
## Writing key metrics
st.markdown("## Key Business Metrics")
col1, col2, col3, col4 = st.columns(4)

churn_rate = (filtered_df["Churn"] == "Yes").mean() * 100
avg_tenure = filtered_df["tenure"].mean()
avg_monthly = filtered_df["MonthlyCharges"].mean()
num_customers= len(filtered_df)

col1.metric("Churn Rate (%)", f"{churn_rate:.1f}%")
col2.metric("Number of Customers", f"{num_customers:,}")
col3.metric("Average Tenure (months)", f"{avg_tenure:.1f}")
col4.metric("Avg Monthly Charges ($)", f"{avg_monthly:.2f}")

##Adding plot

st.markdown("## Average Monthly Charges by Churn Status")

avg_charges_churn = (
    filtered_df
    .groupby("Churn")["MonthlyCharges"]
    .mean()
    .reset_index()
)

fig_charges = px.bar(
    avg_charges_churn,
    x="Churn",
    y="MonthlyCharges",
    color="Churn",
    text_auto=".1f"
)

fig_charges.update_layout(
    yaxis_title="Average Monthly Charges ($)",
    xaxis_title="Churn Status"
)

st.plotly_chart(fig_charges, use_container_width=True)


churn_contract = (
    filtered_df
    .groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="Churn Rate")
)
st.markdown("## Main Churn Drivers")
col1, col2 = st.columns(2)
fig_contract = px.bar(
    churn_contract,
    x="Contract",
    y="Churn Rate",
    color="Contract",
    text_auto=".1f",
    title="Churn Rate by Contract Type"
)

col1.plotly_chart(fig_contract, use_container_width=True)

churn_payment = (
    filtered_df
    .groupby("PaymentMethod")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="Churn Rate")
)

fig_payment = px.bar(
    churn_payment,
    x="PaymentMethod",
    y="Churn Rate",
    color="PaymentMethod",
    text_auto=".1f",
    title="Churn Rate by Payment Method"
)

col2.plotly_chart(fig_payment, use_container_width=True)

st.markdown("## Understanding the Root Cause Behind High Churn")
col3, col4 = st.columns(2)
ContractVSPayMet = pd.crosstab(filtered_df.PaymentMethod, filtered_df.Contract, normalize='index').loc['Electronic check'] * 100
fig_contract_payment = px.bar(
    x=ContractVSPayMet.index,
    y=ContractVSPayMet.values,
    color=ContractVSPayMet.index,
    labels={'x': 'Contract Type', 'y': 'Percentage of Customers (%)'},
    title="Contract Type Distribution for Electronic Check Payment Method"
)

col3.plotly_chart(fig_contract_payment, use_container_width=True)

avg_tenure_contract = (
    filtered_df
    .groupby("Contract")["tenure"]
    .mean()
    .reset_index()
)
fig_tenure_contract = px.bar(
    avg_tenure_contract,
    x="Contract",
    y="tenure",
    color="Contract",
    text_auto=".1f",
    title="Average Tenure by Contract Type")

fig_tenure_contract.update_layout(
    yaxis_title="Average Tenure (months)",
    xaxis_title="Contract Type"
)

col4.plotly_chart(fig_tenure_contract, use_container_width=True)

st.markdown("## Customer Loyalty and Retention")

fig_tenure = px.histogram(
    filtered_df,
    x="tenure",
    color="Churn",
    nbins=30,
    title="Tenure Distribution by Churn Status")
fig_tenure.update_layout(
    yaxis_title="Number of Customers",
    xaxis_title="Tenure (months)"
)

st.plotly_chart(fig_tenure, use_container_width=True)