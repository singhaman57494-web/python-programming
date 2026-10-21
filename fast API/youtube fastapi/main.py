import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv(Path(__file__).with_name(".env"))

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URL") or os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000) if MONGO_URI else None
db = client["Cluster0"] if client is not None else None


@app.get("/")
def read_root():
    if db is None:
        raise HTTPException(
            status_code=503,
            detail="MongoDB is not configured. Set MONGO_URL or MONGO_URI in this project's .env file.",
        )

    try:
        collections = db.list_collection_names()
    except PyMongoError as exc:
        logging.exception("Could not connect to MongoDB")
        if "SSL handshake failed" in str(exc):
            detail = (
                "MongoDB TLS handshake failed before authentication. Check that the Atlas "
                "cluster is active and try without VPN, proxy, or TLS-inspecting firewall."
            )
        else:
            detail = (
                "MongoDB is unavailable. Check the connection string, network access, "
                "and database credentials."
            )
        raise HTTPException(
            status_code=503,
            detail=detail,
        ) from exc

    return {"message": "Successfully connected to MongoDB!", "collections": collections}