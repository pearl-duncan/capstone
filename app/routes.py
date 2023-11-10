from app import app, db
from flask import request, render_template, redirect, url_for, flash
from .forms import OrderForm, SignupForm, LoginForm, ReviewForm
import stripe
from .models import User, Order, db, Review
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    stripe.api_key = "sk_test_51O9th8JSD6ciGn1D1mjG9l6zHbiXZdeEijQ3TqVdbjqyc3XbcVSP6TwiZ2FHafnAKL2P9aqPMNv39QRI8Yrir9v100crrURMmk"
    product = stripe.Product.list(limit=20)
    return render_template('menu.html', product=product)



@app.route('/order-form', methods=['GET', 'POST'])
@login_required
def order():
    form = OrderForm()
    if current_user.is_authenticated:
        if request.method=="POST":
            name=request.form.get("name")
            email=request.form.get('email')
            phone = request.form.get('phone')
            pickup_or_delivery=request.form.get('pickup_or_delivery')
            date = request.form.get("date")
            item = request.form.get('item')
            quantity = request.form.get('quantity')
            description = request.form.get('description')

            order = Order(name, email, phone, pickup_or_delivery, date, item, quantity, description)

            db.session.add(order)
            db.session.commit()
    else:
        flash('Please log in to place an order')
        return redirect(url_for('gallery'))
    return render_template('order-form.html', form=form)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route("/write-review", methods=['GET', 'POST'])
@login_required
def write_review():
    form = ReviewForm()
    if current_user.is_authenticated:
        if request.method == 'POST':
            flash('form submitted!', 'success')
            name = form.name.data
            rating = request.form.get('rating')
            comments = form.comments.data

            review = Review(name=name, rating=rating, comments=comments)

            db.session.add(review)
            db.session.commit()
    else:
        flash('please log in to write a review')
        return redirect(url_for('gallery'))
    return render_template('write-review.html', form=form)

@app.route('/my-reviews')
@login_required
def my_reviews():
    review = Review.query.filter_by(name=current_user.name).all()
    print(review[0])
    return render_template('my_reviews.html', review=review)

@app.route('/update-review/<review_id>')
@login_required
def update(review_id):
    review = Review.query.get(review_id)
    if not review:
        flash('That review does not exist', 'danger')
        return redirect(url_for('home'))
    if current_user.id != review.user_id:
        flash('You cannot edit another user\'s review', 'danger')
        return redirect(url_for('my_reviews', review_id=review_id))
    form = ReviewForm()
    if request.method == 'POST':
        if form.validate():
            name = form.name.data
            rate = form.rate.data
            comments = form.comments.data

            review.name = name
            review.rate = rate
            review.comments = comments

            db.session.commit()
            flash('Successfully updated your review', 'success')
            return redirect(url_for('my_reviews', review_id=review_id))

    return render_template("my_reviews.html", r=review, form=form)

@app.route('/ind_review/<review_id>')
@login_required
def ind_review(review_id):
    review = Review.query.get(review_id)
    return render_template('ind_review.html', r=review)


@app.route('/delete-review/<review_id>')
@login_required
def delete(review_id):
    review = Review.query.get(review_id)
    if not review:
        flash('That review does not exist', 'danger')
        return redirect(url_for('home'))
    if current_user.id != review.user_id:
        flash('You cannot delete another user\'s review', 'danger')
        return redirect(url_for('my_reviews', review_id=review_id))

    db.session.delete(review)
    db.session.commit()
    flash('Successfully deleted your review!', 'success')
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        flash("Form Submitted!", 'success')
        name = form.name.data
        email = form.email.data
        birthday = form.birthday.data
        password = form.password.data
        print(name, email, birthday, password)
        if form.validate():
            name = form.name.data
            email = form.email.data
            birthday = form.birthday.data
            password = form.password.data

            user = User(name, email, password, birthday)
            print(user.birthday)

            db.session.add(user)
            db.session.commit()

            flash('Successfully creadted your accout.', 'success')
            return redirect(url_for('home'))

        else:
            flash('Invalid form, please try again', 'danger')

    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        flash("Form Submitted!", 'success')

        if form.validate():
            email = form.email.data
            print(email)
            password = form.password.data
            print(password)

            user= User.query.filter_by(email=email).first()
            print(user.password)

            if user:
                if user.password == password: #not realizing the passwords match - it thinks the bday input is the password
                    login_user(user)
                    flash("Successfully logged in", 'success')
                    return redirect(url_for('home'))

                else:
                    flash("Invalid username or password!", 'danger')
            else:
                flash('That username does not exists.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/monthly-classes')
def classes():
    return render_template('classes.html')