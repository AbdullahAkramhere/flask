from fileinput import filename
from flask import *  
from werkzeug.utils import secure_filename
app = Flask(__name__)  

@app.route('/')  
def main():  
    return render_template("index.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(filename)  
        return render_template("acknownledge.html", name=filename)  

if __name__ == '__main__':  
    app.run(debug=True)