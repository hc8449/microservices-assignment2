from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# A sample list of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you get if you cross a cat with a dark horse? Kitty Perry.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't programmers like nature? It has too many bugs.",
    "What do you call fake spaghetti? An impasta!",
    "Why was the math book sad? Because it had too many problems.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "How do you organize a space party? You planet.",
    "Why was the big cat disqualified from the race? Because it was a cheetah.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call a bear with no teeth? A gummy bear.",
    "Why don't some couples go to the gym? Because some relationships don't work out.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "What do you call a fish wearing a bowtie? Sofishticated.",
    "Why don't eggs tell jokes? Because they might crack up.",
    "Why can't you give Elsa a balloon? Because she will let it go.",
    "Why was the stadium so cool? Because it was filled with fans.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why did the computer go to the doctor? Because it had a virus.",
    "Why did the coffee file a police report? It got mugged."
]

@app.route('/jokes', methods=['GET'])
def get_jokes():
    try:
        num = int(request.args.get('num', 1))  # Default to 1 joke if num is not specified
        if num > len(jokes):
            num = len(jokes)  # Limit the number to the total number of available jokes
        selected_jokes = random.sample(jokes, num)
        return jsonify(selected_jokes)
    except ValueError:
        return jsonify({"error": "Invalid number provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
