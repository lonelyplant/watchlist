import click

from watchlist import app, db
from watchlist.models import User, Movie, Comment


@app.cli.command()  # 创建一个命令行命令
@click.option('--drop', is_flag=True, help='Create after drop.') # 创建一个选项
def initdb(drop):
    """Initialize the database"""
    if drop:
        db.drop_all()
        click.echo('Dropped database.')
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'}
    ]
    comments = [
        {'comment': 'This is a comment.'},
        {'comment': 'This is a comment.'},
        {'comment': 'This is a comment.'},
        {'comment': 'This is a comment.'},
        {'comment': 'This is a comment.'},
        {'comment': 'This is a comment.'},
        {'comment': 'This is a comment.'},
        {'comment': 'This is a comment.'},
        {'comment': 'This is a comment.'},
        {'comment': 'This is a comment.'}
   ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    for c in comments:
        comment = Comment(comment=c['comment'])
        db.session.add(comment)
    db.session.commit()
    click.echo('Done.')

@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user"""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')