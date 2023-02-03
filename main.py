#!/usr/bin/python -tt
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
from datetime import date
from database import create_table, add_data, view_data, resetCount, countOne, emptyDB


# last = df['Date'].iloc[-1]

# with st.echo():
#     st.write('This code will be printed')

result = view_data()
df = pd.DataFrame(result, columns=['Caption', 'Date', 'Rating'])
emptyDB(df)

selected = option_menu(
    menu_title=None,
    options=["Home", "Activity", "Progress"],
    icons=["house-fill", "clock-history", "graph-up-arrow"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "white", "font-size": "20px"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#F54683"},
    }
)

create_table()
if selected == "Home":
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    st.title("Quote Your Day")
    caption = st.text_area(d2, placeholder="Write something")
    col1, col2 = st.columns(2)
    with col1:

        rating = st.select_slider(
            ":red[**Emotion**] **Scale**", options=["😭", "😕", "🙂", "😁", "🤩"], value="🙂")
        if (rating == "😭"):
            rate = 1
            st.caption("Hmm..sounds :red[**rough!**]")
        elif(rating == "😕"):
            rate = 2
            st.caption("It'll be :blue[**alright!**]")
        elif(rating == "🙂"):
            rate = 3
            st.caption("glad you're :violet[**happy**]")
        elif(rating == "😁"):
            rate = 4
            st.caption(":red[**wooooo**] good for you!")
        elif(rating == "🤩"):
            rate = 5
            st.caption(":red[**DAMNNNNN**], SONNN!!")

        if st.button("Post"):
            def check_date():
                print("running")
                result = view_data()
                df = pd.DataFrame(
                    result, columns=['Caption', 'Date', 'Rating'])
                last = df['Date'].iloc[-1]

                today = date.today()
                d2 = d2 = today.strftime("%B %d, %Y")
                if (d2 == last):
                    countOne()
                    st.error(
                        "You already posted today! Come back again tomorrow.👋")
                else:
                    add_data(caption, d2, rate)
                    st.balloons()
            check_date()


if selected == "Activity":
    st.title("Your Activity")
    result = view_data()
    df = pd.DataFrame(result, columns=['Caption', 'Date', 'Rating'])
    with st.expander("Your Data"):
        st.dataframe(df)

if selected == "Progress":
    st.title("View a visual one")
    result = view_data()
    df = pd.DataFrame(result, columns=['Caption', 'Date', 'Rating'])
    chart_data = (df['Date'], df['Rating'])
    st.line_chart(df, x='Date', y='Rating')
