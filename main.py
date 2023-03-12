from concurrent.futures import thread
from crypt import methods
import csv
import re
import secrets
import os
from datetime import datetime
from urllib import response
import urllib.request, urllib.parse
import urllib
from flask import Flask, render_template, redirect, flash, url_for, request, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, current_user, logout_user
from flask_login import LoginManager
from PIL import Image
from flask_migrate import Migrate
import requests
import random
from csv import writer
import string

import json
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgres://jziidvhglkmwop:847579f0fc359140a5a832725e61db1c3754eb6523c12849558fbfd1bfa8a2cf@ec2-34-236-94-53.compute-1.amazonaws.com:5432/d11sblr8akns3e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

# working db ⬇️
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://hgikcuqfytwhhw:0665b5b321fccc2dbed4070c7c9451877b061d4fa9e3fc32b42220016d276222@ec2-44-195-132-31.compute-1.amazonaws.com:5432/d61i5rsnofs2q2'
# working db ⬆️

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@35.222.128.215:5432/talanku'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@eligibility.central.edu.gh:5432/talanku'

# app.config['SQLALCHEMY_DATABASE_URI']='postgres://mdbmveudctmurf:a15c90f420dc141c4190c0572ec9af402b5acb13113a72578fab7d57e49aa4ac@ec2-52-205-3-3.compute-1.amazonaws.com:5432/ddn4isnkf5f11b'
app.config['SECRET_KEY'] = '5791628b21sb13ce0c676dfde280ba245'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(10), nullable=True)
    description = db.Column(db.String(), nullable = False)
    image =  db.Column (db.String(), default='default.jpg')
    trending = db.Column (db.Boolean, default = False)
    category = db.Column(db.String(), nullable=False)
    # user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    vendor = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
def __repr__(self): 
    return f"Item('{self.name}', '{self.category}', )"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    price = db.Column(db.String(), nullable=True)
    location = db.Column(db.String(), nullable=True)
    items = db.Column(db.String(), nullable=True)

# TODO add Ticketing model!
# TODO add link to poll results

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable = False)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15))
    stock = db.relationship('Item', backref='author', lazy=True)

def __repr__(self):
    return '<User %r' % self.username


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

def __repr__(self):
    return '<Category %r' % self.name

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    count = db.Column(db.String(50), nullable=False)

def __repr__(self):
    return '<Movie %r' % self.name % self.count

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.String(), nullable=False)
    event = db.Column(db.String(), nullable=True)

    def __repr__(self): 
        return f"Session - ('{self.id}', 'for: {self.event}' )"

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=True)
    phoneNumber = db.Column(db.String(), nullable=True)
    movie = db.Column(db.String(), nullable = True)
    movieConfirm =  db.Column (db.String(), nullable = True)
    tlk = db.Column(db.Boolean, nullable=True)
    probability = db.Column(db.String(), nullable=True)
    startDate = db.Column(db.String(), nullable=True)
    event = db.Column(db.String(), nullable=True)
    
    def __repr__(self): 
        return f"Movie('{self.movie}', 'Probability: {self.probability}',  )"


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    code = db.Column(db.String(), nullable=True)
    slug = db.Column(db.String(), nullable=True)
    contact = db.Column(db.String(), nullable=True)
    totalSold = db.Column(db.String(), default = 0)
    paid = db.Column(db.Boolean, nullable=True)
    cost = db.Column(db.Boolean, nullable=True)
    price = db.Column(db.Float(), nullable=True)
    charges = db.Column(db.Float(), nullable=True)
    active = db.Column(db.Boolean, nullable=True)
    organiser = db.Column(db.String(), nullable=True)
    date_ending = db.Column(db.DateTime())
    date_created = db.Column(db.DateTime(), default = datetime.utcnow())
    
    def __repr__(self): 
        return f"Event('{self.id}', 'Paid: {self.name}' )"

# CHANGES HERE SHOULD BE DONE IN generateMultipleCodes(ticket)
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=True)
    phoneNumber = db.Column(db.String(), nullable=True)
    numberOfTickets = db.Column(db.String(), nullable = True)
    confirmTickets =  db.Column (db.String(), nullable = True)
    paid = db.Column(db.Boolean, nullable=True, default=False)
    code = db.Column(db.String(), nullable=True)
    ticketCode = db.Column(db.String(), nullable=True)
    bought = db.Column(db.String(), nullable=True)
    total = db.Column(db.Float(), default=0.00)
    event = db.Column(db.String(), nullable=True)
    scanned = db.Column(db.Boolean, nullable=True, default=False)
    date_created = db.Column(db.DateTime(), default = datetime.utcnow())


    
    def __repr__(self): 
        return f"Ticket('{self.id}', 'Paid: {self.paid}'  )"


from forms import *

@app.route('/naloSms', methods=['GET', 'POST'])
def sendNaloSms(message):
    request = requests.get("https://sms.nalosolutions.com/smsbackend/clientapi/Resl_Nalo/send-message/?key=a)1ty#duwgrigdb0dc4mqa(frd2r14s46lh#0cscage_k!f#te0m3reiu39_h10k&type=0&destination=233545977791&dlr=1&source=PrestoGh&message="+message)
    print(request.content)
    return request.content

# curl --location --request GET '233XXXXXXXXXmessage=This+is+a+test+from+Mars'

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    print(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/items', picture_fn)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    # form_picture.save(picture_path)
    print ("The picture name is" + picture_fn)
    return picture_fn

def save_picture_to_firebase(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    print(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/items', picture_fn)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    print ("The picture name is" + picture_fn)
    return picture_fn

src="../static/items/92f33ab490e95eca.jpg"

def naloresponse(msisdn, message, reply):
    response = {
            "USERID": "prestoGh",
            "MSISDN":msisdn,
            "MSG":message,
            "MSGTYPE":reply
        }
    return response


def de(session):
    print("Session id: " + session["SESSIONID"]+ " \nSession Data: " + session["USERDATA"])
    ticket = Ticket.query.filter_by(sessionId = session["SESSIONID"]).first() 

    if ticket == None:
        print("Attempting to create a new session.")
        event = Event.query.filter_by(code = session["USERDATA"]).first() 
        
        if event != None: 
            print("Event:" + event.name + " has been found")
            ticket = Ticket(sessionId = session["SESSIONID"])

            try:
                db.session.add(ticket)
                db.session.commit()
                print("Ticket Session :" + ticket.sessionId + " has been created successfully")
                return ticket
            except Exception as e:
                print(e)
                print("Could not create Ticket Session " + session["SESSIONID"])
                return make_response(naloresponse(session["MSISDN"], "Sorry, we didnt find any event with that code. \nPowered By Presto Ghana", False))

        else:
            print("Could not find code: "+ session["USERDATA"])
            return make_response(naloresponse(session["MSISDN"], "Sorry, we didnt find any event with that code. \nPowered By Presto Ghana", False))

    else:
        print("Session Id: " + session["SESSIONID"] + " found!")
        print(ticket)
        return ticket


def searchitem(searchquery):
    items = Item.query.all()
    search = searchquery.split()
    foundItems = []
    print(items)
    print(search)
    for s in range(len(search)):
        # This is the word in the search bar
        print(search[s])
        for i in range(len(items)):
            print("Searching for " + search[s] + " in " + items[i].name)
            # Picks a specific item from the Database
            item_string = str(items[i].name.split()).lower()
            itemsArray = items[i].name.split()
            print(item_string)
            # Counts how many words are in that list
            item_string_count = len(items[i].name.split())
            print(item_string_count)
            # Good Code
            if item_string_count != 1:
                print("More than 1 word: " + str(item_string))
                for c in range(item_string_count):
                    item_sub_string = itemsArray[c].lower()
                    item_sub_string = item_sub_string.replace("[", "")
                    item_sub_string = item_sub_string.replace("'", "")
                    item_sub_string = item_sub_string.replace("]", "")
                    print("Item Sub String: " + item_sub_string)
                    if search[s] == item_sub_string:
                        print("found")
                        print(items[i].id)
                        foundItems.append(items[i].id)
            else:
                print("It is one word")
                item_string = item_string.replace("[", "")
                item_string = item_string.replace("'", "")
                item_string = item_string.replace("]", "")
                if search[s] == item_string:
                    print("found")
                    print(items[i].id)
                    foundItems.append(items[i].id)
                    print("We found the ff:" + str(foundItems))
            # End of Good code

            # else:
            #     print(type(search[s]))
            #     print(len(search[s]))
            #     print(type(str(items[i].name.split())))
            #     print(len(str(items[i].name.split())))
            #     res = str(items[i].name.split())    
            #     x = res.replace("[", "")
            #     y = x.replace("'", "")
            #     z = y.replace("]", "")
            #     print("Not found")
                # print(items[i].name.split())
    return foundItems

# searchResults = []
# queryResult = search('case')
# print("Found" + str(queryResult))
# for f in queryResult:
#     item = Item.query.get_or_404(f)
#     searchResults.append(item)
#     print(searchResults)


@app.route('/finditemdata/<string:itemName>', methods=['POST','GET'])
def finditemdata(itemName):
    orders = Order.query.all()
    total = 0
    for o in orders:
        if o.items.find(itemName) != -1:
            total += 1
        else:
            pass
    return str(total)


@app.route('/search', methods=['POST'])
def search():
    piw = request.args.get('q')
    print(piw)
    items = Item.query.all()
    # totalitems = Item.query.all().count()
    results = []
    # for i in items:
        # words = i.split()
        # for word in splits:
            # print(word)
    return render_template('results.html', items = items, search = 'iPhone')


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/shop<string:userid>')
def shop(userid):

    print(userid)
    return render_template('shop.html')

@app.route('/allitems')
def allitems():
    items = Item.query.all()
    return render_template('allitems.html', items = items)


@app.route("/searchal/<string:searchquery>", methods=['POST','GET'])
def searchal(searchquery):
    searchResultsArray = []
    searchresults = (searchitem(searchquery))
    print("Home" + str(searchresults))
    for i in searchresults:
        item = Item.query.get_or_404(i)
        print(item)
        searchResultsArray.append(item)
    return render_template('searchal.html', search=searchquery, items=searchResultsArray)

# def replace_all(text, dic):
#     for i, j in dic.iteritems():
#         text = text.replace(i, j)
#     return text

@app.route('/', methods=['POST','GET'])
def start():
    session['cart'] = []
    return render_template('splash.html')

@app.route('/easypill', methods=['POST','GET'])
def easypill():
    api_key = "aniXLCfDJ2S0F1joBHuM0FcmH" #Remember to put your own API Key here
    phone = "0204716768" #SMS recepient"s phone number
    message = "You have a new order please go to your dashboard and check it out"
    sender_id = "PrestoSl" #11 Characters maximum
    send_sms(api_key,phone,message,sender_id)

    data = request.data
    print(data)
    return 'Easy Pill Webhooks URL'


@app.route("/voip/<string:params>", methods=['POST','GET'])
def voip(params):
    print(params)
    with open('readme.txt', 'w') as f:
        f.write(params)
    return render_template('voip.html', textfile=params)

# def addToCard(addToCart):
#     print ("add to cart thing")
#     return redirect(url_for('index'))

@app.route("/hello/<string:itemId>", methods=['POST','GET'])
def index(itemId):
    if itemId != 0: 
        # flash(f'Added to cart.')
        cart = session['cart']
        print(cart)
    form = Search()
    items = Item.query.order_by(Item.id.desc()).limit(20).all()
    home = 'home'
    if form.validate_on_submit():
        searchquery = form.search.data
        searchquery = searchquery.lower()
        print(searchquery)
        return redirect(url_for('searchal', searchquery = searchquery)) 
    return render_template('index.html', items = items, home=home, form=form, cart=session['cart'])

@app.route('/hello', methods=['POST','GET'])
def home():
    form = Search()
    session['cart'] = []
    items = Item.query.order_by(Item.id.desc()).limit(20).all()
    # items = Item.query.all().order_by()
    home = 'home'
    shoppingCart = session['cart']
    print(type(shoppingCart))
    if form.validate_on_submit():
        searchquery = form.search.data
        searchquery = searchquery.lower()
        print(searchquery)
        return redirect(url_for('searchal', searchquery = searchquery)) 
    return render_template('index.html', items = items, home=home, form=form, cart=shoppingCart, initial=True)

@app.route('/testing')
def testing():
    return render_template('grid.html')

@app.route('/newindex')
def newindex():
    return render_template('newindex.html')

@app.route('/newabout')
def newabout():
    return render_template('newabout.html')

@app.route('/investor')
def investor():
    return render_template('investor.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/form')
def form():
    form=InvestorForm()
    # check request method
    if request.method=='POST':
        if form.validate_on_submit:
            print(form.email.data)
        return redirect(url_for('form'))
    # check form validation
    # check errors
    return render_template('form.html', form=form)

@app.route('/delivery', methods=['POST','GET'])
def delivery():
    form = DeliveryForm()
    if form.validate_on_submit():
        newOrder = Order(name = form.username.data, phone=form.phone.data, price=form.price.data, location=form.location.data, items=form.items.data)
        db.session.add(newOrder)
        db.session.commit()
        print(newOrder)
        params = "New Order " + " username: "  + "\n" + newOrder.name + "\n" + "id: " + str(newOrder.id) + '\n' + str(newOrder.phone) +'\n' + "Location: " +newOrder.location + '\n' + newOrder.items + '\n' + 'Total: Ghc' +  newOrder.price
        try:
            sendtelegram(params)
            ticketMe(newOrder.phone, newOrder.price)
        except:
            print("Well that didsnt work...")
        return redirect(url_for('reciept', orderId=newOrder.id))
    return render_template('delivery.html',form=form)

@app.route('/cart', methods=['POST','GET'])
def cart():
    shoppingCart = session['cart']
    print(shoppingCart)
    items = []
    for i in shoppingCart:
        theItem = Item.query.get_or_404(i)
        print(theItem)
        items.append(theItem)
    print(items)
    if request.method == 'POST':
        print("request.data")
        print(request.form.get('items'))
        # params = request.form.get('items')
        # sendtelegram(params)
        return redirect(url_for('delivery'))
    return render_template('myitems.html', items=items)


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str

def sendRancardMessage(phone,message):
    url = "https://unify-base.rancard.com/api/v2/sms/public/sendMessage"
    message = {
        "apiKey": "dGFsYW5rdTpUYWxhbmt1Q3U6MTY1OkFQSWtkczAxNDI0Nzg1NDU=",
        "contacts": [phone],
        "message": message,
        "scheduled": False,
        "hasPlaceholders": False,
        "senderId": "TalankuCu"
    }
    r = requests.post(url, json=message)
    print(r.text)
    return 

# @app.route('/checkValidity', methods=['GET', 'POST'])
def checkValidity(price):
    valid = ""
    if price < 50:
        valid = "airChair"
    elif price > 50:
        valid = "airBed"
    else:  
        valid = None
    return valid

# a function that sends a message to your number after successful purchase
# @app.route('/ticketMe/<string:phone>/<int:price>', methods=['GET', 'POST'])
def ticketMe(phone, price):
    code = get_random_string(10)
    print(code)
    validFor = checkValidity(price)
    print(validFor)
    if validFor != None:
        sendRancardMessage(phone,'Congratulations! Please present this code at the event to claim your ' + validFor + ' for our movie night on the 26th November. Your ticket code is: '+ str(code) + ' \n' +   'Powered by PrestoTickets')
    return code

@app.route('/remove/<int:id>')
def remove(id):
    print(id)
    shoppingCart = session['cart']
    try:
        theItem = Item.query.get_or_404(id)
        flash(' ' + theItem.name + ' has been deleted','danger')
        shoppingCart.remove(id)
        session['cart'] = shoppingCart
    except:
        flash(f'There was a problem, please try again.', 'danger')
        print('close error')
    if len(shoppingCart) < 1:
        # flash(f'Please add to your cart', 'warning')
        return redirect(url_for('index', itemId=id))
    return redirect(url_for('cart'))

@app.route('/updateCart/<int:itemId>')
def updateCart(itemId):
    print(itemId)
    shoppingCart = session['cart']
    # Checks for duplication
    for i in shoppingCart:
        print(i)
        if i == itemId:
            flash(f'This item has been added to the cart.','warning')
            return redirect(url_for('home'))
    addedItem = Item.query.filter_by(id=itemId).first()
    # print("added " + addedItem)
    shoppingCart.append(itemId)
    print(shoppingCart)
    session['cart'] = shoppingCart
    flash(f' '+addedItem.name+ ' has been added to the cart.','success')
    return redirect(url_for('index', itemId=itemId))

@app.route('/preview/<int:itemid>')
def preview(itemid):
    print(session['cart'])
    item = Item.query.filter_by(id=itemid).first()
    vendor = User.query.filter_by(id = item.vendor).first()
    vendorname = vendor.username
    return render_template('preview.html', item=item, vendorname=vendorname, vendor=vendor)

@app.route('/show/<string:category>')
def show(category):
    items = Item.query.filter_by(category = category).all()
    print(items)
    return render_template('show.html', items=items, category=category)

@app.route('/additem', methods=['POST','GET'])
def additem():
    form = ItemForm()
    if form.validate_on_submit():
        pic = 'default.png'
        pictures = 'default.png'
        # if form.picture.data:
        #     print('YO!!!!!!!!! IT IS OVER HERE!!!')
            # pic = save_picture(form.picture.data)   
        # if form.other_pictures.data:
        #     for picture in form.other_pictures.data:
        #         pictures = []
        #         picture = save_picture(form.picture.data)
        #         pictures.append(picture)
        #         print (pictures)
        new_item = Item(name = form.name.data, category=form.category.data, price = form.price.data, image=form.link.data, description = form.description.data, vendor = current_user.id)
        db.session.add(new_item)
        db.session.commit()
        flash(f'New Item has been added', 'success')
        # x = datetime.now()
        # today = x.strftime("%Y/%m/%d")
        # time = x.strftime("%H:%M:%S")
        params = "New Item Added\n" + form.name.data + '\n' + "By " + current_user.username + " "
        sendtelegram(params)
        return redirect(url_for('account'))
    elif not form.is_submitted():
        print(form.errors)
        flash('There was a problem, please try again.','danger')
    return render_template('additemcopy.html', form=form)

def sendtelegram(params):
    url = "https://api.telegram.org/bot5697243522:AAEeALOhEg7MxRN7rVM1MXnUKWRVgm9eTyg/sendMessage?chat_id=-1001858967717&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content

@app.route('/test', methods=['POST','GET'])
def test():
    return render_template('asdf.html')

# @app.route('/myitems')
# def myitems():

@app.route('/reciept/<int:orderId>', methods=['POST','GET'])
def reciept(orderId):
    session['cart'] = []
    order = Order.query.get_or_404(orderId)
    return render_template('reciept.html', order=order)  

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        checkUser = User.query.filter_by(phone = form.phone.data).first()
        if checkUser:
            flash(f'This Number has already been used','danger')
            return redirect (url_for('register'))
        else:
            new_user = User(username = form.username.data, phone = form.phone.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            params = "New Account Created for " + new_user.username
            sendtelegram(params)
            flash (f'Account for ' + form.username.data + ' has been created.', 'success') 
            user = User.query.filter_by(phone = form.phone.data).first()
            login_user(user, remember=True)
            return redirect (url_for('index'))
    else:
        print(form.errors)
        flash (f'There was a problem', 'danger')
    return render_template('register.html',  form=form)

@app.route('/account')
def account():
    user = current_user
    return render_template('account.html', user=user)

@app.route('/allusers')
def allusers():
    allusers = User.query.all()
    return render_template('allusers.html', allusers=allusers)

@app.route('/categories')
def categories():
    return render_template('cat.html')

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         # Login and validate the user.
        # user should be an instance of your `User` class
        user = User.query.filter_by(phone=form.phone.data).first()
        if user and user.password==form.password.data:
            login_user(user)
            print ("Logged in:" + user.username + " " + user.phone)
            print(form.password.data)
            return redirect(url_for('home'))
        else:
            flash(f'Incorrect details, please try again', 'danger')
    return render_template('login.html', form=form)

@app.route('/bookmarks')
def bookmarks():
    return 'Done'

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/myitems')
def myitems():
    items = Item.query.filter_by(vendor = current_user.id).all()
    print(items)
    user = current_user
    return render_template('adminitems.html', items = items, user=user)

@app.route('/<int:phone>/<int:itemId>')
def item(phone, itemId):
    user = User.query.filter_by(phone = phone).first()
    item = Item.query.filter_by(id=itemId).first()
    return 'hmmmm'


@app.route('/update/<int:itemid>', methods=['POST','GET'])
def update(itemid):
    form = ItemForm()
    item = Item.query.filter_by(id = itemid).first()
    update = True
    print(item)
    if request.method == 'GET':
        print(item.image)
        form.name.data = item.name
        form.price.data = item.price
        form.description.data = item.description
        form.picture.data = item.image 
        form.link.data = item.image
        form.category.data = item.category 
    if request.method == 'POST':
        if form.validate_on_submit():
            prevPicture = item.image
            print(item.image)
            print(prevPicture)
            print("Posting new remote")
            # item = Item(name = form.name.data, description = form.description.data, price = form.price.data, image = form.link.data)
            item.name = form.name.data
            item.price = form.price.data
            item.image = form.link.data
            item.description = form.description.data
            item.category = form.category.data
            db.session.commit()
            flash(f'Your Item has been updated', 'success')
            return redirect(url_for('account'))
        else:
            flash(f'There is a problem', 'danger')
                 
    return render_template('additemcopy.html', form=form, item=item, update=update)

@app.route('/delete/<int:itemid>', methods=['POST','GET'])
def delete(itemid):
    Item.query.filter_by(id = itemid).delete()
    db.session.commit()
    return redirect(url_for('myitems'))

@app.route('/admin/delete/<string:itemid>', methods=['POST','GET'])
def admindelete(itemid):
    Item.query.filter_by(id = itemid).delete()
    db.session.commit()
    return redirect(url_for('allitems'))



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# @app.route('/sendmessage')
def sendmessage(phone, message):
    api_key = "aniXLCfDJ2S0F1joBHuM0FcmH" #Remember to put your own API Key here
    phone = phone #SMS recepient"s phone number
    message = message
    sender_id = "PrestoSl" #11 Characters maximum
    send_sms(api_key,phone,message,sender_id)
    # flash (f'Account has been verified','success')
    return 'Done'

def send_sms(api_key,phone,message,sender_id):
    params = {"key":api_key,"to":phone,"msg":message,"sender_id":sender_id}
    url = 'https://apps.mnotify.net/smsapi?'+ urllib.parse.urlencode(params)
    content = urllib.request.urlopen(url).read()
    print (content)
    print (url)


@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template("users.html", users = users)


# Request Body
@app.route('/orders', methods=['GET', 'POST'])

# Function
def orders():
    # Query is initialized to a variable - orders
    orders = Order.query.all()

    # new array is initiales
    allOrders = []

    # Iterate through the list returned by the query
    for order in orders:

        # Converting to json
        newResponse = {
            "orderId":order.id,
            "price":order.price,
            "location":order.location,
            "phone":order.phone
        }
        # After every iteration, we upload to the arra
        allOrders.append(newResponse)

    # We print all orders
    print(allOrders)

    # Make a response, this parses the data to a readable format
    response = make_response(allOrders)
    # Return the response. Which is recieved by the client.
    return response

@app.route('/neworder', methods=['GET', 'POST'])
def neworder():
    print(request.json["name"])
    print(request.json["price"])
    print(request.json["location"])
    print(request.json["phone"])


    # THis is how you create a new entry to your db.
    newOrder = Order(name = request.json['name'], phone = request.json['phone'], price=request.json['price'], location = request.json['location'])
    # You add to your session
    db.session.add(newOrder)
    # Commits the data to storage if all checks are passed.
    db.session.commit()

    newResponse = {
        "orderId": newOrder.id,
        "name":newOrder.name,
        "phone":newOrder.phone,
        "price":newOrder.price,
        "location":newOrder.location
    }

    response = make_response(newResponse)
    return response

@app.route('/getorder/<int:id>', methods=['GET', 'POST'])
def getorder(id):
    order = Order.query.get_or_404(id)
    print(order)
    jsonOrder = {
        "orderId":order.id,
        "price":order.price,
        "location":order.location,
        "phone":order.phone,
    }

    response = make_response(jsonOrder)
    return response

@app.route('/deleteOrder/<int:id>', methods=['GET', 'POST', 'DELETE'])
def deleteOrder(id):

    try:
        order = Order.query.get_or_404(id)
        db.session.delete(order)
        db.session.commit()
        response = "Order Id: " + str(id) + " was deleted successfully!"

    except:
        response = "Order Id: " + str(id) + " was not deleted!!"
   
    return make_response(response)

@app.route('/extractData', methods=['GET', 'POST'])
def extractData():

    orders = Order.query.all()

    with open('backData.csv', 'w', encoding='utf-8', newline='') as f:
        thewriter = writer(f)
        header = ['OrderId', 'Name Of Item', 'Price']
        thewriter.writerow(header)

        for t in orders:
            line = [str(t.id), t.name, t.price ]
            thewriter.writerow(line)

        return "done"

    # flash(f'' + filename +' has been downloaded successfully')

def extractNumbersFromExcel(filename):
     with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            number = line['number']

            id = id.split('-')[0]
            if status == 'paid' and len(id) <= 3:
                amount = line['amount']

                print(str(id) + " - " + amount)
            
                # find candidate and add amount to votes ... 
                candidate = Candidates.query.get_or_404(id)
                candidate.votes += float(amount)
                print(str(id) + " - " + amount)

        db.session.commit()
        all = []
        candidates = Candidates.query.all()
        for candidate in candidates:
            candidate = {
                candidate.name:candidate.votes
            }
            all.append(candidate) 
        return make_response(all)


@app.route('/broadcastMessage', methods=['GET', 'POST'])
def broadcastMessage():
    contacts = fetchAllNumbers()
    print("Done fetching numbers!")
    # message = "Welcome back to school! \nDelivery prices have been discounted till 31st January. \nStay protected, order from https://talanku.com now"
    message = "Welcome back to school! \nDelivery prices have been discounted till 18th February. \nStay protected, order from https://talanku.com now"
    for contact in contacts:
        print(contact)
        print(sendRancardMessage(contact, message))
    return "Done!" 

@app.route('/broadcastSingleMessage', methods=['GET', 'POST'])
def broadcastSingleMessage():
    contact = "0556036658"
    message = "Welcome back to school! \nDelivery prices have been discounted till 18th February. \nStay protected, order from https://talanku.com now"

    try:
        sendRancardMessage(contact,message)
    except Exception as e:
        print("Yawa")

    return "Done!" 

@app.route('/pollresults', methods=['GET', 'POST'])
def pollresults():
    array = []
    for number in Poll.query.all():
        array.append(number.phoneNumber)
    print (len(array))
    return "array"

@app.route('/fetchAllNumbers', methods=['GET', 'POST'])
def fetchAllNumbers():
    allNumbers = []
    orders = Order.query.all()
    # fetch all numbers from orders
    for number in orders:
        allNumbers.append(number.phone)
    # fetch all numbers from polls
    for number in Poll.query.all():
        allNumbers.append(number.phoneNumber)
    # fetch numbers from prontoSpreadSheet!
    with open("./static/csv/ProntoStudents.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
    # loop through prontoSpreedsheet for column with heading "number"
        for line in csv_reader:
            number = line['number']
            allNumbers.append(number)

    allNumbers = list(dict.fromkeys(allNumbers))

    finalArray = []
    for number in allNumbers:
        if number != None:
            if number.find('/'): #some numbers are 2 numbers divided by "/"
                bothNumbers = number.split("/", 1)
                for singleNumber in bothNumbers:
                    finalArray.append(singleNumber)
            elif number == " " or number == "" or number == "null" or number == "PHONE NUMBER":
                print(number + " is not being added")
                pass
            else:
                print(len(finalArray))
    return finalArray

def checkForPollSession(sessionId, data):
 # Search db for a session with that Id
    session = Poll.query.filter_by(sessionId = sessionId).first()
    # If there is none, create one
    if session == None :
        session = Ticket.query.filter_by(sessionId = sessionId).first()

        # session Data! 
    elif session:

        if session == None:
            print("Session " + sessionId + " is not in the database.")
        #  create session!
        # print("sessionId " + getSession.sessionId + " has been found")
        
        if data == '*920*127*01':
            newSession = Ticket(sessionId = sessionId)
            db.session.add(newSession)
            db.session.commit()
        else:
            newSession = Poll(sessionId = sessionId)
            db.session.add(newSession)
            db.session.commit()
            print(sessionId + " session has been created")
        session = newSession
    print(session)
    return session

@app.route('/newEvent', methods=['GET', 'POST'])
def createEvent():
    event = request.json
    print(event)

    try:
        newEvent = Event(name=event["name"], contact=event["contact"], organiser=event["organiser"], code=event["code"])
        db.session.add(newEvent)
        db.session.commit()
    except Exception as e:
        print(e)
        print("Exception!")

    return event

@app.route('/polls', methods=['GET', 'POST'])
def polls():
    poll = Movies.query.order_by(Movies.count.desc()).all()
    return render_template('polls.html', poll = poll)

def broadcastPoll(poll, msisdn):
    code = get_random_string(5)
    sendtelegram("New Poll! \n Movie - " + str(poll.movie) + "Phone: " + poll.phoneNumber +  "\n Have you heard of talanku before? - " + str(poll.tlk) + " \n Service rating - " +  str(poll.probability) )
    sendRancardMessage(msisdn,'Congratulations! your ' + poll.movie + ' recommendation for our movie night on the 26th November has been recieved. \n Poll results are live at \n https://talanku.com')


def findEvent(msisdn, id):
    event = Event.query.get_or_404(id)
    if event == None:
        return naloresponse(msisdn, "There was no event with that option please check and try again.", False )
    else:
        return event


def getAllEvents():
    events = ""
    for e in Event.query.all():
        events += "" + str(e.id) + ". " + e.name + "\n"
        print(events)
    return str(events)

@app.route('/naloussd', methods=['GET', 'POST'])
def prestoTickets():
    print(request.json)
    sessionId = request.json['SESSIONID']
    # menu = request.json['USERDATA']
    print(sessionId)
    msisdn = request.json['MSISDN']
    mobileNetwork = request.json['NETWORK']
    data = request.json['USERDATA']
    print(data)

    ticket = findTicketSession(request.json)
    print("ticket")

    if ticket:
        print(ticket)
        
        if ticket.phoneNumber == None:
            ticket.phoneNumber = msisdn
            db.session.commit()
            return make_response(naloresponse(msisdn,"Welcome to Presto Tickets\n Please choose an event. \n" + getAllEvents(), True))

        elif ticket.event == None:
            # if event not found
            print(ticket.event)
            ticket.event = data
            db.session.commit()
            return make_response(naloresponse(msisdn, "Please enter your name \n00.Go Back", True ))

        elif ticket.name == None:
            if data == "00":
                ticket.event = None
                db.session.commit()
                return make_response(naloresponse(msisdn,"Welcome to Presto Tickets\n Please choose an event. \n" + getAllEvents(), True))
            else:
                ticket.name = data
                db.session.commit()
                cost = Event.query.get_or_404(ticket.event).price
                print(ticket.event)
                return make_response(naloresponse(msisdn,"Hi "+ ticket.name +"\n1 Ticket = Ghc" + str(cost) +" \nHow many tickets are you buying? \n00. Go back", True ))

        elif ticket.numberOfTickets == None:
            if data == "00":
                print("Reversing to Name")

                ticket.name = None
                db.session.commit()
                return make_response(naloresponse(msisdn,"Please enter your name \n00.Go Back" + getAllEvents(), True))
            
            else:
                ticket.numberOfTickets = data
                print("Number Of Tickets: " + data)

                event = Event.query.get_or_404(ticket.event)
                cost = event.cost
                total = float(data) * event.price 
                charges = event.charges * total

                ticket.bought = total
                ticket.total = total + charges
                db.session.commit()

                message = "Please confirm this purchase \n" + "Number Of Tickets - " + ticket.numberOfTickets + "\nCharges: Ghc" + str(charges)  + "\nTotal: Ghc" + str(ticket.total) + "\n1.Confirm \n00.Back \n2.Cancel"  
                return make_response(naloresponse(msisdn,message, True))

        elif ticket.confirmTickets == None:
            print("Confirming Ticket")
            event = Event.query.get_or_404(ticket.event)
            if data == "00":
                ticket.numberOfTickets = None
                db.session.commit()
                # return make_response(naloresponse(msisdn,"Please enter your name \n00.Go Back" + getAllEvents(), True))
                cost = event.price
                return make_response(naloresponse(msisdn,"Hi "+ ticket.name +"\n1 Ticket = Ghc" + str(cost) +" \nHow many tickets are you buying? \n00. Go back", True ))

            elif data == "2":
                # ticket.confirmTickets = None
                # db.session.commit()
                return make_response(naloresponse(msisdn,"Thanks for using PrestoTickets" + getAllEvents(), False))

            elif data == "1":
                ticket.confirmTickets = data
                # db.session.commit()
                payementInfo={
                    "firstName":ticket.name,
                    "lastName":"Touchdown2.0",
                    "phone": "0"+msisdn[-9:],
                    "callbackUrl":"https://talanku.com/confirmTicket/"+str(ticket.id),
                    "appId":event.organiser,
                    "paymentId":ticket.id,
                    "amount":ticket.bought,
                    "total":ticket.total,
                    "ref":ticket.name,
                    "reference":ticket.name,
                    "recipient":event.organiser,
                    "percentage":str(event.charges),
                    "network":mobileNetwork
                }

                print("payementInfo")
                print(payementInfo)

                r = requests.post('https://prestoghana.com/korba', json=payementInfo)
                print(r.content)
                # print(r.json)
                return make_response(naloresponse(msisdn,"Please wait while we trigger a total payment of Ghc" + str(ticket.total) + "." , False ))

    else:
        return make_response(naloresponse(msisdn, "There was a problem. Please try again alittle later while we rectify the issue. " , False))

def randomLetters(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

@app.route('/generateMultipleCodes', methods=['GET', 'POST'])
def generateMultipleCodes(ticket):
    # generate similar codes with differing ids
    try:
        newTicket = Ticket(
            sessionId = ticket.sessionId,
            name = ticket.name,
            phoneNumber = ticket.phoneNumber,
            numberOfTickets = ticket.numberOfTickets,
            confirmTickets = ticket.confirmTickets,
            paid = ticket.paid,
            code = ticket.code,
            # TODO: ticketCode
            bought = ticket.bought,
            total = ticket.total,
            event = ticket.event,
            scanned = ticket.scanned
        )
        db.session.add(newTicket)
        db.session.commit()
    except Exception as e:
        print(e)
        print("Could not generate remainder tickets")
    return newTicket

# @app.route('/generateTicketCode/<ticketId>', methods=['GET', 'POST'])
def generateTicketCodes(ticketId):
    ticket = Ticket.query.get_or_404(ticketId)
    event = Event.query.get_or_404(ticket.event)
    numberOfTickets = int(ticket.numberOfTickets)
    print(numberOfTickets)

    ticketCodes = [] #Empty Array

    # If one, generate one, else generate one and add the others..
    initialTicket = str(ticket.id)+str(randomLetters(5))+str("PRS")+str(event.slug)+str(randomLetters(5))+str("0")
    ticketCodes.append(initialTicket)
    # First ticket has been generated

    if numberOfTickets > 1:

        for t in range(numberOfTickets - 1):
            ticket = generateMultipleCodes(ticket)

            t += 1 #Indexing to start at 1 not 0

            ticketCode = str(ticket.id)+str(randomLetters(5))+str("PRS")+str(event.slug)+str(randomLetters(5))+str(t)

            print(ticketCode.upper())
            ticketCodes.append(ticketCode)

    print("ticketCodes")
    print(ticketCodes)

    for count, t in enumerate(ticketCodes):
        count += 1
    # for t in ticketCodes:
        try:
            message = "Hi " + str(ticket.name) +" you have successfully bought " + str(ticket.numberOfTickets)+ " ticket(s) for " + event.name + "\n \nTicket " + str(count)+ ":\n" + str(t).upper() + "\nhttps://tickets.prestoghana.com/code/"+str(t).upper() + "\n \nPowered by PrestoGhana."
            # sendNaloSms(message)
            sendmessage(ticket.phoneNumber,message)
        except Exception as e:
            print(e)
            print("Couldnt send nalo sms!!!!")
        # try:
            # ticket.ticketCode = str(ticketCode)
            # print(ticketCode)
            # ticket.paid = True
            # db.session.commit()
            # print("Updated ticket: " + str(ticket.id) + " - " + ticket.name + " - " + ticket.paid)
        # except Exception as e:
            # print(e)
            # print("Couldn't create ticket!!")

    return ticketCodes

@app.route('/scanned', methods=['GET', 'POST'])
@app.route('/scanned/<int:id>', methods=['GET', 'POST'])
def scanned(id):
    ticket = Ticket.query.get_or_404(id)
    event = Event.query.get_or_404(ticket.event)
    return render_template("ticketDetails.html", ticket=ticket, event=event)

@app.route('/confirmTicket/<ticketId>', methods=['GET', 'POST'])
def confirmTicket(ticketId):
    print(ticketId)
    ticket = Ticket.query.get_or_404(ticketId)
    event = Event.query.get_or_404(ticket.event)

    try:
        print(ticket)
        print(event)
    except Exception as e:
        print("Fields are empty...")

    status = "SUCCESS"

    generated = False

    response = {
        "name":ticket.name,
        "tickets":ticket.numberOfTickets,
        "generated":generated
    }
    
    if ticket != None:
        if ticket.paid == False:
            if status == "SUCCESS":

                codes = generateTicketCodes(ticket.id)
                print(codes)

                #TODO:  Validate this please
                generated = True

            else:
                print("This transaction failed!")
        else:
            print("This ticket has been paiad for already ei!")
    else:
        print("This ticket could not be found! Warris going on???")

    return make_response(response)

    # if successful
    # if not already paid
    # Generate ticket code = 1PRS34TB24QZF
    # Send sms of confirmation wth nalo!
    # Send telegram message
    # generate qr code?

    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)