from app.create import create_app
from os import environ

app = create_app(config=environ.get("FLASK_COFIG", None))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)