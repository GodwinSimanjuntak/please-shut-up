USERS = []


def signup(email, password):
    if len(password) < 8:
        raise ValueError("password too short")
    USERS.append({"email": email, "password": password})
    return True
