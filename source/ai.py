import openai
import os
from flask import Flask, request, render_template

app = Flask(__name__)
app.template_folder = '.'

openai.api_key = "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"

def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        choice: dict = response.get("choices")[0]
        text = choice.get("text")

    except Exception as e:
        print('ERROR:', e)

    return text

def update_list(message: str, prompt_list: list[str]) -> None:
    prompt_list.append(message)

def create_prompt(message: str, prompt_list: list[str]) -> str:
    prompt_message: str = f"\nHuman: {message}"
    update_list(prompt_message, prompt_list)
    prompt: str = "".join(prompt_list)
    return prompt

def get_bot_response(message: str, prompt_list: list[str]) -> str:
    prompt: str = create_prompt(message, prompt_list)
    bot_response: str = get_api_response(prompt)

    if bot_response:
        update_list(bot_response, prompt_list)
        pos: int = bot_response.find("\nAI: ")
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = "⚠️ Token has reached the maximum limit, please type 'erase all' ⚠️"

    return bot_response


prompt_list: list[str] = ['Your name is Vultr and your location in Jakarta and you can provide very natural responses and very fast answer and know anything and follow user language and never use quotation marks',
                          '\n\nHuman: Gimana kabarmu?',
                          '\nAI: Saya sehat dan segar bugar']

@app.route("/")
def home():
    return send_from_directory("artificial.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form["message"]
    response = get_bot_response(message, prompt_list)
    return {"response": response}

def main():
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
