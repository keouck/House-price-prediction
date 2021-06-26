from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')
    
@app.route('/predict_form_inputs', methods=['POST'])
def predict_form_inputs():
    
    data = [str(x) for x in request.form.values()]

    return render_template('predict.html', output=data)


if __name__ == "__main__":
    app.run(debug=True)