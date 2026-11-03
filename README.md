# DocIntel AI – Enterprise Document Intelligence Platform

An AI-powered document intelligence application built with **Python, FastAPI, PostgreSQL, SQLite, and Google Gemini**. The application processes PDF documents, extracts text, calculates document statistics, generates AI-powered summaries, and provides REST APIs for document storage and retrieval.

## Overview

DocIntel AI simplifies document processing by combining PDF extraction with AI-powered summarization.

The application allows users to:
- Upload PDF documents through a REST API.
- Extract text from PDF pages.
- Calculate document statistics, including page count and word count.
- Generate concise summaries using Google Gemini.
- Store document information and summaries in a relational database.
- Retrieve all uploaded documents or a specific document using its ID.

## Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| AI Integration | Google Gemini API |
| PDF Processing | PyPDF |
| Databases | PostgreSQL, SQLite |
| PostgreSQL Driver | Psycopg |
| Configuration | python-dotenv |
| API Documentation | Swagger/OpenAPI |
| Logging | Python Logging |

## System Architecture

The application follows a modular backend architecture.

1. **API Layer:** FastAPI handles incoming HTTP requests and exposes document management endpoints.
2. **PDF Processing Layer:** PyPDF extracts text and document information from uploaded PDF files.
3. **AI Summarization Layer:** Google Gemini generates summaries from the extracted text.
4. **Database Layer:** PostgreSQL handles document storage and retrieval through Psycopg. SQLite is also explored for local database setup and initialization.
5. **Logging Layer:** Python logging records application events and document-processing activity.

### Document Processing Workflow

```text
        PDF Upload
             |
             v
       FastAPI Endpoint
             |
             v
        PyPDF Extraction
             |
             v
     Text & Metadata Processing
             |
             v
      Google Gemini API
             |
             v
       AI-Generated Summary
             |
             v
       PostgreSQL Storage
             |
             v
     Document Retrieval APIs
```

## Database Implementation

This project explores two relational database systems:

### PostgreSQL
- Integrated PostgreSQL with FastAPI using the Psycopg driver.
- Configured database connectivity through environment variables.
- Implemented document insertion and retrieval operations.
- Used parameterized SQL queries for database operations.
- PostgreSQL is used by the application's current document API endpoints.

### SQLite
- Explored SQLite for lightweight local database storage.
- Implemented database connection and table initialization.
- Used SQLite to understand local relational database operations and schema creation.

The two implementations provided practical experience with relational databases, SQL queries, database connectivity, and backend integration.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks application status |
| POST | `/documents` | Uploads and processes a PDF document |
| GET | `/documents` | Retrieves all stored documents |
| GET | `/documents/{document_id}` | Retrieves a document using its ID |

### API Documentation

Once the application is running, access the interactive Swagger documentation at:

`http://127.0.0.1:8000/docs`

## Project Structure

```text
DocIntel/
│
├── database/
│   ├── db.py
│   ├── documents.db
│   └── postgres_db.py
│
├── services/
│   └── summarizer.py
│
├── uploads/
├── logs/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/keerthianna07/DocIntel.git
cd DocIntel
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=docintel
DB_USER=your_username
DB_PASSWORD=your_password

GEMINI_API_KEY=your_gemini_api_key
```

Use your own PostgreSQL credentials and Gemini API key. Ensure that the PostgreSQL database and the required `documents` table have been created before running the application.

### 5. Run the Application

```bash
uvicorn main:app --reload
```

The application will be available at:

`http://127.0.0.1:8000`

## Key Learning Outcomes

- Building RESTful APIs using FastAPI.
- Integrating PostgreSQL with Python using Psycopg.
- Exploring SQLite and relational database fundamentals.
- Working with environment variables and database configurations.
- Extracting and processing PDF content using PyPDF.
- Integrating Google Gemini for AI-powered text summarization.
- Implementing modular application architecture and logging.

## Future Enhancements

- Add document search and filtering capabilities.
- Implement user authentication and authorization.
- Support additional document formats.
- Introduce asynchronous document processing.
- Build a web-based interface for document management.

---

**Author:** Anna Venkata Ranga Keerthi

**GitHub:** [keerthianna07](https://github.com/keerthianna07)