# user authentication and registration
from . import db, models

USERS = "users"

def register(username, password, student_id, is_admin=False):
    users = db.read(USERS)
    if any(u["username"] == username for u in users):
        raise ValueError("username_exists")
    user = models.make_user(username, password, student_id, is_admin)
    users.append(user)
    db.write(USERS, users)
    return user

def login(username, password):
    users = db.read(USERS)
    phash = models.hash_password(password)
    for u in users:
        if u["username"] == username and u["password_hash"] == phash:
            return u
    return None

def ensure_admin_exists():
    users = db.read(USERS)
    if not any(u.get("is_admin") for u in users):
        # create a default admin
        admin = models.make_user("admin", "admin123", "ADMIN001", is_admin=True)
        users.append(admin)
        db.write(USERS, users)
