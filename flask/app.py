from flask import Flask, render_template, abort

app = Flask(__name__) # , template_folder="views", static_folder="assets")

ARTICLES = [
    {"slug": "introduction-a-flask",
     "titre": "Introduction à Flask",
     "contenu": "Flask est un micro-framework web Python créé par Armin Ronacher en 2010."},
    {"slug": "les-routes-en-flask",
     "titre": "Les routes en Flask",
     "contenu": "Le décorateur @app.route() associe une URL à une fonction Python appelée vue."},
    {"slug": "les-templates-jinja2",
     "titre": "Les templates Jinja2",
     "contenu": "Jinja2 est le moteur de templates par défaut de Flask. Il permet d'injecter des données Python dans le HTML."},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog_index():
    return render_template("blog_index.html", articles=ARTICLES)

# @app.route("/articles/<int:id>") réponds à /articles/42 avec affectation id = 42
# def article(id:int):
@app.route("/blog/<slug>")
def article(slug):
    if slug not in (a["slug"] for a in ARTICLES):
        abort(404)

    for article in ARTICLES:
        if article["slug"] == slug:
            return render_template("blog_post.html", article=article)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True) # , port=8080)
