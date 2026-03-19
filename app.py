from flask import Flask, render_template, request, redirect
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

@app.route('/tutee_signup', methods=['POST', 'GET'])
def render_signup_page():
    if request.method == 'POST':
        tutee_fname = request.form.get('user_fname').title().strip()
        tutee_lname = request.form.get('user_lname').title().strip()
        tutee_email = request.form.get('user_email').lower().strip()
        tutee_password = request.form.get('user_password')

        con = connect_database(DATABASE)
        query_insert = "INSERT INTO tutees (tutee_fname, tutee_lname, tutee_email, tutee_password) VALUES (?, ?, ?, ?)"
        cur = con.cursor()
        cur.execute(query_insert, (tutee_fname, tutee_lname, tutee_email, tutee_password))
        con.commit()
        con.close()

    return render_template('tutee_signup.html')

@app.route('/tutor_signup', methods=['POST', 'GET'])
def render_tutor_signup_page():
    if request.method == 'POST':
        tutor_fname = request.form.get('user_fname').title().strip()
        tutor_lname = request.form.get('user_lname').title().strip()
        tutor_email = request.form.get('user_email').lower().strip()
        tutor_password = request.form.get('user_password')

        con = connect_database(DATABASE)
        query_insert = "INSERT INTO tutees (tutor_fname, tutor_lname, tutor_email, tutor_password) VALUES (?, ?, ?, ?)"
        cur = con.cursor()
        cur.execute(query_insert, (tutor_fname, tutor_lname, tutor_email, tutor_password))
        con.commit()
        con.close()

    return render_template('tutor_signup.html')


@app.route('/login')
def render_login():
    return render_template('login.html')


@app.route('/dashboard')
def render_dashboard_page():
    con = connect_database(DATABASE)
    query = "SELECT session_id, session_tutor, session_student, session_room, session_time FROM session_db"
    cur = con.cursor()
    cur.execute(query)
    sessions = cur.fetchall()
    print(sessions)
    con.close()

    return render_template('dashboard.html', session_data=sessions)


@app.route('/addsession', methods=['POST', 'GET'])
def render_add_page():
    if request.method == 'POST':
        session_tutor = request.form.get('session_tutor')
        session_student = request.form.get('session_student')
        session_room = request.form.get('session_room')
        session_timed = request.form.get('session_time')

        con = connect_database(DATABASE)
        query_insert = "INSERT INTO session_db (session_tutor, session_student, session_room, session_time) VALUES (?, ?, ?, ?)"
        cur = con.cursor()
        cur.execute(query_insert, (session_tutor, session_student, session_room, session_timed))
        con.commit()
        con.close()

    return render_template('addsession.html')


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)