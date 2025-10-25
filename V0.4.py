import random

# A dictionary for predefined questions and answers
known_phrases = {
    "hello": "Hello! I'm a sentence-building bot.",
    "how are you": "I'm a bot, so I'm always fine!",
    "what can you do": "I can learn words from you and build new sentences with them.",
}

# A list to store all the words the bot has learned
learned_words = [
    "I", "can", "create", "new", "sentences", "with", "the", "words", "you", "give", "me","am","peanuts","butter","poutine","Nissan","Skyline","RB26DETT","nice","beaver","Canada","fast","why","speed","fast","makes","wheel","go","fast","guess","calculator","microwave","because","is","him","her","ah","toyota","supra","Nismo","better","yes","no","interface","error","deploy","evil","idiot","stupid","algorithm","made","honda","engine","it","top_gear","amazing","trash","garbage","code","moron","explosion","boom","giant","city"
]

def generate_sentence():
    """Generates a sentence from the learned words."""
    # The bot needs at least 5 words to create a meaningful sentence.
    if len(learned_words) < 5:
        return "I need more words to learn before I can create sentences. Please tell me more!"
   
    # Get a random number of words (between 5 and 10) to use in the sentence.
    num_words = random.randint(5, min(10, len(learned_words)))
   
    # Randomly choose words from the learned words list.
    sentence_words = random.sample(learned_words, num_words)
   
    # Join the words to form a sentence, then capitalize and add punctuation.
    sentence = " ".join(sentence_words).capitalize() + "."
    return sentence

def learn_words(user_input):
    """Adds words from the user's input to the bot's knowledge base."""
    # Split the input into individual words and filter out common punctuation.
    words = user_input.lower().split()
    for word in words:
        cleaned_word = word.strip(".,!?\"'")
        if cleaned_word and cleaned_word not in learned_words:
            learned_words.append(cleaned_word)

def chat():
    """Starts the main chat loop."""
    print("Bot: Hi! I learn words and create sentences. Type 'quit' to exit.  Version 0.4")
    while True:
        user_input = input("You: ").lower()
       
        if user_input == "quit":
            print("Bot: Goodbye!")
            break
       
        # Check for pre-programmed responses first
        if user_input in known_phrases:
            print("Bot:", known_phrases[user_input])
       
        # If no known phrase, learn from the input and generate a sentence
        else:
            learn_words(user_input)
            response = generate_sentence()
            print("Bot:", response)

# Run the chatbot
chat()

