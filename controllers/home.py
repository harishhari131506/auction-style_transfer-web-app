from main import *
import models
from datetime import datetime
import datetime as dt
import math

def Handle_home():
    if not session.get('user'):
        return redirect(url_for('signin'))
    products = models.Product.query.filter_by(live=1).all()
    if not products:
        return render_template('No_product.html')
    for product in products:
        if product.end_date < datetime.now():
            product.live = 0
            product.winner = product.bid_by
            db.session.commit()
        time_left = product.end_date - datetime.now()
        time = math.ceil(time_left / dt.timedelta(hours=1))
        product = product.__dict__
        product['time_left'] = time
    return render_template('home.html', products=products)