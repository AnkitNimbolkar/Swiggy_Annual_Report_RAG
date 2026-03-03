from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from config import CHROMA_DIR, EMBEDDING_MODEL_NAME


def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)


def get_vectorstore():
    embeddings = get_embeddings()
    vectordb = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )
    return vectordb


def get_retriever(k: int = 5):
    vectordb = get_vectorstore()
    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    return retriever
