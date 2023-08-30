import streamlit as st
import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# NLP pipeline
nlp = spacy.load("en_core_web_sm")

# App setup
st.title("Question Answering from Documents")

# Upload and process documents
documents = []
uploaded_files = st.file_uploader("Upload Documents", accept_multiple_files=True)
if uploaded_files:
  for file in uploaded_files:
    doc = nlp(file.read().decode()) 
    documents.append(doc)

# Build TF-IDF model  
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform([doc.text for doc in documents])

# Get user question
question = st.text_input("Enter your question:")

if question:

  # Vectorize question
  q_vec = vectorizer.transform([question])

  # Calculate similarities
  similarities = np.matmul(q_vec, tfidf.T)

  # Get most similar document
  most_similar_doc = np.argmax(similarities)  

  # Display answer  
  st.write(f"Most similar document: {documents[most_similar_doc]}")
