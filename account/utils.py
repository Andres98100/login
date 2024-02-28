import secrets

def generate_token(user):
    token = secrets.token_hex(20)
    user.password_reset_token = token
    user.save()
    return token
