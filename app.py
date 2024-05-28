import re
from pymongo import MongoClient
import pymongo
import streamlit as st


# MongoDB connection
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client['barry']
collection = db['credentials']

# Regular expressions for username and password validation
username_pattern = "^[a-z]+[a-zA-z0-9]+[@]{1}[a-z]+[.]{1}[a-z]{3}$"
pass_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%&*?])[A-Za-z0-9@#$%&*?]{5,16}$"

def isValidEmail(username):
    return bool(re.fullmatch(username_pattern, username))

def isValidPassword(password):
    return bool(re.fullmatch(pass_pattern, password))

def register():
    username = st.text_input("Enter your email: ")
    if isValidEmail(username):
        password = st.text_input("Enter your password: ")
        if isValidPassword(password):
            # Check if user already exists
            if collection.find_one({"username": username}):
                st.text("Username already exists. Please try again.")
                register()
            else:
                # Insert new user into MongoDB
                collection.insert_one({"username": username, "password": password})
                st.text("Registration successful!")

        else:
            st.text("Invalid password. Please try again.")
            register()
    else:
        st.text("Invalid username. Please try again.")
        register()

def login():
    username = st.text_input("Enter your email: ")
    password = st.text_input("Enter your password: ")
    user = collection.find_one({"username": username})
    if user and user["password"] == password:
        st.text("Login successful!")
    else:
        st.text("Invalid username or password. Please try again.")
        login()

def forgot_password():
    username = st.text_input("Enter your email: ")
    user = collection.find_one({"username": username})
    if user:
        new_password = st.text_input("Enter new password: ")
        if isValidPassword(new_password):
            collection.update_one({"username": username}, {"$set": {"password": new_password}})
            st.text("Password reset successful!")
        else:
            st.text("Invalid password. Please try again.")
            forgot_password()
    else:
        st.text("Username does not exist.")
        login()


option = ['Register', 'Login', 'Reset Password']
option = st.selectbox('Select an option', option)
if option == 'Register':
    register()
elif option == 'Login':
    login()
elif option == 'Password':
    forgot_password()
else:
    st.text("Invalid option. Please try again.")

