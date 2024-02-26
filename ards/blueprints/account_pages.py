from flask import Blueprint, render_template, redirect, url_for, session
from flask import current_app as app

account_pages_bp = Blueprint('account_pages', __name__, url_prefix='/ards')

@account_pages_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('landing_pages.index'))

@account_pages_bp.route('/<username>/dashboard/')
@account_pages_bp.route('/<username>/dashboard')
def dashboard(username):
    if 'username' in session and session['username'] == username:
        return render_template('/web_tools/dashboard.html', username=username)
    return redirect(url_for('landing_pages.index'))

@account_pages_bp.route('/<username>/archives')
@account_pages_bp.route('/<username>/archives/')
def archives(username):
    if 'username' in session and session['username'] == username:
        return render_template('/web_tools/docs_table.html', username=username)
    return redirect(url_for('landing_pages.index'))

@account_pages_bp.route('/<username>/upload')
@account_pages_bp.route('/<username>/upload/')
def upload(username):
    if 'username' in session and session['username'] == username:
        return render_template('/web_tools/upload.html', username=username)
    return redirect(url_for('landing_pages.index'))

@account_pages_bp.route('/<username>')
@account_pages_bp.route('/<username>/')
def account(username):
    if 'username' in session and session['username'] == username:
        return render_template('/account/account.html', username=username)
    return redirect(url_for('landing_pages.index'))
