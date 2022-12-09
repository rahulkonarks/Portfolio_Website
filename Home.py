import streamlit as st
import pandas

df = pandas.read_csv("data.csv", sep=";")
col1, col2 = st.columns(2)

with col1:
    st.image("/home/konarkguatam/Desktop/Portfolio_Website/images/Coding.jpg")

with col2:
    st.title("Konark Gautam")
    content = """
    Programming and tech enthusiast! I started learning how to program in python in 2018 and ever since then my love
    and passion for computers kept growing! My father introduced me to programming and kept giving me the best advice
    to succeed in the field! I love building applications using python and applying my skills in various fields.
    I'm really excited to master python by building projects as I think it is a very engaging way to learn the language.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.text(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")
