from groq import Groq
from util.api_loader import get_api_key

def main():
    try:
        client = Groq(api_key=get_api_key("GROQ_API_KEY"))

        user_input = input("Enter your prompt: ")

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}]
        )

        print("\nResponse:\n", response.choices[0].message.content)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()