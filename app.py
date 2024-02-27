from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,static_url_path='', 
            static_folder='static')

# This will store the notes
notes = []

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', notes=notes)

@app.route('/add_note', methods=['GET','POST'])
def add_note():
    note = request.form.get('note')
    if note:
        notes.append(note)
    return redirect(url_for('home'))

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
