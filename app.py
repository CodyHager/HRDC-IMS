from flask import Flask, request, Response, render_template, redirect
from src.model.product import Product, db


app = Flask(__name__, static_url_path='', static_folder='static')

with db:
    db.create_tables([Product])

# This hook ensures that a connection is opened to handle any queries
# generated by the request.
@app.before_request
def _db_connect():
    db.connect()


# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()