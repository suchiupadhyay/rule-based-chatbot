# WhatsApp Chatbot with Flask, Ngrok & Twilio

A simple rule-based chatbot that integrates with WhatsApp using Twilio API and Flask as the backend.
The app runs locally and uses ngrok to expose it to Twilio’s webhooks.


## 📌 Features
- Receive WhatsApp messages via Twilio Webhook.

- Respond using your own chatbot logic.

- Works locally — no need for cloud hosting.

- Uses ngrok for public HTTPS tunneling.

- Easy to customize bot responses.

- Easy to modify intents via JSON files.

- Handles typos with fuzzy matching.

- No heavy external libraries needed.



## 🛠️ Tech Stack

- Python 3.9+

- Flask – lightweight web framework.

- Twilio API – for WhatsApp integration.

- Ngrok – exposes your localhost to the internet.

- Regex / JSON – for rule-based responses.



## 📂 Project Structure
```
project/
│
├── app.py                  # Main Flask application
├── bot.py                  # Chatbot logic (get_response function)
├── intents_keywords.json   # Keyword matching rules
├── patterns.json           # Regex matching rules
├── responses.json          # Bot responses
├── requirements.txt        # Dependencies
└── README.md               # This file
```




## ⚙️ Installation

1. Create and activate a virtual environment

2. Install ngrok (if not installed)
        Download from https://ngrok.com/download
    OR 
        install via pip: 
        pip install pyngrok

3. Install dependencies :pip install -r requirements.txt



## 🧭 Step-by-Step: Flask → ngrok → Twilio (WhatsApp)

1. Start Flask
    - Chatbot> python app.py 

2. Start ngrok in a new terminal
    - ngrok http 5000
    - Copy the https://<something>.ngrok.io URL.

3. Connect Twilio Webhook
    - Go to Twilio Console → WhatsApp Sandbox
    - Set Webhook URL to:   https://<ngrok-id>.ngrok.io/whatsapp
    - Save changes.

4. Test on WhatsApp     
    - Join the Twilio Sandbox by sending their join code to <number given by twilio>
    - Send a message to your bot and see the response.


### Technical flow of my chatbot:
``` 
WhatsApp user → Twilio (WhatsApp API) → sends POST request → ngrok public URL → Flask app → get_response() → reply sent back → Twilio → WhatsApp user.
```



## ⚙️ How It Works

Step 1 → Check regex patterns in intent_patterns.json.

Step 2 → If no match, check keywords in intent_keywords.json.

Step 3 → If still no match, try simple fuzzy matching to guess the closest keyword.

#### User input → Find matching keywords/patterns → Identify intent → Fetch response.



## 🖥 Running the Chatbot

You can run the chatbot in two modes:

1. #### Terminal (local) mode:
For quick testing in the command line:  python app.py
    You will be prompted: Run mode? (flask/local): local

2. #### Flask (web) mode:
For integrating with ngrok / Twilio / web apps:
    You will be prompted: Run mode? (flask/local): flask
    * Serving Flask app 'app'
    * Debug mode: on



## 📌 Notes :

Ngrok session expires after ~2 hours on free tier. Restart it when needed.

bot logic is in bot.py — modify it to suit your needs.

If your setup needs to run 24/7, consider Gunicorn + Render/Heroku instead of ngrok.

