from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#DB Connection
import psycopg

app = Flask(__name__)
CORS(app)

con = psycopg.connect(
  host = "localhost",
  database="pet-hotel"
)

# Create a cursor
cur = con.cursor()

# Execute a query 
cur.execute("SELECT * FROM pets")

#Retrieve query results
records = cur.fetchall()

# creates route @ used for Flask
@app.route('/')
# define the function for this route
def index():
  # return render_template('index.html')
  return 'Hello World from Pod-3'

if __name__ == "__main__":
  app.run(debug=True)