# DocIntel AI – Enterprise Document Intelligence Platform

## Overview

DocIntel AI is an AI-powered document intelligence platform built using FastAPI and Google Gemini. The application allows users to upload PDF documents, automatically extracts their contents, generates intelligent summaries, and stores document metadata in a SQLite database.

The project demonstrates REST API development, AI integration, document processing, database management, and modular backend architecture.

---

## Features

- Upload PDF documents
- Automatic PDF text extraction
- AI-powered document summarization using Google Gemini
- SQLite database for persistent storage
- Retrieve all uploaded documents
- Retrieve a specific document by ID
- Swagger API documentation
- Application logging

---

## Tech Stack

- Python
- FastAPI
- Google Gemini 3.5 Flash
- SQLite
- PyPDF
- Uvicorn

---

## Project Structure

```
DocIntelAI/
│
├── database/
│   ├── db.py
│   └── documents.db
│
├── services/
│   └── summarizer.py
│
├── uploads/
├── logs/
│   └── app.log
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API Health Check |
| POST | /documents | Upload and analyse a PDF |
| GET | /documents | Retrieve all uploaded documents |
| GET | /documents/{id} | Retrieve a document by ID |

---

## Future Improvements

- User Authentication
- OCR support for scanned PDFs
- Vector database integration
- Semantic search
- Cloud deployment

---

## Author

Keerthi Anna