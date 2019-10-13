from flask import Flask, request, jsonify
from pyfcm import FCMNotification
from firebase import firebase

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def sendNotification():
    push_service = FCMNotification(api_key="AIzaSyC9k26q5YLSn5aO5qy0A62MgYE3PNJ6jRk")
    registration_id = "e5fJJBBdhNQ:APA91bHwyPIEZEtpy7ge_ywzrXVD18LyuvOlO5zXtbU7ToxBwze-dXNvoaBfNVPv8yRFxSqpC83pEPvGFgPrBYOnf58oQgMluBoxClqgFy1J4yNXp3aj1W19r5z9OgkNDuk1tJMw7Ul6"
    message_title = "Hello from college project"
    message_body = "U got to know what you r doing in life !!!"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    print(result)
    result = jsonify({"output":str(result)})

    return result

if __name__ == "__main__":
    app.run(debug = True)
