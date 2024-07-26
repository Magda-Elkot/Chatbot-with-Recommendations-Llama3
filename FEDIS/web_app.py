from flask import Flask, request, render_template, jsonify
import asyncio
from app import get_groq_completion, get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    """
    Route handler for the root URL.
    Renders the index.html template.

    Returns:
        render_template: Renders the index.html template.
    """
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """
    Route handler for form submission via POST request.
    Processes the user prompt asynchronously, retrieves responses,
    and returns JSON data with the prompt, model response, and recommendations.

    Returns:
        jsonify: JSON response containing prompt, response, and recommendations.
    """
    prompt = request.form['prompt']

    # Process the prompt asynchronously
    loop = asyncio.new_event_loop() # Create a new asyncio event loop
    asyncio.set_event_loop(loop)    # Set the event loop for asyncio operations
    # Run get_groq_completion asynchronously
    response = loop.run_until_complete(get_groq_completion(prompt))
    # Run get_recommendations asynchronously
    recommendations = loop.run_until_complete(get_recommendations(prompt))

    return jsonify({'prompt': prompt, 'response': response, 'recommendations': recommendations})

if __name__ == "__main__":
    app.run(debug=True)
