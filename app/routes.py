from flask import send_from_directory
from flask import request, jsonify
from app import pdf_parser
from os import path

def init_app(app):
    @app.route("/", methods=["POST"])
    def home():
        search_term = request.json["kwrd"]
        results = pdf_parser.parse_pdfs(search_term)
        return jsonify(results)


    @app.route("/uploads/<filename>")
    def upload(filename):
        img_path = path.abspath("output_imgs")
        return send_from_directory(img_path, filename)
    