import streamlit as st
import pandas as pd
import requests


API_URL = "http://localhost:8000"

def analytics_monthly_tab():
    if st.button("Get monthly Analytics"):
        response = requests.get(f"{API_URL}/analytics_monthly")

        if response.status_code == 200:
            monthly_expenses = response.json()
            #st.write(monthly_expenses)
        else:
            st.error("Failed to retrieve expenses")
            monthly_expenses = []

        df = pd.DataFrame(monthly_expenses)
        df_sorted = df.sort_values(by="month", ascending=True)
        st.subheader("Monthly Expenses Chart")
        st.bar_chart(df_sorted.set_index("month"))
        st.subheader("Monthly Expenses Table")
        st.table(df_sorted)

