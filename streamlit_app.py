# app.py
import streamlit as st

def add_hello_world_to_file():
    with open("transactions.txt", "a") as file:
        file.write("hello world\n")

def main():
    st.title("GitHub Streamlit App")
    
    if st.button("Add 'hello world' to transactions.txt"):
        add_hello_world_to_file()
        st.success("Line added successfully!")

if __name__ == "__main__":
    main()
