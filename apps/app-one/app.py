from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import time
import uuid
import logging

logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s","level":"%(levelname)s","service":"user-service","msg":"%(message)s"}'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://soloman-devops-cicd.s3-website.ap-south-2.amazonaws.com"}})

START_TIME = time.time()
request_count = {"total": 0, "errors": 0}

USERS = [
    {"id": "u1", "name": "Alice Nguyen",  "email": "alice@example.com",   "role": "admin"},
    {"id": "u2", "name": "Bob Okafor",    "email": "bob@example.com",     "role": "user"},
    {"id": "u3", "name": "Charlie López", "email": "charlie@example.com", "role": "user"},
]

@app.before_request
def before():
    request.request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request.start_time = time.time()
    request_count["total"] += 1

@app.after_request
def after(response):
    ms = round((time.time() - request.start_time) * 1000, 2)
    response.headers["X-Request-ID"]    = request.request_id
    response.headers["X-Response-Time"] = f"{ms}ms"
    logger.info(f"method={request.method} path={request.path} status={response.status_code} ms={ms}")
    return response

@app.route("/")
def home():
    return jsonify({
        "service": "user-service",
        "status":  "healthy",
        "version": os.getenv("APP_VERSION", "1.0.0"),
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/users")
def users():
    return jsonify({"users": ["alice", "bob", "charlie"]}), 200

@app.route("/users/detail")
def users_detail():
    return jsonify({"users": USERS, "count": len(USERS)}), 200

@app.route("/metrics")
def metrics():
    return jsonify({
        "uptime_s":       round(time.time() - START_TIME, 1),
        "requests_total": request_count["total"],
        "requests_error": request_count["errors"],
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
