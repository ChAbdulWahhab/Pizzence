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
- **Ollama Embeddings** for review embedding

---

## 📂 Project Structure

```

pizzence/
│
├── main.py                        # Streamlit chatbot app
├── vector.py                      # Review embedding and retriever setup
├── realistic\_restaurant\_reviews.csv  # Customer reviews dataset
├── requirements.txt               # Dependencies
└── README.md                      # You’re here!

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

```bash
pip install -r requirements.txt
```

### 4. Run the chatbot

```bash
streamlit run main.py
```

---

## 📄 Dataset Format

Make sure the file `realistic_restaurant_reviews.csv` exists with the following columns:

* `Title` – Short title of the review
* `Review` – Full review text
* `Rating` – Numeric rating (e.g., 4.5)
* `Date` – Review date

---

## 🧠 How It Works

1. Reviews are embedded using `OllamaEmbeddings`.
2. Stored locally using `ChromaDB`.
3. When a question is asked, Pizzence retrieves relevant reviews.
4. Feeds them into a custom prompt for LLaMA3 to generate a helpful reply.

---

## ✨ Example Questions

* *Do they offer gluten-free pizzas?*
* *How's the customer service?*
* *What are customers saying about the crust?*

---

## 📬 Feedback

Feel free to [open an issue](https://github.com/ChAbdulWahhab/pizzence/issues) or contribute improvements!

---

Enjoy chatting with your reviews – powered by **Pizzence** 🍕
