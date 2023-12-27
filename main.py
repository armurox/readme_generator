import openai
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a filename")
        # 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
        # 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
    openai.api_key = "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" # Provide your openai API key
    try:
        with open(sys.argv[1], "r") as file:
            prompt = f"Please generate a README for the following code: {file.read()}" 
    except FileNotFoundError:
        sys.exit("Could not read file (it may not exist, please check you typed the name correctly)")
    response = openai.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    Read_me = response.choices[0].text
    with open("README.md", "w") as file:
        file.write(Read_me)

if __name__ == "__main__":
    main()