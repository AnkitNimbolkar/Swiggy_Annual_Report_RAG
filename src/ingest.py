import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from config import PDF_PATH, CHROMA_DIR, CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL_NAME


def load_documents():
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()
    return docs


def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return splitter.split_documents(docs)


def build_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)


def build_chroma_store(chunks, embeddings):
    os.makedirs(CHROMA_DIR, exist_ok=True)
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )
    vectordb.persist()
    return vectordb


def main():
    print("Loading PDF...")
    docs = load_documents()
    print(f"Loaded {len(docs)} pages")

    print("Splitting into chunks...")
    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    print("Loading embedding model...")
    embeddings = build_embeddings()

    print("Building Chroma vector store...")
    vectordb = build_chroma_store(chunks, embeddings)
    print("Chroma store built and persisted at:", CHROMA_DIR)


if __name__ == "__main__":
    main()
