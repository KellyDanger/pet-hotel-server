from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# creates route @ used for Flask
@app.route('/')
# define the function for this route
def index():
  # return render_template('index.html')
  return 'Hello World from Pod-3'

if __name__ == "__main__":
  app.run(debug=True)