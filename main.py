from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                background-color: #eee;
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="POST">
        <label for="entry">Rotation amount:</label>
        <input type="text" name="rot" id="entry" value="0">
        <textarea name="text">{0}</textarea>
        <input type="submit" name="submit">
      </form>
    </body>
</html>

"""

@app.route("/")
def index():
    return form.format("")

@app.route("/",methods=["POST"])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])

    encrypted_text = rotate_string(text, rot)

    return form.format(encrypted_text)
 

app.run()