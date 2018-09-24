from flask import Flask, url_for
from flask import render_template
from flask import request
from twilio.rest import TwilioRestClient
import cgi
import cgitb
cgitb.enable()

app = Flask(__name__)


# Twilio Account SID - AC2c72ba04a6e9fd2d1d535543e12d1a08
# Twilio Authorization token - 60065141024e92c94f4c9449f2577c88

account = "AC2c72ba04a6e9fd2d1d535543e12d1a08"
token = "60065141024e92c94f4c9449f2577c88"
string = "additional string"
my_phone_number = "+16475631480"

 

@app.route('/')
def homepage():
	
	return render_template('index.html')

@app.route('/getMethod', methods = ['GET'])
def get():

	if request.method == 'GET':
		return "Data Retrived:"


@app.route('/postMethod', methods = ['POST'])
def post():

	if request.method == 'POST':
		send_text_message(my_phone_number)
		return "Your input was received\n"



def send_text_message(my_phone_number):
	
	#formData = cgi.FieldStorage()    Trying to get form data here -> user should input phone number
	#phone_num = formData.getvalue("phone_number")
	client = TwilioRestClient(account,token)
    
	message = client.sms.messages.create(to=my_phone_number,
		                                 from_="+16477979576",
		                                 body="Sending text message from server test is successful " + string)
        print message.sid



	

if __name__ == '__main__':

	app.run(debug=True)