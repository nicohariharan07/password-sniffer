from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <form action="/login" method="post">
      <input name="username" placeholder="username">
      <input name="password" type="password" placeholder="password">
      <button type="submit">Login</button>
    </form>
    """

@app.route("/login", methods=["POST"])
def login():
    print("Got login:", request.form)
    return "Login received!"

if __name__ == "__main__":
    app.run(port=8080)
