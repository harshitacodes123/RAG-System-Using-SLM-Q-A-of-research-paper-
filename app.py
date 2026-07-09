
import streamlit as st
from rag import ask_rag      # Import the function from rag.py

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Research Paper QA System",
    page_icon="📚",
    layout="wide"
)

# ---------------- Title ----------------
st.title("📚 Research Paper Question Answering System")
st.write("Ask questions about the uploaded research papers using RAG + Gemma 2B.")

# ---------------- User Input ----------------
question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is Retrieval-Augmented Generation?"
)

# ---------------- Generate Button ----------------
if st.button("Generate Answer"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):

            try:
                answer = ask_rag(question)

                st.subheader("Answer")
                st.success(answer)

            except Exception as e:
                st.error(f"Error: {e}")
