from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
import os
import streamlit as st

class DocumentDatabase:
    def __init__(self, pdf_dir):
        self.pdf_dir = pdf_dir
        
    def initialize_database(self):
        if "pdf_texts" not in st.session_state:
            temp_pdf_texts = []
            with st.spinner("Setting up ChatBot"):
                for file in os.listdir(self.pdf_dir):
                    if file.endswith('.pdf'):
                        loader = PyPDFLoader(os.path.join(self.pdf_dir, file))
                        documents = loader.load()
                        text = " ".join([doc.page_content for doc in documents])
                        temp_pdf_texts.append(text)
                        
                st.session_state["pdf_texts"] = temp_pdf_texts
                pdf_list = list(st.session_state["pdf_texts"])
                pdfDatabase = " ".join(pdf_list)
                
                splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
                chunks = splitter.split_text(pdfDatabase)
                embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
                
                if "vectors" not in st.session_state:
                    vectors = FAISS.from_texts(chunks, embeddings)
                    st.session_state["vectors"] = vectors