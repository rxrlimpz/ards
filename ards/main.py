from flask import Flask
from blueprints.landing_pages import landing_pages_bp
from blueprints.account_pages import account_pages_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'J5r5V6l3O4v8D3N7u8G4t8Z5x5B4f5K'
app.config['SESSION_TYPE'] = 'filesystem'   

app.register_blueprint(landing_pages_bp)
app.register_blueprint(account_pages_bp)

if __name__ == '__main__':
    app.run(debug=True)
