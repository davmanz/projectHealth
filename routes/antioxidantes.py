from flask import Blueprint, render_template

antioxidantes_bp = Blueprint('antioxidantes', __name__)

@antioxidantes_bp.route('/antioxidantes')
def antioxidantes():
    return render_template('index.html')

@antioxidantes_bp.route('/antioxidantes/info')
def antioxidantes_info():
    return render_template('antioxidantes.html')
