# Customer Churn Analysis & Business Impact Dashboard

This project presents an end-to-end customer churn analysis using a telecommunications dataset.  
The objective is to identify key drivers of churn, extract business insights, and present results through both exploratory analysis and an interactive dashboard designed to support decision-making.

The project follows a realistic data analytics workflow, from data exploration to business interpretation and visualization.

---

## Business Problem

Customer churn represents a major financial risk for subscription-based companies.  
Understanding which customers are more likely to leave — and why — allows businesses to design targeted retention strategies and reduce revenue loss.

This analysis focuses on:
- Identifying customer segments with higher churn rates
- Understanding behavioral and contract-related churn drivers
- Translating insights into actionable business recommendations

---
## Dataset

- **Source:** Telco Customer Churn Dataset  
- **Records:** ~7,000 customers  
- **Type:** Structured, tabular data  


---

## Exploratory Data Analysis (EDA)

The exploratory analysis was conducted using Python and focuses on:
- Churn distribution across customer segments
- Relationships between churn and contract types
- Impact of tenure, monthly charges, and payment methods
- Identification of high-risk churn profiles

The notebook includes:
- Data cleaning and preprocessing
- Visual analysis using plots and summary statistics
- Business-oriented interpretation of results

Notebook available here:  
`customer-churn-exploratory-data-analysis.ipynb`

---

## Key Insights

- Customers on **month-to-month contracts** have significantly higher churn rates
- **Short-tenure customers** are more likely to churn
- **Electronic check payment method** is associated with higher churn
- Higher **monthly charges**, when combined with low tenure, increase churn probability

These insights suggest that churn is strongly influenced by **contract stability and early customer experience**.

---

## Dashboard & Application

An interactive dashboard was developed using **Streamlit** to allow stakeholders to:
- Explore churn metrics dynamically
- Visualize churn by customer segment
- Support data-driven retention strategies

The dashboard is structured as a **multi-page application** using Streamlit’s `pages/` architecture.

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Jupyter Notebook
- Streamlit
- Git & GitHub
  
## Business Recommendations
- Incentivize long-term contracts to reduce churn
- Focus retention efforts on customers within their first months
- Improve onboarding experience to increase early engagement

