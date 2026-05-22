from flask import Flask
from blueprints.palindrome import palindrome_bp

app = Flask(__name__)

app.register_blueprint(palindrome_bp)

app.run(host="0.0.0.0", debug=True)