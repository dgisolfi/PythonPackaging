#!/usr/bin/env python3

import connexion
from flask_cors import CORS
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir="./swagger/")
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api("swagger.yaml", arguments={"title": "Coffee ☕️"}, pythonic_params=True)
    app.run(port=8012, debug=True)


if __name__ == "__main__":
    main()
