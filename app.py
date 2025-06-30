import subprocess
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    print("Flask server is running")
    return render_template('spamSite.html')



@app.route('/spamSite',methods=['POST'])
def spam():
    mobile_number = request.form.get('MobileNumber')
    message = request.form.get('Message')
    Count = request.form.get('RepeatCount')
    subprocess.run([
        'python', 'spam.py',
        str(mobile_number),
        str(message),
        str(Count)
    ])
    return render_template('spamSite.html', result="Spam messages sent successfully!")

if __name__ == '__main__':
    app.run(debug=False)