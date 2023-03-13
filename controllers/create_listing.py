from main import *
from datetime import datetime
import models

def Handle_add_product():
    if not session.get('user'):
        return redirect(url_for('signin'))
    if request.method == 'POST':
        # Get the data from the form
        name = request.form['name']
        description = request.form['description']
        category = request.form['category']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        image = request.form['image']
        seller = session.get('user')
        live = True
        price = request.form['price']
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        # Create a new product
        new_product = models.Product(name=name, description=description, image=image, categary=category, start_date=start_date_obj, end_date=end_date_obj, live=live, price=price, owner=seller)
        # Add the product to the database
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully', 'success')
        return redirect(url_for('home'))
    return render_template('add_product.html')