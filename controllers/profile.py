from main import *

import models

def Handle_profile():
    if not session.get('user'):
        return redirect(url_for('signin'))
    user = models.User.query.filter_by(email=session.get('user')).first()
    products = models.Product.query.filter_by(owner=session.get('user')).all()
    return render_template('profile.html', user=user, products=products)