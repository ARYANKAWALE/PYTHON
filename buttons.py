from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # Added GET so you can visit it in a browser
def handle_choices():
    gender = request.form.get('gender')
    hobbies = request.form.getlist('hobby')
    return f"Gender: {gender}, Hobbies: {', '.join(hobbies)}"

# ALWAYS PUT THIS AT THE BOTTOM
if __name__ == "__main__":
    app.run(debug=True)
