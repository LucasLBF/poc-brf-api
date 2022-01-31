from flask import render_template
from flask import request, jsonify
from app import pdf_parser

def init_app(app):
    @app.route("/", methods=["POST"])
    def home():
        if request.method == "POST":
            search_term = request.json["kwrd"]
            results = pdf_parser.parse_pdfs(search_term)
            return jsonify(results)

        return render_template("search.html")
    