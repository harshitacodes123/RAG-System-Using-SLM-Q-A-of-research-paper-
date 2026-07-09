# 📄 Research Paper Question Answering System using RAG and Small Language Models (SLMs)

## Overview

This project is a **Research Paper Question Answering System** that enables users to ask natural language questions about research papers and receive context-aware answers. It leverages **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded research papers and generates accurate responses using a Small Language Model (SLM).

The application is built with **Streamlit** for an interactive user interface and is designed to efficiently answer questions while minimizing hallucinations by grounding responses in the retrieved document context.

---

## Features

* 📚 Upload and process research papers in PDF format
* 🔍 Semantic search using vector embeddings
* 🤖 Question answering powered by a Small Language Model (SLM)
* 📄 Retrieval-Augmented Generation (RAG) pipeline
* ⚡ Interactive Streamlit web application
* 💾 Vector database for efficient document retrieval

---

## Tech Stack

* **Frontend:** Streamlit
* **Programming Language:** Python
* **Framework:** LangChain
* **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`
* **Language Model:** Google Gemma 2B (or another compatible Small Language Model)
* **Vector Database:** FAISS / ChromaDB
* **PDF Processing:** PyPDF
* **Machine Learning:** Hugging Face Transformers

---

## Project Workflow

1. Upload research paper(s) in PDF format.
2. Extract text from the documents.
3. Split the text into manageable chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in a vector database.
6. Retrieve the most relevant chunks based on the user's query.
7. Pass the retrieved context to the language model.
8. Generate and display an accurate answer.

---

## 📁 Project Structure

```text
Research-Paper-RAG/
│
├── app.py                              # Streamlit web application
├── rag.py                              # RAG pipeline and question-answering logic
├── research_paper_rag_using_slm_final.py   # Original Google Colab implementation
├── research_db.zip                     # Compressed vector database (FAISS/Chroma)
├── README.md                           # Project documentation
│
├── data/                               # (Optional) Research paper PDFs
│   ├── paper1.pdf
│   ├── paper2.pdf
│   └── ...
│
└── requirements.txt                    # Python dependencies
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/research-paper-rag.git
cd research-paper-rag
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Improvements

* Support multiple research papers simultaneously
* Add citation-aware responses
* Improve retrieval with hybrid search
* Chat history and conversation memory
* Deploy using RunPod for persistent hosting
* Docker containerization
* User authentication

---

## Applications

* Academic research
* Literature review
* Research assistants
* Student learning
* Knowledge management

---

## Author

**Harshita Mittal**

B.Tech (Artificial Intelligence & Machine Learning)

Passionate about Artificial Intelligence, Machine Learning, and Retrieval-Augmented Generation (RAG) systems.

---

## License

This project is developed for educational and learning purposes.
