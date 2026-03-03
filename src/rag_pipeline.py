from typing import List
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

from config import (
    GROQ_API_KEY,
    GROQ_MODEL,
    LLM_TEMPERATURE,
    LLM_MAX_NEW_TOKENS,
)

from retriever import get_retriever


# -----
# LLM
# -----

def get_llm():
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not set")

    return ChatGroq(
        model=GROQ_MODEL,
        temperature=LLM_TEMPERATURE,
        max_tokens=LLM_MAX_NEW_TOKENS,
        groq_api_key=GROQ_API_KEY,
    )


# -------------------------
# Prompt
# -------------------------

PROMPT_TEMPLATE = """
You are an AI assistant answering questions strictly from the Swiggy Limited Annual Report FY 2024-25.

Use ONLY the provided context from the report.
If the answer is not contained in the context, say:
"I do not know based on the annual report."

Context:
{context}

Question:
{question}

Answer in a concise and factual way.
"""


def build_prompt():
    return ChatPromptTemplate.from_template(PROMPT_TEMPLATE)


# -------------------------
# Helper to format docs
# -------------------------

def format_docs(docs: List[Document]) -> str:
    parts = []
    for i, d in enumerate(docs):
        page = d.metadata.get("page", "NA")
        parts.append(f"[CHUNK {i+1}, page {page}]\n{d.page_content}")
    return "\n\n---\n\n".join(parts)


# -------------------------
# Main RAG function
# -------------------------

def answer_query(question: str, retriever):
    docs = retriever.invoke(question)

    context_str = format_docs(docs)

    prompt = build_prompt()
    llm = get_llm()

    chain = prompt | llm

    response = chain.invoke({
        "context": context_str,
        "question": question
    })

    return {
        "answer": response.content,
        "contexts": docs
    }