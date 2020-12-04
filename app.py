from flask import Flask, render_template, url_for, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#DB Connection
import psycopg2

con = psycopg2.connect(
  host = "localhost",
  database="pet-hotel"
)

# Create a cursor
cur = con.cursor()

# Execute a query 
cur.execute('SELECT * FROM "Pets";')

#Retrieve query results
records = cur.fetchall()

# creates route @ used for Flask
@app.route('/pets', methods=['GET'])
def get_pets():
    return {'result': records}

# creates route to send data 
@app.route('/pets', methods=['POST'])
def send_pets():
  return json.dumps({"success": True}), 201

if __name__ == "__main__":
  app.run(debug=True)
#       