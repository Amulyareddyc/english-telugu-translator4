from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
translator = Translator()

@app.route('/')
def home():
    return "English to Telugu Translator is Running!"

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text', '')
    dest = 'te'
    translated = translator.translate(text, dest=dest)
    return jsonify({'translated_text': translated.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
