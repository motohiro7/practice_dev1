from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///employees.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class Employee(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(100), nullable=False)
        remote = db.Column(db.String(50), nullable=False)
        department = db.Column(db.String(100), nullable=False)
        years = db.Column(db.Integer, nullable=False)

    @app.route('/')
    def hello():
        title = 'ライコンWebアプリ開発研修へようこそ!'
        return render_template('index.html', title=title)

    @app.route('/manage_employee')
    def manage_employee():
        employees = Employee.query.all()
        return render_template('manage_employee.html', employees=employees)

    @app.route('/register_employee', methods=['GET', 'POST'])
    def register_employee():
        if request.method == 'POST':
            new_employee = Employee(
                name=request.form['name'],
                email=request.form['email'],
                remote=request.form['remote_status'],
                department=request.form['department'],
                years=int(request.form['years'])
            )
            db.session.add(new_employee)
            db.session.commit()
            return redirect(url_for('manage_employee'))
        return render_template('register_employee.html')

    @app.route('/bmi')
    def bmi():
        return render_template('bmi.html')

    with app.app_context():  
        db.create_all()

    return app
