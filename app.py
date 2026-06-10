from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'konkan_secret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/certificates')
@app.route('/verify')
def certificates():
    return render_template('certificates.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)