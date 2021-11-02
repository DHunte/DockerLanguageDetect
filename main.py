from flask import Flask, request, jsonify
import re
app = Flask(__name__)
from langid.langid import LanguageIdentifier, model

@app.route('/api', methods=['GET', 'POST'])
def add_message():
    content = request.json
    code = content['Comment']
    code = re.sub(r'[^\w]', ' ', code)
    code = code.rstrip()
    code = code.replace("/", "")
    data = {}
    data['Language'] = "eng"
    data['Probability'] = 1.0
    if len(code)>0:
        identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
        classify = identifier.classify(code)
        data['Language'] = classify[0]
        data['Probability'] = classify[1]
    return jsonify(data)

def main():
    app.run(host='0.0.0.0', debug=True, port=5500)
    pass

if __name__ == '__main__':
    main()
