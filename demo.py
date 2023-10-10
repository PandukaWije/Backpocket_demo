import streamlit as st
import openai
from dotenv import load_dotenv


def open_ai_scrip(email):
    load_dotenv()
    openai.api_key = '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'
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "system", "content" : '''You will be provided with unstructured data, and your task is to process the data - segment the sections to following titles
    email_metadata, service_details, bill_details, payment_details, service_provider_details,
    these are to be saved in a system that is using a template based architecture to insert data to a nosql database, parse it into JSON format regardless of the inserted data format'''},
                {"role": "user", "content" : email}],
    temperature=0,
    )
    return response['choices'][0]['message']['content']


# Streamlit UI components
st.title("Email Parser")

# Input field for raw email
raw_email = st.text_area("Enter Raw Email", height=200)

# Process button
if st.button("Process"):
    # Parse the email
    parsed_data = open_ai_scrip(raw_email)
    # Display the output
    st.write("Parsed Output:")
    st.json(parsed_data)
