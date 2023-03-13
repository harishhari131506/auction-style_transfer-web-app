from main import *
import models

def Handle_delete_product(id):
    if not session.get('user'):
        return redirect(url_for('signin'))
    product = models.Product.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully', 'success')
    return redirect(url_for('profile'))