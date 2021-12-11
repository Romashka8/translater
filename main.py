from flask import Flask, render_template, request, session, redirect, url_for
from textblob import TextBlob, exceptions

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["SECRET_KEY"] = "Very&Strong%#Key*"

@app.route("/")
def index():
	session["origin_text"] = ""
	session["translated_text"] = ""
	session["lang_from"] = "ai"
	session["lang_to"] = "ru"
	return redirect(url_for("translater"))

@app.route("/translater", methods=["POST", "GET"])
def translater():
	if request.method == "POST":
		session["origin_text"] = request.form.get("origin")
		if len(session["origin_text"]) > 1:
			try:
				blob = TextBlob(session["origin_text"])
				session["translated_text"] = str(blob.translate(to=session["lang_to"]))
			except exceptions.NotTranslated:
				session["origin_text"] = ""
				session["translated_text"] = ""
	return render_template("index.html", origin_text=session["origin_text"], translated_text=session["translated_text"], lang_from=session["lang_from"], lang_to=session["lang_to"])

@app.route("/set_lang_from/<string:lang>")
def set_lang_from(lang):
	if len(lang) == 2: # and lang != session["lang_to"]:
		session["lang_from"] = lang
	return redirect(url_for("translater"))

@app.route("/set_lang_to/<string:lang>")
def set_lang_to(lang):
	if len(lang) == 2: # and lang != session["lang_from"]:
		session["lang_to"] = lang
	return redirect(url_for("translater"))

@app.route("/reset")
def reset():
	session["origin_text"] = ""
	session["translated_text"] = ""
	return redirect(url_for("translater"))

if __name__ == "__main__":
	app.run()