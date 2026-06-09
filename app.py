from flask import Flask
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")

client = Client(account_sid, auth_token)

@app.route("/send_sms")
def send_sms():

    message = client.messages.create(
        body="Thank you for contacting Binjaw IT Solutions.",
        from_=twilio_number,
        to="+918319688692"   # Verified number
    )

    return f"SMS Sent! SID: {message.sid}"

if __name__ == "__main__":
    app.run(debug=True)