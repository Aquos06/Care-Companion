import bcrypt   

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(str(password).encode('utf-8'),salt)
    return hashed_password

def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(str(provided_password).encode('utf-8'), str(stored_password).encode('utf-8'))