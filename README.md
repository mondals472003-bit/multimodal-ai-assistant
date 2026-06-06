# AI PDF Assistant

A Retrieval-Augmented Generation (RAG) based AI Assistant that can answer questions from PDF documents.

## Features

- Extracts text from PDF files
- Splits documents into chunks
- Generates embeddings using Sentence Transformers
- Retrieves the most relevant chunk using semantic search
- FastAPI backend
- React + Vite frontend
- Interactive question-answer interface

## Tech Stack

### Backend
- Python
- FastAPI
- PyPDF
- Sentence Transformers
- NumPy

### Frontend
- React
- Vite
- Axios

## Project Structure

AI_ASSISTANT/
├── BACKEND/
│   ├── main.py
│   ├── rag.py
│   ├── uploads/
│   └── venv/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json

## Installation

### Clone Repository

```bash
git clone https://github.com/mondals472003-bit/multimodal-ai-assistant.git
cd multimodal-ai-assistant
```

### Backend Setup

```bash
cd BACKEND

python -m venv venv

venv\Scripts\activate

pip install fastapi uvicorn pypdf sentence-transformers numpy
```

### Run Backend

```bash
python -m uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

## Usage

1. Start backend server.
2. Start frontend server.
3. Open browser.
4. Ask questions about the PDF document.
5. The system retrieves the most relevant content and displays the answer.

## Example Question

```text
What is stochastic nonlinear programming?
```

## Future Improvements

- PDF upload from UI
- Multiple PDF support
- FAISS vector database
- OpenAI/Gemma/Llama integration
- Chat history
- User authentication

## Author

Sayan Mondal

M.Tech, NIT Durgapur
