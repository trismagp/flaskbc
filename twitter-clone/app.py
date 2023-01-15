from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/User/trism/dev/flask/twitter-clone/engage.db'

db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
