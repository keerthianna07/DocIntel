from fastapi import FastAPI, UploadFile, File
from services.summarizer import generate_summary
from pypdf import PdfReader
from fastapi import HTTPException

import logging
import sqlite3

import shutil
app = FastAPI()

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

@app.get(
    "/documents",
    summary="Retrieve all uploaded documents",
    tags=["Documents"]
)
def get_documents():
    connection = sqlite3.connect("database/documents.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM documents")

    rows = cursor.fetchall()

    connection.close()

    documents = []

    for row in rows:
        documents.append({
            "id": row[0],
            "filename": row[1],
            "pages": row[2],
            "words": row[3],
            "summary": row[4]
        })

    logger.info("Retrieved all documents")

    return {
        "documents": documents
    }


@app.get(
    "/documents/{document_id}",
    summary="Retrieve a document by ID",
    tags=["Documents"]
)
def get_document(document_id: int):

    connection = sqlite3.connect("database/documents.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM documents WHERE id = ?",
        (document_id,)
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    logger.info(f"Retrieved document ID: {document_id}")

    return {
        "id": row[0],
        "filename": row[1],
        "pages": row[2],
        "words": row[3],
        "summary": row[4]
    }

@app.get(
    "/",
    summary="Health check",
    tags=["System"]
)
def root():
    return {"message": "DocIntel AI is running!"}


@app.post(
    "/documents",
    summary="Upload and analyse a PDF document",
    tags=["Documents"]
)
def upload(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        logger.warning(
            f"Rejected upload: {file.filename} is not a PDF"
        )

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    reader = PdfReader(file_path)

    pages = len(reader.pages)

    text = ""

    for page in reader.pages:
        extracted=page.extract_text()

        if extracted:
            text += extracted

    words = len(text.split())

    summary = generate_summary(text)

    logger.info(f"Processed document: {file.filename}")

    connection = sqlite3.connect("database/documents.db")

    cursor = connection.cursor()

    cursor.execute("""
                   INSERT INTO documents(filename, pages, words, summary)
                   VALUES (?, ?, ?, ?)
                   """, (
                       file.filename,
                       pages,
                       words,
                       summary
                   ))

    connection.commit()
    connection.close()

    return {
        "filename": file.filename,
        "pages": pages,
        "words": words,
        "summary": summary
    }

