# README
This program is used to generate a 'README.md' document which summarises a given code snippet. In order to use this programme you must have an OpenAI API key, which must be specified when using the `openai.api_key` parameter.

## Requirements
* The OpenAI API key
* The filename of the code snippet you would like to summarise

## Features
* A 1000-token long summary of the selected code snippet
* Written in Markdown format

## Usage
* Clone this repo
* Run the command `pip3 install -r requirements.txt`
To run the programme, enter the following command in the command prompt/terminal:
```
python3 main.py <filename>
```
Replace `<filename>` with the filename of the code snippet you would like to summarise (with the path to it from the current directory indicated as well).