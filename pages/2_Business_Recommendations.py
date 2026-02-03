import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df= pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

st.set_page_config(
    page_title="Business Recommendations and Impact Analysis",
    layout="wide"
)

st.title("Business Recommendations and Impact Analysis")

st.markdown("#### Actionable insights and estimated business impact based on customer churn analysis")

st.info("These recommendations are based on the key insights derived from the Churn Analysis Dashboard.")

st.markdown("""
#### Incentivize Long-Term Contracts
*   **Insight:** Customers with month-to-month contracts exhibit significantly higher churn rates, while those with one-year and two-year contracts show much lower churn.
*   **Action:** Offer discounts or exclusive benefits (e.g., free streaming service add-on) for customers who switch to **1-year** or **2-year** contracts.

#### Focus on New Customer Onboarding
*   **Insight:** Customer tenure is a critical driver of retention: churn is heavily concentrated in the first months of the customer lifecycle, particularly within the first three months.
*   **Action:** Implement a robust **onboarding program** for the first 3-6 months. This could include proactive check-in calls, tutorials on using services, and dedicated support lines.

#### Enhance Customer Support for High-Risk Segments
*   **Insight:** Churn risk is highly concentrated among customers with month-to-month contracts, electronic check payments, and low tenure. These attributes frequently overlap, creating a small but disproportionately high-risk customer segment.
*   **Action:** Implement targeted retention actions for these customers early in their lifecycle, such as proactive outreach, payment method incentives (e.g., encouraging auto-pay), and contract migration offers. Focusing on this segment maximizes churn reduction impact while minimizing operational cost.
""")


churn_by_contract = (
    df.groupby("Contract")["Churn"]
      .apply(lambda x: (x == "Yes").mean())
)

mtm = df[df["Contract"] == "Month-to-month"]
mtm_churn_rate = (mtm["Churn"] == "Yes").mean()
one_year_churn_rate = churn_by_contract["One year"]
adoption_rate = 0.30  # 20% migrate to 1-year contract

mtm_customers = len(mtm)

avoided_churn = (
    mtm_customers *
    adoption_rate *
    (mtm_churn_rate - one_year_churn_rate)
)

total_customers = len(df)
churn_reduction_rate = avoided_churn / total_customers

# --- Business Impact KPIs ---
df['Churn_binary'] = df['Churn'].map({'Yes': 1, 'No': 0})
# --- Business Impact KPIs ---


# Baseline churn (numeric, correct)
baseline_churn_rate = df['Churn_binary'].mean()

# New churn after strategy
new_churn_rate = baseline_churn_rate - churn_reduction_rate

# Relative churn reduction (main business KPI)
relative_churn_reduction = churn_reduction_rate / baseline_churn_rate

# Customers retained per 1,000 users
customer_saved_per_1000 = churn_reduction_rate * 1000

st.markdown("## 📈 Business Impact ")
st.text("By prioritizing retention efforts on early-tenure and month-to-month customers, the company could achieve an estimated 19.6% relative reduction in churn, even with partial adoption (30%) of targeted actions. This translates into retaining approximately 52 additional customers per 1,000, generating meaningful business impact without major changes to pricing or infrastructure.")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Churn Rate (Before)", f"{baseline_churn_rate:.1%}")
col2.metric("Relative Churn Reduction", f"{relative_churn_reduction:.1%}")
col3.metric("Churn Rate (After)", f"{new_churn_rate:.1%}")
col4.metric("Customers Retained per 1,000 users", f"{customer_saved_per_1000:.0f}")






 
