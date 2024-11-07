from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        title = "ライコンWebアプリ開発研修へようこそ!"
        return render_template('index.html', title=title)

    return app