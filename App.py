import streamlit as st
from transformers import pipeline

@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad')

def answer_question(context, question):
    nlp_model = load_model()
    ans = nlp_model({
        'context': context,
        'question': question
    })
    return ans['answer']

st.title('Question Answering System')
context = st.text_area('Context')
question = st.text_input('Question')

if st.button('Get an Answer'):
    answer = answer_question(context, question)
    st.write(answer)
