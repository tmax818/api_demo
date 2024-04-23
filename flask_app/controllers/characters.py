from flask_app import app, render_template
from flask_app.models.character import Character

@app.route("/")
def index():

    return render_template('index.html', characters = Character.get_data())