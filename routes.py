from flask import render_template, session, request, redirect, url_for, flash
from server import app,db
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from server import Users  # Make sure to import the Users model
from werkzeug.security import generate_password_hash, check_password_hash


# Load model and tokenizer
model_path = "./model/twitter_xlm_roberta_fine_tuned_sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Function to predict sentiment
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    predicted_class = logits.argmax().item()
    sentiment_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
    return sentiment_map.get(predicted_class, "Unknown")


@app.route('/loading_screen')
def loading_screen():
    # This route shows the loading screen, then redirects
    target = request.args.get("target")
    return render_template("loading.html", redirect_url=target)


@app.route('/')
def main():
    return redirect(url_for("loading_screen", target=url_for("main_page")))

@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['username']  # Email is used as the username
        password = request.form['password']
        
        # Check if the user exists in the database
        user = Users.query.filter_by(email=email).first()
        if user:
            # Check if the password matches
            if user.password == password:  # Direct comparison
                session['username'] = user.name  # Store username in session
                return redirect(url_for("loading_screen", target=url_for("dashboard")))
            else:
                flash("Invalid password!", "error")  # Password is incorrect
        else:
            flash("Email not found!", "error")  # Email is not registered

        return redirect(url_for("login"))  # Redirect back to login

    return render_template('Auth/login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('loading_screen', target=url_for('login')))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confpassword = request.form['confpassword']
        
        # Check if passwords match
        if password != confpassword:  
            flash("Passwords do not match!", "error")
            return redirect(url_for('register_page'))

        # Check if the user already exists
        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            flash("Email address already exists!", "error")
            return redirect(url_for('register_page'))

        # Create a new user without hashing the password
        new_user = Users(name=username, email=email, password=password)
        
        # Add and commit to the database
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('Auth/register.html')






@app.route('/register_page')
def register_page():
    return render_template('Auth/register.html')

# Other routes similarly wrapped with the loading screen
@app.route('/evaluate', methods=['GET', 'POST'])
def evaluate():
    if 'username' in session:
        sentiment = None
        if request.method == 'POST':
            comment = request.form.get('comment')
            if comment:
                sentiment = predict_sentiment(comment)
        return render_template('evaluate.html', username=session['username'], sentiment=sentiment)
    return redirect(url_for('loading_screen', target=url_for('login')))


@app.route('/loading_dashboard')
def loading_dashboard():
    return redirect(url_for("loading_screen", target=url_for("dashboard")))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)
    return redirect(url_for('loading_screen', target=url_for('login')))


# Routes for history with loading screen
@app.route('/loading_history')
def loading_history():
    return redirect(url_for("loading_screen", target=url_for("history")))

@app.route('/history')
def history():
    if 'username' in session:
        username = session['username']
        return render_template('history.html', username=username)
    return redirect(url_for('loading_screen', target=url_for('login')))


# Routes for comments with loading screen
@app.route('/loading_comments')
def loading_comments():
    return redirect(url_for("loading_screen", target=url_for("comments")))

@app.route('/comments')
def comments():
    if 'username' in session:
        username = session['username']
        return render_template('comments.html', username=username)
    return redirect(url_for('loading_screen', target=url_for('login')))


# Routes for user account with loading screen
@app.route('/loading_users_account')
def loading_users_account():
    return redirect(url_for("loading_screen", target=url_for("account")))

@app.route('/users_account')
def account():
    if 'username' in session:
        username = session['username']
        return render_template('users_account.html', username=username)
    return redirect(url_for('loading_screen', target=url_for('login')))


# Routes for profile with loading screen
@app.route('/loading_profile')
def loading_profile():
    return redirect(url_for("loading_screen", target=url_for("profile")))

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        return render_template('Users/profile.html', username=username)
    return redirect(url_for('loading_screen', target=url_for('login')))


# Routes for edit profile with loading screen
@app.route('/loading_edit_profile')
def loading_edit_profile():
    return redirect(url_for("loading_screen", target=url_for("edit_profile")))

@app.route('/edit_profile')
def edit_profile():
    if 'username' in session:
        username = session['username']
        return render_template('Users/edit_profile.html', username=username)
    return redirect(url_for('loading_screen', target=url_for('login')))


@app.route('/FQS')
def FQS():
    if 'username' in session:
        username = session['username']
        return render_template('FQS.html', username=username)
    return redirect(url_for('loading_screen', target=url_for('FQS')))


@app.route('/analys')
def analys():
    if 'username'  in session:
        username = session['username']
        return render_template('analys.html', username=username )
    return redirect(url_for('loading_screen', target=url_for('analys')))