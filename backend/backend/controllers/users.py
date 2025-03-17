from backend import db, app
from backend.models import User

from flask import request, g, jsonify


@app.post('/register')
def register():
    data = request.json
    username = data.get('username')

    # 1) Check for duplicates to avoid IntegrityError
    if not isinstance(username, str):
        return 'Missing username', 400
    if User.by_username(username) is not None:
        return 'Already registered', 400

    # 2) Use a keyword argument if you don't have a custom constructor
    user = User(username=username)
    db.session.add(user)

    try:
        db.session.commit()
    except Exception as e:
        # Log the exception, return a descriptive error to the client
        print(f"Error saving user: {e}")
        return 'Server error', 500

    return ''

@app.get('/test')
def test():
    return "test"