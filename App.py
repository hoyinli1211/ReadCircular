import streamlit as st
import torch  # PyTorch
import tensorflow as tf  # TensorFlow
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

# Specify model name
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"

# Load the model and tokenizer
@st.cache(allow_output_mutation=True)
def load_model_and_tokenizer():
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

# Initialize the model and tokenizer
model, tokenizer = load_model_and_tokenizer()

# App title
st.title('Question Answering System')

# User input
context = st.text_area('Context') 
question = st.text_input('Question')

# Button to get answer
if st.button('Get Answer'):
    inputs = tokenizer(question, context, return_tensors='pt')
    outputs = model(**inputs)
    answer_start = torch.argmax(outputs.start_logits)  # get the most likely beginning of answer with the argmax of the start logits
    answer_end = torch.argmax(outputs.end_logits) + 1  # get the most likely end of answer with the argmax of the end logits
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))
    
    st.write('Answer: ', answer)
