import streamlit as st

from views import Pages



list_of_pages = [
    "Dashboard",
    "Observations",
    "Insights",
]

st.sidebar.title(':scroll: Coffee Consumption Behavior of Consumers')

selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Dashboard":
    Pages.dashboard()

elif selection == "Observations":
    Pages.observations()

elif selection == "Insights":
    Pages.insights()