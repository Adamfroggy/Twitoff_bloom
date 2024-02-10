from flask import Flask, render_template
from models import DB, User, Tweet


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='My rental home',
                               users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()

        adam = User(id=1, username='adam')
        katie = User(id=2, username='katie')

        tweet1 = Tweet(id=1, text='This is Adam shouting out on twitoff',
                       user=adam)
        tweet2 = Tweet(id=2, text='Hello all this is Katie', user=katie)
        tweet3 = Tweet(id=1, text='Did we hear about Miami', user=adam)
        tweet4 = Tweet(id=2, text='Tax season is coming up #yay', user=katie)
        tweet5 = Tweet(id=1, text='I hope this project works!', user=adam)
        tweet6 = Tweet(id=2, text='Loving life and my baby girl', user=katie)

        DB.session.add(adam)
        DB.session.add(katie)
        DB.session.add(tweet1)
        DB.session.add(tweet2)
        DB.session.add(tweet3)
        DB.session.add(tweet4)
        DB.session.add(tweet5)
        DB.session.add(tweet6)

        DB.session.commit()

        return render_template('base.html', title='Reset')

    return app
