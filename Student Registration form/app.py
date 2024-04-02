import hashlib
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Pwioi@2301010068',
        port=3307,
        database='registration_db'
    )
    return conn

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])

@app.route('/register', methods=['POST'])
def register():
   
    student_name = request.form['studentName']
    father_name = request.form['fatherName']
    mother_name = request.form['motherName']
    phone_number=request.form['phoneNumber']
    email = request.form['email']
    dob = request.form['dob']
    address = request.form['address']
    blood_group = request.form['bloodGroup']
    department = request.form['department']
    course = request.form['course']
    password = request.form['password']
    

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_data (student_name,father_name,mother_name,phone,email,dob,address,Blood_Group,department,course,password) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)',
                   (student_name, father_name, mother_name,phone_number,email,dob,address,blood_group,department,course,hashed_password))  # Insert the hashed password
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/users')  # Redirect to the /users route to see registered users

@app.route('/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id,student_name,father_name,mother_name,phone,email,dob,address,Blood_Group,department,course,password from user_data')
    users_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('users.html', users=users_data)


if __name__ == '__main__':
    app.run(debug=True)