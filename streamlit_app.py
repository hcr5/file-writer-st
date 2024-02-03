# app.py
import streamlit as st
import subprocess

def add_hello_world_to_file():
    with open("transactions.txt", "a") as file:
        file.write("hello world\n")

def commit_and_push_changes():
    try:
        # Add changes to the index
        subprocess.run(["git", "add", "transactions.txt"])
        
        # Commit changes
        subprocess.run(["git", "commit", "-m", "Automatically add 'hello world'"])
        
        # Push changes to the remote repository
        subprocess.run(["git", "push", "origin", "main"])  # Replace "main" with your branch name if different

        st.success("Changes committed and pushed successfully!")

    except Exception as e:
        st.error(f"Error: {e}")

def main():
    st.title("GitHub Streamlit App")

    # Automatically add 'hello world' to transactions.txt
    add_hello_world_to_file()

    # Automatically commit and push changes
    commit_and_push_changes()

    st.success("Line added and changes committed automatically!")

if __name__ == "__main__":
    main()
