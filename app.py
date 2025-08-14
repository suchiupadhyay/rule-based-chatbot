from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bot import get_response

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])

def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    reply = get_response(incoming_msg)  # use your chatbot function
    resp = MessagingResponse()
    resp.message(reply)
    #resp.message("Hello  This is a test reply from Flask!")
    return str(resp)

# def whatsapp_reply():
#     # verify flast-twilio connection working
#     resp = MessagingResponse()
#     resp.message("Hello  This is a test reply from Flask!") 
#     return str(resp)


if __name__ == "__main__":
    #app.run(port=5000, debug=True)
    mode = input("Run mode? (flask/local): ").strip().lower()

    if mode == 'flask':
        app.run(host="0.0.0.0", port=5000, debug=True)
    else:
        while True:
            user_input= input("You: ")
   
            if user_input.lower() in ["exit" ,"quit"]:
                print("Bot: Goodbye!")
                break
            
            print("What user entered --> ", user_input)
            print("Bot: ",get_response(user_input))

