import random
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Expanded responses for different domains
responses = {
    "greeting": [
        "Hello! How can I assist you today?",
        "Hi there! Do you have a health-related question?"
    ],
    "goodbye": [
        "Take care and stay healthy!",
        "Goodbye, wishing you good health!"
    ],
    "thanks": [
        "You're welcome!",
        "Glad I could help!"
    ],
    "fever": [
        "A fever is often a sign of infection. Stay hydrated, rest, and monitor your temperature. If it goes above 102°F (39°C), consult a doctor."
    ],
    "cough": [
        "A cough may come from a cold, allergies, or infection. Drink warm fluids and rest. If it's persistent or produces blood, seek medical attention."
    ],
    "headache": [
        "Headaches can result from stress, dehydration, or lack of sleep. Drink water, rest, and consider over-the-counter medication. If severe or frequent, consult a doctor."
    ],
    "stomach": [
        "Stomach pain may be indigestion, food poisoning, or other issues. Stay hydrated and eat light foods. If pain is severe or prolonged, see a doctor."
    ],
    "chest_pain": [
        "Chest pain can be serious. If it's sudden, severe, or accompanied by shortness of breath, sweating, or dizziness, call emergency services immediately. Otherwise, consult a doctor as soon as possible."
    ],
    "mental_health": [
        "Taking care of your mental health is important. Try relaxation techniques, regular exercise, and talk to someone you trust. If feelings persist, consider professional help."
    ],
    "diet": [
        "A balanced diet should include fruits, vegetables, whole grains, lean proteins, and plenty of water. Limit processed foods and sugar."
    ],
    "exercise": [
        "Aim for at least 30 minutes of moderate exercise most days—like walking, cycling, or yoga. Regular activity supports both physical and mental health."
    ],
    "first_aid": [
        "For small cuts, wash with clean water, apply antiseptic, and cover with a bandage. For serious injuries, seek medical help immediately."
    ],
    "default": [
        "I’m not sure I understand. Could you rephrase your question?",
        "I can help with general health advice like symptoms, diet, exercise, and first aid."
    ]
}

# Keywords mapped to intents
symptom_keywords = {
    "fever": ["fever", "temperature", "chills", "hot"],
    "cough": ["cough", "throat", "phlegm"],
    "headache": ["headache", "migraine", "head pain"],
    "stomach": ["stomach", "abdominal", "belly", "nausea"],
    "chest_pain": ["chest", "chest pain", "heart pain", "tightness"],
    "mental_health": ["stress", "anxiety", "depression", "sad", "lonely"],
    "diet": ["diet", "food", "nutrition", "eat", "meal"],
    "exercise": ["exercise", "workout", "fitness", "run", "yoga"],
    "first_aid": ["cut", "burn", "injury", "bleeding", "wound"]
}
#greetings
def get_intent(user_input):
    doc = nlp(user_input.lower())
    tokens = [token.text for token in doc]

    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    elif any(word in tokens for word in ["thanks", "thank you"]):
        return "thanks"

    for intent, keywords in symptom_keywords.items():
        if any(word in user_input.lower() for word in keywords):
            return intent

    return "default"

def chatbot():
    print("🤖 HealthBot: Hello! I'm your offline health assistant. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "stop"]:
            print("🤖 HealthBot: Goodbye! Stay safe.")
            break

        intent = get_intent(user_input)
        response = random.choice(responses[intent])
        print("🤖 HealthBot:", response)

# Run chatbot
if __name__ == "__main__":
    chatbot()
