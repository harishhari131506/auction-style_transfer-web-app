from flask import Flask, render_template, url_for, request, redirect, flash, session,jsonify,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_session import Session

import os
import test
import neuralstylepro
import cv2

app = Flask(__name__)
app = Flask(__name__, template_folder='views/templates')
app.config['SECRET_KEY'] = '789654123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

import controllers

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return controllers.Handle_home()

@app.route('/about')
def about():
     return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return controllers.Handle_signup()

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return controllers.Handle_signin()

@app.route('/create_listing', methods=['GET', 'POST'])
def create_listing():
    return controllers.Handle_add_product()

@app.route('/my_bid')
def my_bid():
    return controllers.Handle_my_bid()

#https://images.hdqwalls.com/download/1/sundown-landscape-minimalist-c6-1920x1080.jpg
#-------------------------------------------------------------------------------------------------------------------------

@app.route('/stylize')
def stylize():
    return render_template('upload.html')


@app.route("/upload", methods=['POST'])
def upload():
	target = os.path.join(APP_ROOT, 'images/')
	print("TARGET", target)

	if not os.path.isdir(target):
		os.mkdir(target)
	else:
		print("Couldn't create upload directory: {}".format(target))

	data = request.form.get("style")
	print(data)

	myFiles = []

	for file in request.files.getlist("file"):
		print("file", file)
		filename = file.filename
		print("filename", filename)
		destination = "".join([target, filename])
		print("destination", destination)
		file.save(destination)
		myFiles.append(filename)
	print(myFiles)

	return render_template("complete.html", image_names=myFiles, selected_style=data)

# in this function send_image will HAVE to take in the parameter name <filename>
@app.route('/upload/<filename>')
def send_original_image(filename):
	return send_from_directory("images", filename)

# this app route cant be the same as above
@app.route('/complete/<filename>/<selected_style>')
def send_processed_image(filename, selected_style):
	directoryName = os.path.join(APP_ROOT, 'images/')

	newImg = neuralstylepro.neuralStyleTransfer(directoryName, filename, selected_style)
	
	return send_from_directory("images", newImg)

#---------------------------------------------------------------------------------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id):
    return controllers.Handle_bidding(id)

@app.route('/product/delete/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    return controllers.Handle_delete_product(id)

@app.route('/profile')
def profile():
    return controllers.Handle_profile()

@app.route('/update', methods=['GET', 'POST'])
def update():
    return controllers.Handle_update()

if __name__ == '__main__':
    app.run(debug=True)