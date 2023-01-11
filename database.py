#!/usr/bin/python -tt
import sqlite3
import streamlit as st
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()
import pandas as pd
from datetime import date


def emptyDB(df):
    if df.empty:
        st.success(
            "Hey Stranger!, Let's get started by writing your first quote.", icon="🔥")
        st.info(
            "**Note:** You can only quote once everyday.", icon="👀")
        c.execute('INSERT INTO user(caption, date, rating) VALUES(?, ?, ?)',
                  ("Yogur First Day!", "1st day", "5"))
        conn.commit()


count = 0


def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS user (caption TEXT, date DATE, rating INT)')


def add_data(quote, date, rating):
    global count
    print("The current count value is:", count)
    if (quote != "" and count == 0):
        c.execute('INSERT INTO user(caption, date, rating) VALUES(?, ?, ?)',
                  (quote, date, rating))
        conn.commit()
        st.success("Sucessful!")
        count = count + 1
        print("I added the quote. Now the count value is: ", count)
    elif (quote == "" and count == 0):
        st.error("Your text is empty!")
        print("The text field is empty, the count value is:", count)
    elif (quote != "" and count != 0):
        st.error("Limit Exceeded!")
        print("Limit exceeded for today, the count value is", count)
    elif (quote == "" and count != 0):
        st.error("You already exceeded your limit for today!")
        print("Limit exceeded for today, the count value is", count)


def view_data():
    c.execute('SELECT * FROM user')
    data = c.fetchall()
    return data


def countOne():
    count = 1
    print("count value is: ", count)


def resetCount():
    count = 0
    print("count value reseted! count value is: ", count)
