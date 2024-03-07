from flask import Flask, render_template, request, jsonify
from service_url import service_data


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggestions')
def get_suggestions():
    query = request.args.get('q', '').lower()
    suggestions = [{'tag': tag, 'url': url} for tag, url in service_data.items() if query in tag.lower() or query in url.lower()]

    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)
