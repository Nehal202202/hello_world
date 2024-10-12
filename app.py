from flask import Flask, request, render_template

#Create the Flask app

app = Flask(__name__)

#Route 1: Show the form

@app.route('/')

def form():

    return render_template('form.html')

# Route 2: Handle the form submission and show the result 
@app.route('/submit', methods=['POST'])

def submit():

#Get the data from the form.

    name = request.form['name']

    email = request.form['email']

#Pass the data to the result page
    return render_template('result.html', name=name, email=email)

# Run the app 
if __name__ == '__main__': 
    app.run(debug=True)