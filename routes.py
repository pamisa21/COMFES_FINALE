from flask import render_template, session, request, redirect, url_for
from server import app
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

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
        username = request.form['username']
        if username:
            session['username'] = username
            return redirect(url_for("loading_screen", target=url_for("dashboard")))
        else:
            return "Username is required"
    return render_template('Auth/login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('loading_screen', target=url_for('login')))

@app.route('/register')
def register():
    return redirect(url_for('loading_screen', target=url_for("register_page")))

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