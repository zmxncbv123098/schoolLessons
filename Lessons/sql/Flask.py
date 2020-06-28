from flask import redirect, Flask
from Functions import *
from UsersDB import UsersDB


app = flask.Flask(__name__)


@app.route('/test/<url>')
def main(url):
    url_id = ShortUrlToId(url)
    a = UsersDB()
    final_url = a.fetch('SELECT destination FROM links WHERE id=\'%s\'' % url_id)[0][0]
    return redirect(final_url)


if __name__ == '__main__':
    app.run(debug=True)
