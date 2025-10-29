import streamlit as st
st.title("test")
st.write("HELLO")
name=st.text_input("name?")
if st.button("CLICK"):
    st.sucess(f"안녕하세요[name]님!")

