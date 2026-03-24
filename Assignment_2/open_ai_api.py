from openai import OpenAI
from util.api_loader import get_api_key

def main():
    try:
        client = OpenAI(api_key=get_api_key("OPENAI_API_KEY"))

        user_input = input("Enter your prompt: ")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}]
        )

        print("\nResponse:\n", response.choices[0].message.content)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
