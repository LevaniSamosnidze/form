from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)

# გარე გარემოდან ვიღებთ ბაზის მისამართს (Render-ზე ავტომატურად გადაეცემა)
DATABASE_URL = os.environ.get('DATABASE_URL')

# მონაცემთა ბაზის კავშირის ფუნქცია
def get_connection():
    return psycopg2.connect(DATABASE_URL)

# ბაზაში ცხრილის შექმნა (ერთხელ ხდება)
def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS emails (
                    id SERIAL PRIMARY KEY,
                    name TEXT,
                    email TEXT
                );
            """)
            conn.commit()

create_table()

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def send_Email():
    name = request.form['full_name']
    email = request.form['email']

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO emails (name, email) VALUES (%s, %s);", (name, email))
            conn.commit()

    return {'name': name, 'email': email}

if __name__ == "__main__":
    app.run(debug=True)
