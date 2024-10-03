from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database Connection
conn = pymysql.connect(host='localhost', user='root', password='', database='employee_management')


# Email Validator Function
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/employees')
def employee_list():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template('employee_list.html', employees=employees)


@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        salary = request.form['salary']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']
        address = request.form['address']
        hire_date = request.form['hire_date']

        if not is_valid_email(email):
            flash('Invalid email format')
            return redirect(url_for('add_employee'))

        # Encrypt the password
        hashed_password = generate_password_hash(password)

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO employees (name, position, salary, email, password, phone_number, address, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (name, position, salary, email, hashed_password, phone_number, address, hire_date))
        conn.commit()
        flash('Employee Added Successfully')
        return redirect(url_for('employee_list'))

    return render_template('add_employee.html')


@app.route('/update_employee/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        salary = request.form['salary']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']
        hire_date = request.form['hire_date']

        if not is_valid_email(email):
            flash('Invalid email format')
            return redirect(url_for('update_employee', id=id))

        cursor.execute("""
            UPDATE employees SET name=%s, position=%s, salary=%s, email=%s, phone_number=%s, address=%s, hire_date=%s WHERE id=%s
        """, (name, position, salary, email, phone_number, address, hire_date, id))
        conn.commit()
        flash('Employee Updated Successfully')
        return redirect(url_for('employee_list'))

    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cursor.fetchone()
    return render_template('update_employee.html', employee=employee)


@app.route('/delete_employee/<int:id>', methods=['GET', 'POST'])
def delete_employee(id):
    cursor = conn.cursor()

    if request.method == 'POST':
        cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
        conn.commit()
        flash('Employee Deleted Successfully')
        return redirect(url_for('employee_list'))

    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cursor.fetchone()
    return render_template('delete_employee.html', employee=employee)


if __name__ == '__main__':
    app.run(debug=True)
