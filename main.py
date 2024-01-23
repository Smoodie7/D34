#!/bin/python3

from app import create_app

app = create_app()
app.secret_key = "secret"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
