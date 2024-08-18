from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        current_age = int(request.form['current_age'])
        retirement_age = int(request.form['retirement_age'])
        current_savings = float(request.form['current_savings'])
        monthly_contribution = float(request.form['monthly_contribution'])
        annual_interest_rate = float(request.form['annual_interest_rate'])

        years_to_retirement = retirement_age - current_age
        total_savings = current_savings

        for _ in range(years_to_retirement * 12):
            total_savings += monthly_contribution
            total_savings *= (1 + annual_interest_rate / 100 / 12)

        return render_template('result.html', total_savings=total_savings)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
