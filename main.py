import fasttext
from flask import Flask, request, jsonify
import re

app = Flask(__name__)
class Handler:
    model = None
    tokenizer = None
handle = Handler()

@app.route('/language/api', methods=['GET', 'POST'])
def add_message():
    content = request.json
    code = content['Comment']
    code = re.sub(r'[^\w]', ' ', code)
    code = code.rstrip()
    code = code.replace("/", "")
    data = {}
    data['Language'] = "None"
    data['Probability'] = 0.0
    try:
        if len(code)>0:
            language = handle.model.predict(code)
            if language!=None and len(language[0])>0:
                languageResult = language[0][0].replace('__label__', '')
                print(language)
                print(language)
                data['Language'] = languageResult
                data['Probability'] = language[1][0]
    except:
        data['Language'] = "None"
        data['Probability'] = 0.0
    return jsonify(data)

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

def main():
    model = fasttext.load_model("lid.176.bin")
    handle.model = model
    app.run(host='0.0.0.0', debug=True, port=5500)
    pass

if __name__ == '__main__':
    main()
