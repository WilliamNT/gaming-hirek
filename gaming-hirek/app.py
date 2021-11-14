from flask import Flask, render_template
from gnews import GNews

app = Flask(__name__)
google_news = GNews(language="hu", country="HU", period="10d", max_results=50, exclude_websites=["globalgame.hu"]) # a globalgame-t az api hibásan tálalja, ezért inkább nem foglalkozunk vele
news = google_news.get_news(key="gaming gamer hír videójáték játék játékok xbox playstation")

@app.route("/")
def home():
    return render_template(
        "index.html",
        news = news
        )

if __name__ == "__main__":
    app.run(debug=True)