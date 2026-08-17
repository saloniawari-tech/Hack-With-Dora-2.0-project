from google import genai
from dotenv import load_dotenv
import os
import json

from utils.pdf_loader import extract_pdf_text

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_lease(text):

    prompt = f"""
You are Renter Shield AI, a rental agreement risk analyzer.

Analyze the following rental agreement and return ONLY valid JSON.

Do not write any text outside JSON.

Use this exact structure:

{{
    "overall_score": 0,
    "overall_risk": "LOW",
    "summary": "",
    "issues": [
        {{
            "clause_number": "",
            "category": "",
            "risk_level": "LOW",
            "title": "",
            "clause_text": "",
            "explanation": "",
            "recommendation": ""
        }}
    ]
}}

Analyze these categories:

- Security deposit
- Notice period
- Lock-in period
- Maintenance responsibilities
- Hidden charges
- Penalties
- Rent increase
- Utility responsibilities

Rules:
1. Only analyze clauses present in the agreement.
2. Do not create imaginary clauses.
3. Explain risks in simple language.
4. Give practical recommendations.
5. Risk level should only be LOW, MEDIUM, or HIGH.

Rental Agreement:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    return response.text


if __name__ == "__main__":

    lease = extract_pdf_text(
    "ai/sample_data/lease.pdf"
)

    result = analyze_lease(lease)

    print("==============================")
    print("     RENTER SHIELD REPORT")
    print("==============================")

   # Save AI result as JSON file

output_path = "ai/output/risk_report.json"

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(
        json.loads(result),
        file,
        indent=4,
        ensure_ascii=False
    )

print("\nReport saved successfully!")
print(output_path)