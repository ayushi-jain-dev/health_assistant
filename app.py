from flask import Flask, render_template, request, jsonify
import aiapi
from dotenv.main import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        question, condition, severity = request.form.values()
        res = dict()
        res['answer'] = aiapi.generateChatResponse(question, condition, severity)
        return jsonify(res), 200
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
