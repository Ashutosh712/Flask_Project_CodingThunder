from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import json
import os
import math
from werkzeug.utils import secure_filename

"""import mysql.connector"""

app = Flask(__name__)
app.secret_key = 'super-secret-key'
local_server = True
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app.config.update(
    MAIL_SEVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_url"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_url"]

db = SQLAlchemy(app)

app.config['UPLOAD_FOLDER'] = params['upload_location']


class Contacts(db.Model):
    """Contact_Id, Name,Phone_Number,Email_Address,Message,Date_Time"""
    Contact_Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(25), nullable=False)
    Phone_Number = db.Column(db.String(12), nullable=False)
    Email_Address = db.Column(db.String(20), nullable=False)
    Message = db.Column(db.String(100), nullable=False)
    Date_Time = db.Column(db.String(20), nullable=False)


class Post(db.Model):
    """Post_Id,Title,SUb_Title,Slug,Content,Date,img_file"""
    Post_Id = db.Column(db.Integer(), primary_key=True)
    Title = db.Column(db.String(50), nullable=False)
    Sub_Title = db.Column(db.String(50), nullable=False)
    Slug = db.Column(db.String(20), nullable=False)
    Content = db.Column(db.String(500), nullable=False)
    Date = db.Column(db.String(20), nullable=False)
    img_file = db.Column(db.String(20), nullable=False)


@app.route("/")
def home_page():
    posts = Post.query.filter_by().all()
    last = math.ceil(len(posts) / int(params["no_of_post"]))
    page = request.args.get('page')

    # [0:params['no_of_post']] posts[2:1*2+2] = posts[2:4]

    if not str(page).isnumeric():
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_post']):(page - 1) * int(params['no_of_post']) + int(
        params['no_of_post'])]

    if page == 1:
        prev_page = "#"
        next_page = "/?page=" + str(page + 1)
    elif page == last:
        prev_page = "/?page=" + str(page - 1)
        next_page = "#"
    else:
        prev_page = "/?page=" + str(page - 1)
        next_page = "/?page=" + str(page + 1)

    return render_template('index.html', params=params, posts=posts, prev=prev_page, next=next_page)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard_page():
    if 'user' in session and session['user'] == params['Admin_username']:
        posts = Post.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if username == params['Admin_username'] and userpass == params['Admin_password']:
            session['user'] = username
            posts = Post.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
    else:
        return render_template('login.html', params=params)


@app.route("/edit/<string:sno>/", methods=['GET', 'POST'])
def edit_page(sno):
    if 'user' in session and session['user'] == params["Admin_username"]:
        if request.method == 'POST':
            box_title = request.form.get('title')
            box_subtitle = request.form.get('subtitle')
            box_slug = request.form.get('slug')
            box_content = request.form.get('content')
            box_image = request.form.get('img')
            if sno == '0':
                post = Post(Title=box_title, Sub_Title=box_subtitle, Slug=box_slug, Content=box_content,
                            Date=datetime.now(), img_file=box_image)
                db.session.add(post)
                db.session.commit()
            else:
                post = Post.query.filter_by(Post_Id=sno).first()
                post.Title = box_title
                post.Sub_Title = box_subtitle
                post.Slug = box_slug
                post.Content = box_content
                post.img_file = box_image
                post.Date = datetime.now()
                db.session.commit()
                return redirect("/edit/" + sno)
    post = Post.query.filter_by(Post_Id=sno).first()
    return render_template("edit.html", params=params, post=post, Post_Id=sno)


@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        """Add entry to database"""
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = request.form.get('msg')
        entry = Contacts(Name=name, Phone_Number=phone, Email_Address=email, Message=msg, Date_Time=datetime.now())
        db.session.add(entry)
        db.session.commit()

    # Use a breakpoint in the code line below to debug your script.
    return render_template('contact.html', params=params)


@app.route("/about")
def about_page():
    return render_template("about.html", params=params)


@app.route("/post/<string:post_slug>/", methods=['GET'])
def post_page(post_slug):
    post = Post.query.filter_by(Slug=post_slug).first()
    return render_template("post.html", params=params, post=post)


@app.route("/uploader", methods=['GET', 'POST'])
def uploader_page():
    if 'user' in session and session['user'] == params['Admin_username']:
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded successfully!"


@app.route("/logout")
def logout_page():
    session.pop('user')
    return redirect('dashboard')


@app.route("/delete/<string:sno>/", methods=['GET'])
def delete_page(sno):
    if 'user' in session and session['user'] == params['Admin_username']:
        post = Post.query.filter_by(Post_Id=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')


app.run(debug=True)
