from backend import db, app
from backend.models import User

from flask import request


@app.post('/register')
def register():
    data = request.json
    username = data.get('username')

    if not isinstance(username, str):
        return 'Missing username', 400
    if User.by_username(username) is not None:
        return 'Already registered', 400

    user = User(username=username)
    db.session.add(user)

    try:
        db.session.commit()
    except Exception as e:
        print(f"Error saving user: {e}")
        return 'Server error', 500

    return ''

@app.get('/test')
def test():
    return "test"