from project import db , login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    # Load and return the user from the database based on the user ID
    return User.query.get(int(user_id))

class User(db.Model , UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)


    
    def __repr__(self):
        return f'User(username={self.username}, email_address={self.email_address})'

    def check_password_correction(self, attempted_password):
        # Compare the provided password with the stored password (plain text comparison)
        return self.password_hash == attempted_password
    
    def get_id(self):
        return str(self.id)


def __repr__(self):
    return  f'Item{self.name}'

