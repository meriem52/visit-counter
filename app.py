import os, socket
from flask import Flask
import redis

app = Flask(__name__)
db = redis.Redis(host=os.getenv("REDIS_HOST", "db-service"), port=6379)

@app.route("/")
def index():
    hits = db.incr("hits")
    return f"Bonjour ! Cette page a été vue {hits} fois. Je suis le conteneur {socket.gethostname()}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)