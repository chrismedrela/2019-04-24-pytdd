from flask import Flask, request

import calc

app = Flask(__name__)

HOME_PAGE = """
<h1>Home Page</h1>
<form method="POST">
<input name="first" /> +
<input name="second" /> =
<input type="submit" value="?" />
</form>
"""

FORM_SENT_TEMPLATE = "{first} + {second} = {sum}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        first = float(request.form['first'])
        second = float(request.form['second'])
        sum_ = calc.add(first, second)
        return FORM_SENT_TEMPLATE.format(
            first=first, second=second, sum=sum_)
    else:
        return HOME_PAGE

if __name__ == "__main__":
    app.run()
