import os
from flask import Flask, render_template, jsonify, Response
from extensions import database, commands
from scraping.medium_scraping import scraping_medium, fetch_medium_posts

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
database.init_app(app)
commands.init_app(app)

@app.route("/")
def index():
    medium_posts = fetch_medium_posts()
    return render_template('index.html', posts=medium_posts)


@app.route("/load")
def get_load_parser():
    scraping_medium()
    return jsonify({"success": "data parsed"}, 200)


if __name__ == "__main__":
    app.run()

