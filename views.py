import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.title(':scroll: Coffee Consumption Behavior of Consumers')
st.sidebar.header('Iñigo Jose G. Franco')

def dashboard():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

    title_container = st.beta_container()
    col1, mid, col2 = st.beta_columns([1, 1, 20])
    image = Image.open('https://raw.githubusercontent.com/IgsFranco/Coffee-Consumption-Behavior/main/images/logo.png')
    with title_container:
        with col1:
            st.image(image, width=50)
        with col2:
                st.markdown('<h1 style="color: navy blue;">Coffee Consumption of Consumers</h1>',
                            unsafe_allow_html=True)
        

    #Row 1
    st.markdown('### Summary Statistics')
    col1, col2, col3 = st.columns(3)
    col1.metric("Number of Posts", "1,063")
    col2.metric("Earliest Date", "Jan 2, 2020")
    col3.metric("Latest Date", "Dec 31, 2020")

    #Row 2
    g_coffee_t = pd.read_csv('https://raw.githubusercontent.com/IgsFranco/Coffee-Consumption-Behavior/main/data/coffee-trends-graph.csv')
    i_coffee_t = pd.read_csv('https://raw.githubusercontent.com/IgsFranco/Coffee-Consumption-Behavior/main/data/iced-coffee-trends-graph.csv')

    c1, c2 = st.columns((7,3))
    with c1:
        st.markdown('### Coffee Trends')
        plost.donut_chart(
        data=g_coffee_t,
        theta='Number_of_Posts',
        color='cTheme_label',
        legend='bottom', 
        use_container_width=True)
    with c2:
        st.markdown('### Iced-Coffee Trends')
        plost.bar_chart(
        data=i_coffee_t,
        bar='Trend (Coffee-related)',
        value='Number_of_Posts',
        legend='bottom', 
        use_container_width=True)

def observations():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def insights():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": dashboard,
    "Page 2": observations,
    "Page 3": insights,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
