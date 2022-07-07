from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('regression')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rates = float(request.form.get('rates'))
        prediction = model.predict([[rates]])
        return render_template('index.html', result=prediction)
    else:
        return render_template('index.html', result="WAITING")


if __name__ == '__main__':
    app.run(debug=True)
