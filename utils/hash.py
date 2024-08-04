import os
import bcrypt   

def hash_password(password):
    # Ensure password is a string
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    
    # Convert password to bytes
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))