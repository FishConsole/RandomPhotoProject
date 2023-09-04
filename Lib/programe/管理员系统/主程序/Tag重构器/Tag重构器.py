from flask import Blueprint, render_template

admin_edittag_page_bp = Blueprint('admin_edittag_page', __name__)


@admin_edittag_page_bp.route('/admin~/<token>/edittag')
def edittag_page(token):
    return render_template('admin_edittag.html')
