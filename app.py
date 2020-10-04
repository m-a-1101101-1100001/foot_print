from flask import Flask
from commands import test
from commands import pairs

app = Flask(__name__)

app.register_blueprint(test.bp)
app.register_blueprint(pairs.bp)
