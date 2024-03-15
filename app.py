from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to Load Google Gemini Model and provide queries as a response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the Table named as STUDENTS and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also, the SQL code should not have ``` in the beginning or end and "sql" word in the output.
    """
]

# Streamlit App
st.sidebar.header("Gemini App Configuration")
api_key = st.sidebar.text_input("Enter your Gemini API Key Here")

if api_key:
    genai.configure(api_key=api_key)

st.text("I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(response)

    # Check if the response contains "SELECT" and "FROM" keywords to identify an SQL query
    if "SELECT" in response.upper() and "FROM" in response.upper():
        data = read_sql_query(response, "students.db")
        st.subheader("SQL Query Result:")
        for row in data:
            st.write(row)
    else:
        st.warning("The generated query does not seem to be a valid SQL query.")
