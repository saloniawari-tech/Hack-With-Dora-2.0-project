from google import genai
from dotenv import load_dotenv
import os

from utils.text_loader import load_lease


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_lease(question, lease_text):

    prompt = f"""

You are Renter Shield AI Assistant.

Answer the user's question using ONLY the rental agreement provided.

Rules:
- Do not make assumptions.
- If information is not present, say:
  "This information is not mentioned in the agreement."
- Explain in simple language.
- Mention the relevant clause if possible.


Rental Agreement:

{lease_text}


User Question:

{question}

"""


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )


    return response.text



if __name__ == "__main__":

    lease = load_lease()

    question = input(
        "\nAsk something about your lease: "
    )


    answer = ask_lease(
        question,
        lease
    )


    print("\n==============================")
    print("RENTER SHIELD AI ASSISTANT")
    print("==============================\n")

    print(answer)