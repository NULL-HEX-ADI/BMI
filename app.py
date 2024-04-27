from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        height = float(request.form['height']) / 100
        weight = float(request.form['weight'])
        gender = request.form['gender']

        # Calculate BMI
        bmi = weight / (height * height)

        # Determine BMI category
        if bmi < 18.5:
            category = 'Underweight'
        elif bmi >= 18.5 and bmi < 24.9:
            category = 'Normal weight'
        elif bmi >= 24.9 and bmi < 29.9:
            category = 'Overweight'
        else:
            category = 'Obese'

        return render_template('result.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
  