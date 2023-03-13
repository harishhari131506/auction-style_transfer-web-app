from main import *
import models

def Handle_signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Password does not match')
            return redirect(url_for('signup'))

        if len(password) < 8:
            flash('Password must be at least 8 characters')
            return redirect(url_for('signup'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = models.User( name=name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        session["user"] = user.email
        return redirect(url_for('home'))

    return render_template('signup.html')