from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "C:/Users/22240/mini_project/tutor_db"

app = Flask(__name__)


def connect_database(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        print("error has occurred while connecting to the database")
    return


@app.route('/')
def render_homepage():
    return render_template('base.html')


@app.route('/dashboard')
def render_dashboard_page():
    con = connect_database(DATABASE)
    query = "SELECT session_id, session_tutor, session_tutee, session_room, session_time FROM session_db"
    cur = con.cursor()
    cur.execute(query)
    sessions = cur.fetchall()
    print(sessions)
    con.close()
    return render_template('dashboard.html', session_data=sessions)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)