import cohere
from util.api_loader import get_api_key

def main():
    try:
        co = cohere.Client(get_api_key("COHERE_API_KEY"))

        user_input = input("Enter your prompt: ")

        response = co.generate(
            model="command",
            prompt=user_input,
            max_tokens=100
        )

        print("\nResponse:\n", response.generations[0].text)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()