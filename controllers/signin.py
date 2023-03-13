from main import *
import models

def Handle_signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = models.User.query.filter_by(email=email).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                session["user"] = user.email
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('signin.html')