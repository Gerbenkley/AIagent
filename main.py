import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv



def main():
    #INITIALIZE API KEY
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    #CHECK IF GIVEN A PROMPT
    if len(sys.argv) < 2:
        print("Error: no input is given")
        sys.exit(1)

    #USER PROMPT
    user_prompt = sys.argv[1]
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    
    #CHECK THIRD ARGUMENT

    #RESPONSE
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    #OUTPUT
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
