
from flask import render_template
from flask import request
from src import pdf_parser

def init_app(app):
    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            print(request.form)
            results = pdf_parser.parse_pdfs(request.form.get("kwrd"))
            print(results)

        return render_template("search.html")
    
