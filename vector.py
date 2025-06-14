import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import OllamaEmbeddings
import pandas as pd
import os

def load_retriever():
    df = pd.read_csv("realistic_restaurant_reviews.csv")
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")

    db_location = "./chrome_langchain_db"
    add_documents = not os.path.exists(db_location)

    vector_store = Chroma(
        collection_name="restaurant_reviews",
        persist_directory=db_location,
        embedding_function=embeddings
    )

    if add_documents:
        documents = []
        ids = []

        for i, row in df.iterrows():
            document = Document(
                page_content=row["Title"] + " " + row["Review"],
                metadata={"rating": row["Rating"], "date": row["Date"]},
                id=str(i)
            )
            ids.append(str(i))
            documents.append(document)

        vector_store.add_documents(documents=documents, ids=ids)

    return vector_store.as_retriever(search_kwargs={"k": 5})

retriever = load_retriever()
