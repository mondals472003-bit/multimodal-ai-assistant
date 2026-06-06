from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np


# ==========================
# LOAD PDF
# ==========================

pdf_path = "uploads/NOTES.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text

print("Total Characters:", len(text))


# ==========================
# CHUNKING
# ==========================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)

print("Number of Chunks:", len(chunks))


# ==========================
# EMBEDDINGS
# ==========================

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

embeddings = model.encode(chunks)

print("Embedding Shape:", embeddings.shape)


# ==========================
# QUESTION ANSWERING
# ==========================

def ask_question(question):

    question_embedding = model.encode([question])

    similarities = np.dot(
        embeddings,
        question_embedding.T
    ).flatten()

    best_idx = np.argmax(similarities)

    return chunks[best_idx]


# ==========================
# TEST
# ==========================

question = "What is stochastic nonlinear programming?"

answer = ask_question(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)