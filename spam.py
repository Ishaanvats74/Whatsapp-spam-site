import pywhatkit
import pyautogui
import time
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    print("Flask server is running")
    return render_template('spamSite.html')

@app.route('/spamSite',methods=['POST'])
def spam():
    mobile_number = int(request.form.get('MobileNumber'))
    message = request.form.get('Message')
    Count = int(request.form.get('RepeatCount'))

    pywhatkit.sendwhatmsg_instantly(f"+91{mobile_number}", message ,wait_time=10)
    pyautogui.press("enter")
    for i in range(Count-1):
        pyautogui.write(message)
        pyautogui.press("enter")
        time.sleep(0.5)
    return render_template('spamSite.html', result="Spam messages sent successfully!")
if __name__ == '__main__':
    app.run(debug=True)
    