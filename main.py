from pyscript import document

def account_creation(event):
    output = document.getElementById("output")
    output.innerHTML = ""

    username = document.getElementById("username").value
    password = document.getElementById("password").value

    # Username validation
    if len(username) < 7:
        output.innerHTML += "❌ Username must be at least 7 characters long.<br>"
    else:
        output.innerHTML += "✅ Username is valid.<br>"

    # Password validation
    if len(password) < 10:
        output.innerHTML += "❌ Password must be at least 10 characters long.<br>"
    elif not any(char.isalpha() for char in password):
        output.innerHTML += "❌ Password must contain at least one letter.<br>"
    elif not any(char.isdigit() for char in password):
        output.innerHTML += "❌ Password must contain at least one number.<br>"
    else:
        output.innerHTML += "✅ Password is valid."
