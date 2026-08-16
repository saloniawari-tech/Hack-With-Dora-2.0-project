import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Check your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)


def test_ai():
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=(
            "You are Renter Shield, an AI assistant that helps "
            "tenants understand rental agreements. "
            "Say hello to the Renter Shield team in one friendly sentence."
        )
    )

    print("\n====================================")
    print("       RENTER SHIELD AI TEST")
    print("====================================")

    print("\nAI Response:")
    print(response.text)


if __name__ == "__main__":
    test_ai()