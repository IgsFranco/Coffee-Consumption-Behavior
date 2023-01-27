import streamlit as st
import pandas as pd
import plost

from views import Pages

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

list_of_pages = [
    "Dashboard",
    "Observations",
    "Insights",
]

st.sidebar.header('Iñigo Jose G. Franco')

st.sidebar.title(':scroll: Coffee Consumption Behavior of Consumers')

selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Dashboard":
    Pages.dashboard()

elif selection == "Observations":
    Pages.observations()

elif selection == "Insights":
    Pages.insights()
