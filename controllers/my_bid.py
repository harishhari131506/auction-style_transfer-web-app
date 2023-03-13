from main import *
import models

def Handle_my_bid():
    if not session.get('user'):
        return redirect(url_for('signin'))
    products = models.Product.query.filter_by(bid_by=session.get('user')).all()
    if not products:
        return render_template('No_bid_yet.html')
    return render_template('my_bidding.html', products=products)