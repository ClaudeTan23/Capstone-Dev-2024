from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="images", static_url_path="/images")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)

@app.route('/fonts/<path:filename>')
def serve_fonts(filename):
    return send_from_directory('fonts', filename)

@app.route('/scss/<path:filename>')
def serve_scss(filename):
    return send_from_directory('scss', filename)

@app.route('/rooms')
def serve_room():
    return render_template("rooms.html")

@app.route('/reservation')
def serve_reservation():
    return render_template("reservation.html")

@app.route('/events')
def serve_events():
    return render_template("events.html")

@app.route('/contact')
def serve_contact():
    return render_template("contact.html")

@app.route('/about')
def serve_about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()