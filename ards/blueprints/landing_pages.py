from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask import current_app as app
import json

landing_pages_bp = Blueprint('landing_pages', __name__, url_prefix='/ards')

@landing_pages_bp.route('/')
def index():
    return redirect(url_for('.home'))

@landing_pages_bp.route('/home')
def home():
    return render_template('/landing_pages/home.html')

@landing_pages_bp.route('/about')
def about():
    return render_template('/landing_pages/about.html')

@landing_pages_bp.route('/contact')
def contact():
    return render_template('/landing_pages/contact.html')

@landing_pages_bp.route('/faq')
def faq():
    with app.open_resource('static/faq.json') as faqjson:
        faq_data = json.load(faqjson)
    return render_template('/landing_pages/faq.html', faq_data=faq_data)

@landing_pages_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'rex' and password == 'client1234':
            session['username'] = username
            return redirect(url_for('account_pages.dashboard', username=username))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('.login', error='true')) 
    return render_template('/landing_pages/login.html')
