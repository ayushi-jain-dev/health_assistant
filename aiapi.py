import os
import openai

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "assistant", "content": "You are a helpful health assistant"})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    try:
        answer = response.choices[0].message
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists, come back later'
    return answer
