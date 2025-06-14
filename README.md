# 🍕 Pizzence – Your Pizza Restaurant Review Assistant

**Pizzence** is an AI-powered chatbot built with **Streamlit** and **LangChain**, designed to answer customer questions based on real restaurant reviews. Whether it's gluten-free options, service quality, or favorite dishes—Pizzence delivers quick, relevant answers powered by **LLaMA3** via **Ollama**.

---

## 🚀 Features

- 💬 Chat with real customer reviews  
- ⚡ Fast, relevant, and to-the-point responses  
- 🧠 Uses local vector search (ChromaDB) for context  
- 🌐 Simple Streamlit web UI  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** for frontend
- **LangChain** for prompt orchestration
- **Ollama (LLaMA3.2)** as the LLM
- **ChromaDB** for vector database
- **OllamaEmbeddings** for review embedding

---

## 📂 Project Structure

```

pizzence/
│
├── chrome\_langchain\_db/              # ChromaDB vector store (auto-created)
├── .gitignore                        # Git ignore rules
├── .python-version                   # Python version file (optional)
├── main.py                           # Streamlit chatbot app
├── vector.py                         # Review embedding and retriever setup
├── realistic\_restaurant\_reviews.csv  # Customer reviews dataset
├── pyproject.toml                    # Project dependencies and config
├── uv.lock                           # Package lock file (if using uv/rye)
└── README.md                         # You’re here!

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/ChAbdulWahhab/pizzence.git
cd pizzence
````

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

If you're using `uv`:

```bash
uv pip install -r requirements.txt
```

Otherwise:

```bash
pip install -r requirements.txt
```

### 4. Start the chatbot

```bash
streamlit run main.py
```

---

## 🧠 How It Works

1. Loads and embeds the reviews using **OllamaEmbeddings**.
2. Saves them to a local **ChromaDB** vector store.
3. When a user asks a question, relevant reviews are retrieved.
4. These are used as context for the **LLaMA3** model to generate an answer.

---

## ✨ Example Questions

* *Do they offer gluten-free pizzas?*
* *How is the staff behavior according to reviews?*
* *What’s the most appreciated item on the menu?*

---

## 📬 Feedback

Open an issue or contribute on [GitHub](https://github.com/ChAbdulWahhab/pizzence).

Enjoy chatting with your reviews – powered by **Pizzence** 🍕
