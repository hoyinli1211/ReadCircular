# Importing libraries
import streamlit as st
import spacy
from spacy import displacy
from collections import defaultdict

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

def process_text(file_content):
    # Process whole documents
    text = file_content.decode("utf-8")
    doc = nlp(text)

    # Analyze syntax
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]

    # Find named entities, phrases and concepts
    entities = [(entity.text, entity.label_) for entity in doc.ents]

    return noun_phrases, verbs, entities

def answer_question(question, noun_phrases, verbs, entities):
    # Here, we're just returning the first noun phrase, verb, or entity that appears in the question.
    # This is a very naive approach to question answering.
    doc = nlp(question)
    for token in doc:
        if token.text in noun_phrases:
            return token.text
        elif token.text in verbs:
            return token.text
        for entity, _ in entities:
            if token.text in entity:
                return entity
    return "I don't know."

# Streamlit app
st.title('Document Analyzer and Question Ansower App')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    file_content = uploaded_file.read()
    noun_phrases, verbs, entities = process_text(file_content)
    st.write('Noun phrases:', noun_phrases)
    st.write('Verbs:', verbs)
    st.write('Named entities:', entities)

    question = st.text_input('Ask a question about the document')
    if question:
        answer = answer_question(question, noun_phrases, verbs, entities)
        st.write('Answer:', answer)
