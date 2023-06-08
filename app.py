from flask import Flask, render_template, request, jsonify
import aiapi
from dotenv.main import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['prompt']
        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt)
        return jsonify(res), 200
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
