import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    internship = int(request.form['internship'])
    cgpa = float(request.form['cgpa'])
    backlogs = int(request.form['backlogs'])
    input_arr = [[internship, cgpa, backlogs]]

    with open("aptitude1.pickle", "rb") as f:
        classifier = pickle.load(f)

    ans = classifier.predict(input_arr)
    if ans[0][0] == 1:
        result = "Congratulations! You are placed."
    else:
        result = "Sorry, you are not placed."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
