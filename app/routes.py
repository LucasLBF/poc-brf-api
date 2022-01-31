
from flask import render_template
from flask import request
from app import pdf_parser
import pprint

def init_app(app):
    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            print(request.form)
            results = pdf_parser.parse_pdfs(request.form.get("kwrd"))
            return render_template("search.html", results=results)

        return render_template("search.html")
    