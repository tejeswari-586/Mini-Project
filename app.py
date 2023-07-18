from flask import Flask,render_template,request,redirect,session,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
#import os
#from werkzeug.utils import secure_filename
#import shutil
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:6000/mini'
db = SQLAlchemy(app)
class details(db.Model):
    first_name=db.Column(db.String(20),nullable=False)
    last_name=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(30),primary_key=True,nullable=False)
    password=db.Column(db.String(15),nullable=False)
    confirm_password=db.Column(db.String(15),nullable=False)
class books(db.Model):
    Book_id=db.Column(db.Integer(),primary_key=True)
    Firstname=db.Column(db.String(15),nullable=False)
    Lastname=db.Column(db.String(15),nullable=False)
    Email=db.Column(db.String(40),nullable=False)
    Book_name=db.Column(db.String(20),nullable=False)
    Price=db.Column(db.Integer(),nullable=False)
    Front_view=db.Column(db.String(100),nullable=False)
    Phone_Number=db.Column(db.String(10),nullable=False)
    Address=db.Column(db.String(100),nullable=False)
    Book_quality=db.Column(db.String(10),nullable=False)
    Author_name=db.Column(db.String(15),nullable=False)
    About_book=db.Column(db.String(1000),nullable=False)
    Year_of_publication=db.Column(db.Integer(),nullable=False)
@app.route("/")
def login():
    return render_template("Loginpage.html")
@app.route("/signuppage")
def signup():
    return render_template("signuppage.html")
@app.route("/homepage")
def home():
    book=books.query.all()
    return render_template("homepage.html",book=book)
@app.route("/uploadpage")
def upload():
    return render_template("Upload.html")
@app.route("/viewpage")
def view():
    book=books.query.all()
    return render_template("viewpage.html",book=book)
@app.route("/bookdetails")
def bookdet():
    Contentdata=books.query.filter_by(Book_id=request.args.get('book_id')).all()
    return render_template("bookdetail.html",book=Contentdata)
@app.route("/signuping",methods=['GET','POST'])
def sign():
    if(request.method=='POST'):
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        email=request.form.get('email')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm_password')
        if(confirm_password==password):
            entry=details(first_name=fname,last_name=lname,email=email,password=password,confirm_password=confirm_password)
        else:
            return "<h1> passwords not matched </h1>"
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('login'))
@app.route("/loginaut",methods=['GET','POST'])
def logaut():
    if(request.method=='POST'):
        email=request.form.get('email')
        password=request.form.get('password')
        check=details.query.filter_by(email=email).first()
        if(check is None):
            return '<h1>wrong user</h1>'
        else:
            if(check.password==password):
                return redirect(url_for('home'))
            else:
                return "<h1>wrong password</h1>"
    else:
        return '<h1>wrong user</h1>'

@app.route("/uploadpage",methods=['GET','POST'])
def uploaddetails():
    if(request.method=='POST'):
        Fname=request.form.get('Firstname')
        Lastname=request.form.get("Lastname")
        Email=request.form.get("email")
        Book_name=request.form.get("bookname")
        Price=request.form.get("price")
        f1=request.form.get("f1")
        Phone_Number=request.form.get("phonenumber")
        Address=request.form.get("address")
        #Phone_Number=request.form.get("phonenumber")
        Book_quality=request.form.get("dropdown")
        Author_name=request.form.get("author")
        About_book=request.form.get("about")
        Year_of_publication=request.form.get("yp")
        #print(Firstname,Lastname,Email,Book_name,Price,f1,Phone_Number,Address,Phone_Number,Book_quality,)
        #f1.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f1.filename)))
        #print(f1)
        #f1.save(os.path.join('C:\\Users\\RGUKT\\Documents\\sure trust assesments\\blog_post-master\\static\\',f1))
        #file=request.files['img']
        #filename=secure_filename(file.filename)
        entry=books(Firstname=Fname,Lastname=Lastname,Email=Email,Book_name=Book_name,Price=Price,Front_view=f1,Phone_Number=Phone_Number,Address=Address,Book_quality=Book_quality,Author_name=Author_name,About_book=About_book,Year_of_publication=Year_of_publication)
        db.session.add(entry)
        db.session.commit()
        #return "done"
        return redirect(url_for('home'))
        #entry=bookstore(Firstname=Firstname,Lastname=Lastname,Email=Email,Book_name=Book_name,Price=Price)
        #db.session.add(entry)
        #db.session.commit()
        #return "done"
@app.route('/reset')
def reset_password():
    return render_template('reset_password.html')
#@app.route('/viewpage/<Book_id>')
#def deletepost(Book_id):
#   bid=books.query.filter_by(Book_id=Book_id).first()
#   db.session.delete(bid)
#   db.session.commit()
#   return "delete successfully"
@app.route('/verify')
def verification():
    return render_template('verify.html')
@app.route("/loginauthentication",methods=['GET','POST'])
def loginauthentication():
    if(request.method=='POST'):
        email=request.form.get('email')
        password=request.form.get('password')
        book_id=request.form.get('book_id')
        check=details.query.filter_by(email=email).first()
        print(type(book_id))
        book=books.query.filter_by(Book_id=book_id).first()
        print(book.Email)
        print(type(book.Book_id))
        if(check is None):
            return redirect(url_for('verification'))
        else:
            if(check.password==password):
                if(int(book_id)==book.Book_id):
                    if(check.email==book.Email):
                        return redirect(url_for('delete',Book_id=book.Book_id))
                    else:
                        return "<h1>Error</h1>"
                else:
                    return "<h1>enter correct book_id</h1>"
            else:
                return "<h1>wrong password</h1>"
    else:
        return redirect(url_for('verification'))

@app.route('/viewpage/<Book_id>')
def deletepost(Book_id):
    return redirect(url_for('verification'))
@app.route('/loginauthentication/<Book_id>')
def delete(Book_id):
    bid=books.query.filter_by(Book_id=Book_id).first()
    db.session.delete(bid)
    db.session.commit()
    return "delete successfully"
