from flask import flash, render_template, redirect, request
from flask_app import app
from email.message import EmailMessage
import ssl
import smtplib

#landing page
@app.route('/')
def landing_page():
    return render_template("index.html")

@app.route('/services')
def services_page():
    return render_template("services.html")

@app.route('/products')
def products_page():
    return render_template("products.html")

@app.route('/gallery')
def gallery_page():
    return render_template("gallery.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/private')
def private_page():
    return render_template("private.html")

@app.route('/submit', methods=["post"])
def submit():
    data = request.form

    email_sender = 'monsterapps365@gmail.com'
    email_password = 'jtghdrrhtutapygi'
    email_reciever = 'grindboats@gmail.com'#TODO change email might be greg@cansrusLLC.com 

    subject = f'{data["name"]} would like more information'
    body = f"""
    {data['message']}
    
    Name: {data['name']}
    Email: {data['email']}
    Phone Number:{data['phone']}
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciever,em.as_string())
        flash("Message sent")

    return redirect('/contact')

# email tutorial
# https://www.youtube.com/watch?v=g_j6ILT-X0k