import os
import streamlit as st
from rag_pipeline import answer_query
from retriever import get_retriever
from components import (
    hero_banner, metric_pills, section_header,
    answer_card, fancy_divider, empty_state
)

# ── Helpers ──
@st.cache_resource
def load_retriever(k):
    return get_retriever(k)

def load_css(path: str):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DEFAULT_K = 5

# ── Config ──
st.set_page_config(
    page_title="Swiggy Annual Report QA",
    page_icon="🍊",
    layout="wide"
)

load_css(os.path.join(os.path.dirname(__file__), "styles.css"))

# ── UI ───
st.markdown(hero_banner(), unsafe_allow_html=True)
st.markdown(metric_pills(), unsafe_allow_html=True)

question = st.text_input(
    "🔎 What would you like to know?",
    placeholder="e.g. What was Swiggy's revenue growth in FY 2024-25?"
)

col1, _ = st.columns([1, 7])
with col1:
    ask_button = st.button("✦ Ask")

# ── Query & Response ──
if ask_button and question.strip():
    with st.spinner("📖 Analysing report…"):
        retriever = load_retriever(DEFAULT_K)
        result = answer_query(question.strip(), retriever=retriever)

    st.markdown(fancy_divider(), unsafe_allow_html=True)
    st.markdown(section_header("📌", "Answer", ""), unsafe_allow_html=True)
    st.markdown(answer_card(result["answer"]), unsafe_allow_html=True)

    st.markdown(fancy_divider(), unsafe_allow_html=True)
    st.markdown(section_header("📄", "Supporting Context", "From Report"), unsafe_allow_html=True)

    for i, doc in enumerate(result["contexts"], start=1):
        page = doc.metadata.get("page", "N/A")
        with st.expander(f"📑  Chunk {i}  ·  Page {page}"):
            st.write(doc.page_content)

else:
    st.markdown(empty_state(), unsafe_allow_html=True)
