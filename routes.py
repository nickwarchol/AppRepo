from app import app       # From our app package import the app variable

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/about")
def about():
    me = {
        "first_name": "Nick",
        "last_name": "Warchol",
        "hobbies": "DIY stuff",
        "color":"blue" 
    }
    return 