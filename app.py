import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def classify_email(email):
    prompt = f"""
    Classify this customer email into one category:
    - Refund Request
    - Technical Bug
    - Sales Inquiry
    - Account Issue
    - General Question

    Email:
    {email}

    Return only the category name.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def generate_reply(email, category):

    prompt = f"""
    You are a customer support assistant.

    Category:
    {category}

    Customer email:
    {email}

    Write a professional customer support reply.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def main():

    email = input("Enter customer email:\n")

    category = classify_email(email)

    reply = generate_reply(
        email,
        category
    )

    print("\n--- Ticket Category ---")
    print(category)

    print("\n--- AI Response Draft ---")
    print(reply)


if __name__ == "__main__":
    main()