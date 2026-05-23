import streamlit as st

from chatbot import get_response


st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖"
)

st.title(
    "🤖 FAQ Chatbot"
)

st.write(
    "Ask a question from stored FAQs"
)

question = st.text_input(
    "Enter your question"
)

if st.button(
    "Ask"
):

    if question:

        answer = get_response(
            question
        )

        st.success(
            answer
        )