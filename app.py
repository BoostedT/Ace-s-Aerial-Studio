from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save to submissions.txt
        try:
            with open("submissions.txt", "a") as f:
                f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n{'-'*40}\n")
            flash("Thank you for your message! We'll get back to you soon.", "success")
        except Exception as e:
            flash("An error occurred while saving your message. Please try again later.", "error")
            print(f"Error writing to file: {e}")

        return redirect('/contact')

    return render_template('contact.html')

@app.route('/new-submission', methods=['GET', 'POST'])
def new_submission():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            with open("submissions.txt", "a") as f:
                f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n{'-'*40}\n")
            flash("Thank you for your submission! We'll get back to you soon.", "success")
        except Exception as e:
            flash("An error occured when making your submission. Please try again later", "error")
            print("Error submitting request: {}".format(e))

        return redirect('/submissions')

    return render_template('new-submissions.html')

@app.route('/pending', methods=['GET', 'POST'])
def pending_submission():
    return render_template('pending_submissions.html')

USERNAME = "admin"
PASSWORD = "password123"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            flash("Successfully logged in!", "success")
            return redirect('/submissions')
        else:
            flash("Invalid credentials. Please try again.", "error")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You have been logged out.", "success")
    return redirect('/login')

@app.route('/submissions')
def submissions():
    if not session.get('logged_in'):
        flash("Please log in to view this page.", "error")
        return redirect('/login')

    try:
        with open("submissions.txt", "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        data = ["No submissions found."]

    return render_template('submissions.html', data=data)

@app.route('/map')  # New route for the map
def map():
    return render_template('map.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        flash("Successfully created account!", "success")
        return redirect('submissions')
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)