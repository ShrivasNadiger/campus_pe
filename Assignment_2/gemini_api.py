import google.generativeai as genai
from util.api_loader import get_api_key

def main():
    try:
        genai.configure(api_key=get_api_key("GEMINI_API_KEY"))

        model = genai.GenerativeModel("gemini-1.5-flash")

        user_input = input("Enter your prompt: ")

        response = model.generate_content(user_input)

        print("\nResponse:\n", response.text)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()