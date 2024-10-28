from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        #h1タグををtitle変数にして内容を動的に設定＆レンダリング
        title = "ライコンWebアプリ開発研修へようこそ!"
        return render_template('index.html', title=title)

    return app