import openai
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a filename")
    openai.api_key = "" # Provide your openai API key
    try:
        with open(sys.argv[1], "r") as file:
            prompt = f"Please generate a README for the following code: {file.read()}, with a summary of the programme, its features, the requirements and also how to run it" 
    except FileNotFoundError:
        sys.exit("Could not read file (it may no exist, please check you typed the name correctly)")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    Read_me = response.choices[0].text
    with open("README.md", "w") as file:
        file.write(Read_me)

if __name__ == "__main__":
    main()