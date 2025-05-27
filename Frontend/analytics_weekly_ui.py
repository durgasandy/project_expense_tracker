import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000"

def analytics_weekly_tab():
    st.title("Weekly Expense Analytics")
    col1, col2 = st.columns(2)
    with col1:
    # Select Year and Month using dropdowns
        years = list(range(2020, 2031))  # you can adjust year range
        year = st.selectbox("Select Year", years, index=years.index(2024))

    months = [
        ("January", "01"), ("February", "02"), ("March", "03"),
        ("April", "04"), ("May", "05"), ("June", "06"),
        ("July", "07"), ("August", "08"), ("September", "09"),
        ("October", "10"), ("November", "11"), ("December", "12")
    ]
    with col2:
        month_name, month_num = st.selectbox("Select Month", months, index=7)  # default August (index 7)

    # Format expense_date as YYYY-MM
    expense_date = f"{year}-{month_num}"

    if st.button("Get Weekly Analytics"):
        response = requests.get(f"{API_URL}/analytics_weekly/{expense_date}")

        if response.status_code == 200:
            weekly_expenses = response.json()
        else:
            st.error("Failed to retrieve expenses")
            return

        if not weekly_expenses:
            st.warning("No expenses found for selected month.")
            return

        df = pd.DataFrame(weekly_expenses)
        df_sorted = df.sort_values(by="week_of_month")

        st.subheader(f"Weekly Expenses for {month_name} {year}")
        st.bar_chart(df_sorted.set_index("week_of_month")["total_expense"])

        st.subheader("Weekly Expenses Table")
        st.table(df_sorted)
