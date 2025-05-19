from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1. Load
loader = Docx2txtLoader("docs/knowledge.docx")
documents = loader.load()  # reads .docx into text :contentReference[oaicite:5]{index=5}

# 2. Chunk
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)  # splits into ~500-char pieces :contentReference[oaicite:6]{index=6}

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # MiniLM model :contentReference[oaicite:7]{index=7}

# Vector store
vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="db")
vectordb.persist()  # saves DB to disk :contentReference[oaicite:8]{index=8}
