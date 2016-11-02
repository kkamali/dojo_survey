from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route("/")
def greetings():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def result():
    print "Got Post Info"
    name = request.form['name']
    comment = request.form['comment']
    if (len(name) < 1):
        flash("Name cannot be empty!")
        return redirect("/")
    elif(len(comment) < 1):
        flash("Comment cannot be empty!")
        return redirect("/")
    elif(len(comment) > 120):
        flash("Comment cannot be longer than 120 characters")
        return redirect("/")
    else:
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        return render_template("result.html", name=name, location=location,language=language, comment=comment)

app.run(debug=True)
