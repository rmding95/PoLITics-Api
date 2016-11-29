from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'richardding'
app.config['MYSQL_DATABASE_HOST'] = 'politicsdb.cdcme9z9rkbx.us-west-2.rds.amazonaws.com'
app.config['MYSQL_DATABASE_DB'] = 'politicsdb'
app.config['MYSQL_DATABASE_PASSWORD'] = 'politics'
mysql.init_app(app)

@app.route('/')
def index():

    return 'Hello World!'

@app.route('/db')
def connect():
    conn = mysql.connect()
    cursor = conn.cursor()
    # query = """CREATE TABLE tweets (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #  Latitude varchar(255), Longitude varchar(255), Party varchar(255), Timestamp varchar(255))"""
    #cursor.execute(query)
    query = "SELECT * FROM tweets"
    cursor.execute(query)
    return jsonify(data=cursor.fetchall())

if __name__ == '__main__':
    app.run(debug=True)