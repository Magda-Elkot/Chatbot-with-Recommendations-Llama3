# Llama3: Chatbot with Recommendations

The **Llama3** project is a sophisticated chatbot application integrated with a recommendation system, developed during a data science internship at Fixed Misr (FEDIS). This project leverages the Groq API to deliver interactive and insightful responses to user queries, along with personalized recommendations.

## Project Idea

The **Llama3** application provides a web-based interface where users can input text prompts. The system processes these prompts to generate detailed responses and offer relevant recommendations based on the user's input. This application highlights the application of advanced natural language processing and recommendation algorithms.

## Key Features

- **Interactive Chatbot**: Engage with a chatbot by submitting text prompts.
- **Asynchronous Processing**: Efficient handling of user inputs with asynchronous request processing.
- **Detailed Responses**: Receive detailed and relevant responses based on user prompts.
- **Personalized Recommendations**: Get recommendations tailored to the user's input and the generated responses.
- **User-Friendly Interface**: A clean and intuitive web interface for seamless interaction.

## How to Use

### Submit a Prompt

1. Access the application in your web browser.
2. Enter your prompt into the provided form and submit it.

### Receive Response and Recommendations

1. The chatbot will process your prompt and display the generated response.
2. Along with the response, you will receive personalized recommendations.

### View Results

1. The results, including the prompt, response, and recommendations, will be displayed on the results page.
   ![image](https://github.com/user-attachments/assets/09c1aabd-9312-4ca0-8fac-3dda92dddfee)
   ![image](https://github.com/user-attachments/assets/6c36335a-3cac-4b10-b896-7cab79876758)
   ![image](https://github.com/user-attachments/assets/d8125b60-d557-4c8d-a9af-816807b7b3c9)
   ![image](https://github.com/user-attachments/assets/7c38a888-fe13-474a-8c09-bcb7648979d7)



## Running the Application

To see the chatbot in action, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Magda-Elkot/Chatbot-with-Recommendations-Llama3.git
   cd Chatbot-with-Recommendations-Llama3

2. **Create a Virtual Environment and Install Packages**
    ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  pip install -r requirements.txt

## Configure Environment Variables

1. **Create a .env file in the root directory of the project and add your Groq API key:**
   ```bash
   GROQ_API_KEY=your_groq_api_key
   
### Start the Flask Application

1. **Run the Flask application:**
   ```bash
   python web_app.py
   
### Open Your Web Browser

1. **Navigate to http://127.0.0.1:5000 to interact with the chatbot and view results.**
