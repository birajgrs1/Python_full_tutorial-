from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbFlask'

mysql = MySQL(app)

@app.route('/')
def index():
    fname = 'Biraj'
    lname = 'Ghorasaine'

    cur = mysql.connection.cursor()
    # Insert data into the user table
    cur.execute('INSERT INTO `user` (fname, lname) VALUES (%s, %s)', (fname, lname))
    mysql.connection.commit()  # Commit the transaction
    cur.close()  # Close the cursor

    return "User added successfully!"

if __name__ == '__main__':
    app.run(debug=True)
