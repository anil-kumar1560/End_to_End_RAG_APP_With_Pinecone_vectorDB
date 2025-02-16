import streamlit as st

from langchain.schema import HumanMessage,SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="Conversational Q&A Bot")
st.header("hey lets chat")

from dotenv import load_dotenv
load_dotenv()

chat=ChatOpenAI(temperature=0.9)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="you are a comedian AI assistant")
    ]

def get_chatmodel_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("Input:",key="Input")
response=get_chatmodel_response(input)

submit=st.button("Submit")

if submit:
    st.subheader("the response is:")
    st.write(response)