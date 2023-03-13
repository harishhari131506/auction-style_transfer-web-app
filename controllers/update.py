from main import *
import models

def Handle_update():
    if not session.get('user'):
        return redirect(url_for('signin'))

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        user = models.User.query.filter_by(email=session.get('user')).update(dict(name=name, phone=phone, address=address))
        db.session.commit()
        return redirect(url_for('profile'))