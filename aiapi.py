import os
import openai

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY


def generateChatResponse(_question, condition, severity):
    messages = []
    messages.append({"role": "assistant", "content": "You are a helpful health assistant"})

    question = {}
    question['role'] = 'user'
    question[
        'content'] = f"I am suffering with {severity} {condition} condition. Please answer my question on the given " \
                     f"condition and severity. {_question}"
    messages.append(question)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    try:
        answer = response.choices[0].message
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists, come back later'

    return answer
