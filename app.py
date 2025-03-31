"""
Main Streamlit application file.
"""
import streamlit as st
from src.utils import example_function

def main():
    st.title("Midterm Project")
    st.write("Welcome to the Streamlit Midterm Project!")
    
    # Example of using the custom module
    message = example_function()
    st.write(message)

if __name__ == "__main__":
    main()
