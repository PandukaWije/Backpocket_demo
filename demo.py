import streamlit as st
import openai
import os

def open_ai_script(email):
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "system", "content" : '''You will be provided with unstructured data, and your task is to process the data - segment the sections to following titles
    email_metadata,transaction_date, transaction_time, service_details, bill_details, payment_details, vendor_details,
    these are to be saved in a system that is using a template based architecture to insert data to a nosql database, parse it into JSON format regardless of the inserted data format, if you cant find the details for relevent sections put NULL'''},
                {"role": "user", "content" : email}],
    temperature=0,
    )
    return response['choices'][0]['message']['content']


# Streamlit UI components
st.title("Backpocket Test Environment")

# Input field for raw email
raw_email = st.text_area("Enter Raw Email", height=200)

# Process button
if st.button("Process"):
    # Parse the email
    parsed_data = open_ai_script(raw_email)
    # Display the output
    st.write("Parsed Output:")
    st.json(parsed_data)
