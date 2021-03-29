from flask import Blueprint, render_template, request
from sboard.models import MainContents

bp = Blueprint('views', __name__, url_prefix='/views')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    contents_list = MainContents.query.order_by(MainContents.create_date.desc())
    contents_list = contents_list.paginate(page, per_page=10)
    return render_template('main/main_list.html', contents_list=contents_list)


@bp.route('/detail/<int:contents_id>/')
def detail(contents_id):
    one_contents = MainContents.query.get_or_404(contents_id)
    return render_template('main/main_detail.html', one_contents=one_contents) 
