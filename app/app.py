from flask import Flask 
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Customer Platform"

@app.route("/health")
def health():
    return "healthy"

@app.route("/customers/search")
def search():
    return "Customer search working"

@app.route("/db")
def db():
    conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME", "customerdb"),
    user=os.getenv("DB_USER", "customer"),
    password=os.getenv("DB_PASSWORD")
)

    conn.close()
    return "Database connection successful"

app.run(host="0.0.0.0", port=8081)