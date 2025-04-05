from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def send_Email():
    user = {
        'name': request.form['full_name'],
        'email': request.form['email']
    }
    with open('emails.txt', 'a', encoding='utf-8') as f: 
        f.write(str(user) + '\n')
    return user

if __name__ == "__main__":
    app.run(debug=True)
