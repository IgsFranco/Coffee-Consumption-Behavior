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

selection = st.sidebar.radio("Go to: ", list_of_pages)
list_of_pages = [
    "Dashboard"
    "Observations",
    "Insights",
]

if selection == "Dashboard":
    Pages.dashboard()

elif selection == "Observations":
    Pages.observations()

elif selection == "Insights":
    Pages.insights()

class Pages:
    # Page 1 - Introduction
    def dashboard():
    # Write the title and the subheader
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


    
#     # Page 2 - [DEMOGRAPHICS?]
#     def demog():
#         # Write the title
#         st.title(
#             "Insert Title - Demographics"
#         )
#         # Load photo -> Update photo relevant to our topic
#         st.image("image1.jpg")

#         # Show Gender
#         # Show Employment

#         # Show Educational Attainment
#         st.markdown("In terms of educational attainment:")
#         Demographics.show_educ()

#     # Page 3 - Show Factors Why Filipinos are Unbanked
#     def show_factors():
#         # Write the title
#         st.title(
#             "Factors why Filipinos are Unbanked"
#         )

#         # Get the reasons why Filipinos are Unbanked
#         r_ph_data = ph_data[
#             [
#                 'r_too_far',
#                 'r_too_expensive',
#                 'r_lack_documentation',
#                 'r_trust',
#                 'r_religious_reasons',
#                 'r_lack_of_money',
#                 'r_family_already_have',
#                 'r_no_need_for_fs'
#             ]
#         ]
        
#         r_labels = [
#             'Too Far',
#             'Too Expensive',
#             'Lack of Documentation',
#             'Lack of Trust',
#             'Religious Regions',
#             'Lack of Money',
#             'Family Member Already Has Account',
#             'No Need For Financial Services'
#         ]

#         # Get total for each reason
#         sum_per_reason = r_ph_data.sum()
#         sum_no_accounts = ph_data['no_accounts'].sum()
#         percentage_reasons = (sum_per_reason*100)/sum_no_accounts

#         # Assign label to percent value
#         df = pd.DataFrame({"percentage_reasons":percentage_reasons, "r_labels":r_labels})
#         df = df.sort_values('percentage_reasons', ascending=False).reset_index()

#         # Plot the data
#         fig, ax = plt.subplots(figsize=(9,5), dpi=350)
#         plot = sns.barplot(
#             x = df['percentage_reasons'],
#             y = df['r_labels'],
#             color='#C0C0C0'
#         )
#         plt.title("Top 5 Reasons Why Filipinos aged 21 and above are Unbanked")
#         ax.set_xlabel("% of Population")
#         ax.set_ylabel("Reasons")
#         plt.bar_label(plot.containers[0], fmt='%.2f')
#         plt.xlim(0, 80)

#         # Plot the special bar separately
#         plot.barh([0], [71.63], color='#378078')
#         plot.barh([1], [56.40], color='#378078')
#         plot.barh([2], [46.41], color='#378078')
#         plot.barh([3], [43.78], color='#378078')
#         plot.barh([4], [39.93], color='#378078')

#         # Show the data
#         st.pyplot(fig)


#     def recommendations():
#         # Write the title
#         st.title(
#             "What We Can Do"
#         )
    
#     def the_team():
#         # Write the title
#         st.title(
#             "The Team"
#         )

# # Demographics Class
# class Demographics:
#         def show_educ():
#             ### EDUCATIONAL ATTAINMENT ###
#             # Clean the data
#             ph_no_account = ph_data[ph_data['no_accounts'] != 0]
#             ph_no_account = ph_no_account.groupby('educ')['no_accounts'].count().reset_index()

#             educ_mapping = {
#                 1: 'Primary or Less',
#                 2: 'Secondary',
#                 3: 'Tertiary'
#             }

#             ph_no_account = ph_no_account.replace({'educ': educ_mapping})

#             # Plot the data
#             fig, ax = plt.subplots(figsize=(8.5,4), dpi=200)
            
#             plot = sns.barplot(
#                 x = ph_no_account['educ'],
#                 y = ph_no_account['no_accounts'],
#                 color='#C0C0C0'
#             )
#             plot.bar([1], [322], color='#378078')

#             plt.title('Educational Attainment of Unbanked Filipinos aged 21 and above')
#             ax.set_xlabel('Educational Attainment')
#             ax.set_ylabel('No. of Filipinos with no Accounts')
#             plt.bar_label(plot.containers[0], fmt='%.2f')
#             #plt.xticks(rotation=45)
#             plt.ylim(0, 400)

#             # Show the data
#             st.pyplot(fig)
        
#         def show_gender():
#             # Insert Code Here
#             return ('Page under construction.')
        
#         def show_emp():
#             # Insert code here
#             return ('Page under construction.')