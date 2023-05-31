from flask import Flask, render_template, request, redirect, url_for
import pymssql
from flask import jsonify

app = Flask(__name__)

# Database configuration
app.config['DATABASE_SERVER'] = 'localhost'
app.config['DATABASE_NAME'] = 'test'
app.config['DATABASE_USER'] = 'SA'
app.config['DATABASE_PASSWORD'] = 'Josh@123'

# Helper function to get a database connection
def get_db():
    conn = pymssql.connect(server=app.config['DATABASE_SERVER'],
                           database=app.config['DATABASE_NAME'],
                           user=app.config['DATABASE_USER'],
                           password=app.config['DATABASE_PASSWORD'])
    return conn


# Route to list all records
@app.route('/', methods=['GET', 'PUT'])
def list_records():
    print("list_records")
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, age, email FROM records')
    records = cursor.fetchall()
    conn.close()
    return render_template('list.html', records=records)

# Route to add a new record
@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO records (name, age, email) VALUES (%s, %s, %s)', (name, age, email))
        conn.commit()
        conn.close()
        return redirect(url_for('list_records'))
    else:
        return render_template('add.html')

# Route to get record to edit
@app.route('/get_record/<int:id>', methods=['GET'])
def get_record(id): 
    conn = get_db()
    cursor = conn.cursor()
    print("get_record request.method ",request.method)
    print('get_record IDDDDDDDDDDDDDDD ',id)
    cursor.execute('SELECT id, name, age, email FROM records WHERE id=%s', (id,))
    record = cursor.fetchone()
    conn.close()
    print('record ',record)
    if record:
        return render_template('edit.html', record=record)
    else:
        return redirect(url_for('list_records'))

# Route to edit a record
@app.route('/edit_record/<int:id>', methods=['POST'])
def edit_record(id): 
    conn = get_db()
    cursor = conn.cursor()
    print("request.method ",request.method)
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        cursor.execute('UPDATE records SET name=%s, age=%s, email=%s WHERE id=%s', (name, age, email, id))
        conn.commit()
        conn.close() 
    
    return redirect(url_for('list_records'))

@app.route('/record/<int:id>', methods=['PUT'])
def put_record(id):  
    
    print("request.json ", request.json)
    data = request.json
    print("data['name'] : ", data['name'])
    conn = get_db()
    cursor = conn.cursor()
    print("put_record request.method ",request.method)
    
    if request.method == 'PUT':
        print("inside request.method  ")
        name = data['name']
        age = data['age']
        email = data['email']
        print("id : ", id)
        print("inside request.method name  ", name)
        print("inside request.method age  ", age)
        print("inside request.method email  ", email)

        cursor.execute('UPDATE records SET name=%s, age=%s, email=%s WHERE id=%s', (name, age, email, id))
        conn.commit()
        print("cursor.rowcount ", cursor.rowcount)
        if cursor.rowcount == 1:
            # One row has been updated successfully
            print("One row has been updated successfully")
            conn.close() 
            return jsonify(success=True)
            
        else:
            # No rows updated
            conn.close() 
            return 'Error updating record'

    #return redirect(url_for('list_records'))


# Route to delete a record
@app.route('/delete_record/<int:id>', methods=['POST'])
def delete_record(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM records WHERE id=%s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('list_records'))


if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)