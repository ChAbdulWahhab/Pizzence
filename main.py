import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from vector import load_retriever

st.set_page_config(page_title="Pizzence", page_icon="🍕")
st.title("Pizza Restaurant Assistant 🍕")
st.markdown("Ask anything about the restaurant based on real reviews!")

# Load retriever and model
retriever = load_retriever()

model = Ollama(
    model="llama3.2",  # Your preferred 2GB model
    temperature=0.5
)

# Prompt template
template = """
You are an expert in answering questions about a pizza restaurant.

Based on the following customer reviews, give a short, helpful, and to-the-point answer. Avoid unnecessary details.

Here are the reviews:
{reviews}

User's question:
{question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_query = st.chat_input("Ask your question here...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.spinner("Thinking..."):
        try:
            docs = retriever.invoke(user_query)

            # Convert docs to plain text
            reviews_text = "\n\n".join(doc.page_content for doc in docs)

            if reviews_text.strip():
                st.markdown("📄 **Reviews context:**")
                for doc in docs:
                    st.markdown(f"- {doc.page_content}")
            else:
                st.markdown("📄 **Reviews context:** _No relevant reviews found._")

            # Get model response
            response = chain.invoke({
                "reviews": reviews_text,
                "question": user_query
            })

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
            response = "Sorry, I couldn't process your request."

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
