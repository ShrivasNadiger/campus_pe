import requests

def main():
    try:
        user_input = input("Enter your prompt: ")

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": user_input,
                "stream": False
            }
        )

        print("\nResponse:\n", response.json()["response"])

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()