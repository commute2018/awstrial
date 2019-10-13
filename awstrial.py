from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyC9k26q5YLSn5aO5qy0A62MgYE3PNJ6jRk")
registration_id = "e5fJJBBdhNQ:APA91bHwyPIEZEtpy7ge_ywzrXVD18LyuvOlO5zXtbU7ToxBwze-dXNvoaBfNVPv8yRFxSqpC83pEPvGFgPrBYOnf58oQgMluBoxClqgFy1J4yNXp3aj1W19r5z9OgkNDuk1tJMw7Ul6"
# message_title = "Hello from college project"
# message_body = "U got to know what you r doing in life !!!"
data = {
    "title": "hello",
    "message": "Good morning"
}
result = push_service.notify_single_device(registration_id=registration_id, data_message=data)
print(result)