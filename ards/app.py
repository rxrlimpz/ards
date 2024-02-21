from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'J5r5V6l3O4v8D3N7u8G4t8Z5x5B4f5K'
app.config['SESSION_TYPE'] = 'filesystem'   
Session(app)
    
# Define routes
@app.route('/ards/')
@app.route('/ards')
def index():
    return redirect('/ards/home')

@app.route('/ards/home')
def home():
    return render_template('home.html')

@app.route('/ards/about_us')
def about_us():
    return render_template('about.html')

@app.route('/ards/services')
def services():
    return render_template('services.html')

@app.route('/ards/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/ards/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'client' and password == 'client1234':
            session['username'] = username
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login', error='true')) 
    return render_template('login.html')

@app.route('/ards/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# Modified routes to check if the username is provided in the URL
@app.route('/ards/<username>/dashboard/')
def dashboard(username):
    if 'username' in session and session['username'] == username:
        return render_template('dashboard.html', username=username)
    return redirect(url_for('index'))

@app.route('/ards/<username>/records/')
def records(username):
    if 'username' in session and session['username'] == username:
        return render_template('records.html', username=username)
    return redirect(url_for('index'))

@app.route('/ards/<username>/documents/')
def documents(username):
    if 'username' in session and session['username'] == username:
        return render_template('documents.html', username=username)
    return redirect(url_for('index'))

@app.route('/ards/<username>/upload/')
def upload(username):
    if 'username' in session and session['username'] == username:
        return render_template('upload.html', username=username)
    return redirect(url_for('index'))

@app.route('/ards/<username>')
def account(username):
    if 'username' in session and session['username'] == username:
        return render_template('account.html', username=username)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
