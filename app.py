from flask import Flask, render_template, request, redirect, url_for, flash

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

        # Save form data to submissions.txt
        try:
            with open("submissions.txt", "a") as f:
                f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n{'-'*40}\n")
            flash("Thank you for your message! We'll get back to you soon.")
        except Exception as e:
            flash("An error occurred while saving your message. Please try again later.")
            print(f"Error writing to file: {e}")

        return redirect('/contact')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

