from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'J5r5V6l3O4v8D3N7u8G4t8Z5x5B4f5K'
app.config['SESSION_TYPE'] = 'filesystem'   
Session(app)
    
# Define routes
@app.route('/ards')
def index():
    return redirect('/ards/home')

@app.route('/ards/home')
def home():
    return render_template('/landing_pages/home.html')

@app.route('/ards/about')
def about():
    return render_template('/landing_pages/about.html')

@app.route('/ards/contact')
def contact():
    return render_template('/landing_pages/contact.html')

@app.route('/ards/faq')
def faq():
    with app.open_resource('static/faq.json') as faqjson:
        faq_data = json.load(faqjson)
    return render_template('/landing_pages/faq.html', faq_data=faq_data)

@app.route('/ards/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'rex' and password == 'client1234':
            session['username'] = username
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login', error='true')) 
    return render_template('/landing_pages/login.html')

@app.route('/ards/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# Modified routes to check if the username is provided in the URL
@app.route('/ards/<username>/dashboard/')
def dashboard(username):
    if 'username' in session and session['username'] == username:
        return render_template('/web_tools/dashboard.html', username=username)
    return redirect(url_for('index'))

@app.route('/ards/<username>')
@app.route('/ards/<username>/')
def account(username):
    if 'username' in session and session['username'] == username:
        return render_template('/account/account.html', username=username)
    return redirect(url_for('index'))

#Invalid URL 
@app.errorhandler(404)
def page_not_found(e):
     return render_template('/error_pages/404.html'), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
     return render_template('/error_pages/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
