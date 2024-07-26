import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Debug: Print environment variable value
print("GROQ_API_KEY:", os.environ.get("GROQ_API_KEY"))

async def get_groq_completion(prompt, model="llama3-70b-8192", completion_type="chat"):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    client = Groq(api_key=api_key)

    try:
        """
        Sends a request to the Groq API with the user's prompt.
        If the completion_type is "chat", it returns the response from the API.
        """
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )

        if completion_type == "chat":
            return chat_completion.choices[0].message.content
        else:
            print("Unsupported completion type:", completion_type)
            return None

    except Exception as e:
        print(f"Error with Groq: {e}")
        return None


async def enhance_prompt(user_prompt):
    """
    Enhance the initial user prompt with suggestions to guide the conversation.

    Args:
        user_prompt (str): The original user input prompt.

    Returns:
        str: The enhanced prompt with additional suggestions appended.

    """
    enhancement = (
        "As a helpful assistant, I aim to make our conversation engaging and informative. "
        "Here are a few things you might want to ask about:\n"
        "- Tell me a fun fact about the Roman Empire\n"
        "- Help me pick a gift for my dad who loves fishing\n"
        "- Write a Python script to automate sending email reports\n\n"
        "User Prompt: "
    )
    return enhancement + user_prompt


async def get_recommendations(user_prompt, model="llama3-70b-8192"):
    """
    Generate recommendations based on the enhanced user prompt and initial model response.

    Args:
        user_prompt (str): The original user input prompt.
        model (str, optional): The model identifier. Defaults to "llama3-70b-8192".

    Returns:
        str: Three concise recommendations as bullet points, based on the combined context of
             user input and model response.

    Raises:
        ValueError: If GROQ_API_KEY environment variable is not set.
    
    """
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    client = Groq(api_key=api_key)

    try:
        # Enhance the user prompt
        enhanced_prompt = await enhance_prompt(user_prompt)

        # Generate initial response from the model with enhanced prompt
        initial_response = await get_groq_completion(enhanced_prompt, model=model)

        # Construct recommendation prompt based on both user prompt and model response
        recommendation_prompt = (
            f"Based on the following conversation prompts and responses, please provide three concise recommendations as bullet points "
            f"without any explanations or additional text.\n\n"
            f"User Prompt:\n{user_prompt}\n\n"
            f"Model Response:\n{initial_response}\n\n"
            f"Recommendations:\n-"
        )

        # Generate recommendations based on the combined context
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": recommendation_prompt,
                }
            ],
            model=model,
        )

        return chat_completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error with Groq: {e}")
        return None