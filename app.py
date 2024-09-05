from flask import Flask, request, render_template
from random import randint, choice
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)


@app.route('/form')
def show_form():
    return render_template("form.html")

COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]


@app.route('/spell/<word>')
def spell_word(word):
    return render_template("spell_word.html", word=word)


@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    compliment = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=compliment)


@app.route('/')
def home():
    """Shows home page"""
    return """
    <html>
        <body>
            <h1>Home Page</h1>
            <p>Welcome to my simple Flask app!</p>
        </body>
    <html>
    """

@app.route('/lucky')
def lucky_number():
    num = randint(1, 10)
    return render_template("lucky.html", lucky_num=num, msg="You are so lucky!")

@app.route('/hello')
def say_hello():
    """Shows hello page"""
    return render_template("hello.html")


@app.route('/search')
def search():
    """Shows search results.  Looks for term & sort in query string"""
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1> <p>Sorting by: {sort}</p>"


# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "YOU MADE A POST  REQUEST!"


# @app.route("/post", methods=["GET"])
# def get_demo():
#     return "YOU MADE A GET REQUEST!"


@app.route('/add-comment')
def add_comment_form():
    """Shows add comment form"""
    return """
    <h1>Add Comment </h1>
    <form method="POST">
      <input type='text' placeholder='comment' name='comment'/>
      <input type='text' placeholder='username' name='username'/>
      <button>Submit</button>
    </form>
  """


@app.route('/add-comment', methods=["POST"])
def save_comment():
    """Saves comment data (pretends to)"""

    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
      <h1>SAVED YOUR COMMENT</h1>
      <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
      </ul>
    """


@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing The {subreddit} Subreddit</h1>"


@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit} Subreddit</h1>"


POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo!",
    3: "Double rainbow all the way",
    4: "YOLO OMG (kill me)"
}


@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id,  "Post not found")
    return f"<p>{post}</p>"
