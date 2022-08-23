from flask import Flask,render_template,request

# instance of Flask class
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/works')
def works():
    return render_template('works.html')
@app.route('/work')
def work():
    return render_template('work.html')
@app.route('/components')
def components():
    return render_template('components.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')    
@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return render_template('thankyou.html', form_data=data)
    else :
        return "Something went wrong"
if __name__ == '__main__':
    app.run(debug=True)