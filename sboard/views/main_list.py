from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('list', __name__, url_prefix='/')

@bp.route('/hello')
def hello():
    return 'Hello, Flask'

@bp.route('/')
def index():
    return redirect(url_for('views._list')) 