import requests
from util.api_loader import get_api_key

API_URL = "https://router.huggingface.co/models/distilgpt2"

def main():
    try:
        headers = {"Authorization": f"Bearer {get_api_key('HUGGINGFACE_API_KEY')}"}

        user_input = input("Enter your prompt: ")

        response = requests.post(API_URL, headers=headers, json={"inputs": user_input})

        print("\nResponse:\n", response.json())

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()