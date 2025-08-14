## First : Rule-based Chatbot for Mutual Fund.

import json
import re
import difflib

with open("intent_keywords.json") as f:
    intent_keywords = json.load(f)

with open("intent_patterns.json") as f:
    intent_patterns = json.load(f)

with open("intent_responses.json") as f:
    intent_responses = json.load(f)

def clean_text(user_input):
    text = user_input.lower()
    text = re.sub(r'[^\w\s]','',text)
    text = re.sub(r'\s+', ' ', text).strip()  
    return text

def match_keywords(user_input):
    user_input_clean = clean_text(user_input)
    user_words = re.findall(r'\b\w+\b', user_input_clean)

    for intent, keywords in intent_keywords.items():
        for keyword in keywords:
            keyword_clean = keyword.strip().lower()
            if keyword_clean in user_words:
                #response = intent_responses.get(intent,"I dont have response for that")
                print("if match_keywords intent: ", intent)
                return intent  # Return intent name, not response
    return None


def fuzzy_match_keyword(user_input, threshold=0.8):
    # Flatten keyword list
    all_keywords = []
    for intent, kw_list in intent_keywords.items():
        all_keywords.extend(kw_list)
    match = difflib.get_close_matches(user_input.lower(), all_keywords, n=1, cutoff=threshold)
    return match[0] if match else None


def match_patterns(user_input):
    user_input_clean = clean_text(user_input)
    user_words = re.findall(r'\b\w+\b', user_input_clean)

    for intent, pattern_info in intent_patterns.items():
        required_words = pattern_info.get("required_words", [])
        one_word = pattern_info.get("one_word", False)
        
        # Check if required words match
        if one_word:
            for word in required_words:
                if word.lower() in user_words:
                    print("If cond match_pattern intent:", intent)
                    return intent        
        else:
            # all required words must be present (substring match allowed)
            if all(word.lower() in user_input_clean for word in required_words):
                print("else cond match_pattern intent:", intent)
                return intent
    
    return None

def get_response(user_input):

    # Step 1: check patterns 
    intent = match_patterns(user_input)
    
    if not intent:
        # Step 2: try keywords if no match patterns found
        intent = match_keywords(user_input)

     # Step 2.1: If still no intent, try fuzzy matching
    if not intent:
        close_kw = fuzzy_match_keyword(user_input)
        if close_kw:
            # Find which intent this keyword belongs to
            for key_intent, kw_list in intent_keywords.items():
                if close_kw in kw_list:
                    intent = key_intent
                    print(f"Fuzzy matched {user_input} to keyword '{close_kw}' for intent '{intent}'")
                    break


    # Step 3: If intent matched, check if it needs to be remapped
    if intent and intent in intent_patterns:

        # Use the map_to intent if it exists, else keep original intent
        intent = intent_patterns[intent].get("map_to", intent)

    #  Step 4: Return the response for the (mapped) intent
    if intent:
        if intent in intent_responses:
            return intent_responses[intent]

     # Fallback if no intent matched or no response found
    return "Sorry! I don't understand that."
        

# while True:
#     user_input= input("You: ")
   
#     if user_input.lower() in ["exit" ,"quit"]:
#         print("Bot: Goodbye!")
#         break


#     print("What user entered --> ", user_input)
#     print("Bot: ",get_response(user_input))
