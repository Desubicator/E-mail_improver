import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
Below is an e-mail that may be poorly worded.
Your goal is to:
- Properly format the e-mail
- Convert the input text to a specified tone
- Convert the input text to a specified dialect

Here are some examples of different Tones:
- Formal: We went to Barcelona for the weekend. We have a lot of things to tell you about the trip.
- Informal: Went to Barcelona for the weekend, lots to tell you about.

Here are some examples of different Dialects:
- American English: French fries, cotton candy, apartment, garbage, cookie.
- British English: chips, candyfloss, flat, rubbish, biscuit.

Below is the e-mail, tone and dialect:
TONE = {tone}
DIALECT = {dialect}
EMAIL = {email}

YOUR RESPONSE:

"""

prompt = PromptTemplate(
    input_variables={"tone", "dialect", "email"},
    template=template,
)

def load_LLM():
    llm = OpenAI(temperature=.5)
    return llm

llm = load_LLM()

st.set_page_config(page_title="E-mail Improver", page_icon=":envelope:")

st.header("E-mail Improver")

col1, col2 = st.columns(2)

with col1:
    st.markdown("This app uses AI language models to improve your e-mail contents. It is powered by OpenAI and Langchain to interpret the text and return improvements to the original.")
    st.markdown("This app is made using Streamlit.")

with col2:
    st.image(image="Images\open-ai-seeklogo.com.svg")

st.markdown("### Enter the e-mail you wish to improve.")

col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        "Select the tone of your e-mail.", ("Formal", "Informal")
    )
with col2:
    option_dialect = st.selectbox(
        "Select the English Dialect you wish to use.", ("American English", "British English")
    )

def get_text():
    input_text = st.text_area(label="", placeholder="Enter the e-mail you wish to improve here...", key="email_input_text")
    return input_text

email_input = get_text()

st.markdown("### Here is your improved e-mail.")

if email_input:
    st.write(email_input)

