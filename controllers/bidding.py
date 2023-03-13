from main import *
import models

def Handle_bidding(id):
    if not session.get('user'):
        return redirect(url_for('signin'))
    product = models.Product.query.filter_by(id=id).first()
    if request.method == 'POST':
        bid = request.form['bid']
        bid = float(bid)
        if session.get('user') == product.owner:
            flash('You cannot bid on your own product')
            return redirect(url_for('product', id=id))
        if bid < product.price:
            flash('Bid must be greater than current price')
            return redirect(url_for('product', id=id))
        else:
            product.price = bid
            product.bid_by = session.get('user')
            db.session.commit()
            flash('Bid placed successfully', 'success')
            return redirect(url_for('home'))

    if session.get('user') == product.owner:
        return render_template('bid.html', product=product, owner=True)
    return render_template('bid.html', product=product, owner=False)