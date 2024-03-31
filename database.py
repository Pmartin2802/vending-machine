from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Waitlist']
collection = db['Vending Machines']

@app.route('/waitlist')
def waitlist():
    return render_template('waitlist.html')

@app.route('/')
def index():
    start_color = '#ff0000'  # Red color
    end_color = '#007bff'    # Blue color
    return render_template('homepage.html', start_color=start_color, end_color=end_color)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    business = request.form['business']
    email = request.form['email']
    phone = request.form['phone']
    
    # Insert data into MongoDB
    entry = {'name': name, 'business': business, 'email': email, 'phone': phone}
    collection.insert_one(entry)
    
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
