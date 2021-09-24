from flask import Flask, render_template
from gnews import GNews

app = Flask(__name__)
google_news = GNews(language="hu", country="HU", period="3d", max_results=50)
news = google_news.get_news(key="gamer hir")

@app.route("/")
def home():
    return render_template(
        "index.html",
        news = news
        )

if __name__ == "__main__":
    app.run()