import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from analytics_monthly_ui import analytics_monthly_tab
from analytics_weekly_ui import analytics_weekly_tab


st.title("Expense Tracking System")

tab1, tab2,tab3,tab4 = st.tabs(["Add/Update", "Analytics","Analytics_Monthly","Analytics_weekly"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_monthly_tab()

with tab4:
    analytics_weekly_tab()


