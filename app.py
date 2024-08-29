from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Registro del blueprint
from routes.antioxidantes import antioxidantes_bp
app.register_blueprint(antioxidantes_bp)

# Definición del login
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('antioxidantes.antioxidantes'))
        else:
            error = 'Credenciales inválidas. Inténtalo de nuevo.'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
