import pandas as pd
import pyodbc
from datetime import datetime

DB_CONFIG = {
    "driver": "{SQL Server}",
    "server": "localhost",
    "database": "practicaITla",
    "trusted_connection": "yes"
}

DATA_PATH = "data/"


def transform_data(data):


    clients = data["clients"]
    clients.drop_duplicates(inplace=True)
    clients.dropna(subset=["nombre", "email"], inplace=True)
    clients["email"] = clients["email"].str.lower().str.strip()

    products = data["products"]
    products.drop_duplicates(inplace=True)
    products.dropna(subset=["name", "categoria"], inplace=True)
    products["categoria"] = products["categoria"].str.upper().str.strip()


    social = data["social_comments"]
    social.dropna(subset=["client_id", "product_id", "comment_text"], inplace=True)
    social = social[social["rating"].between(1, 5)]

    reviews = data["web_reviews"]
    reviews.dropna(subset=["client_id", "product_id", "comentario"], inplace=True)
    reviews["fecha"] = pd.to_datetime(reviews["fecha"], errors="coerce")
    reviews.dropna(subset=["fecha"], inplace=True)

    surveys = data["surveys"]
    surveys.dropna(subset=["client_id", "idProducto", "comentario"], inplace=True)
    surveys = surveys[surveys["puntajeSastifacion"].between(0, 10)]

    return clients, products, social, reviews, surveys

