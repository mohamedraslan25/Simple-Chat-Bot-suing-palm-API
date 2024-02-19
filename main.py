from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)
palm.configure(api_key="AIzaSyDiV_fvHcrlQZ1MswI0MjT9WRcSwGlhwNc")
defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 150
}
@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = palm.generate_text(**defaults, prompt=prompt)
        response_text = response.result
    return render_template('index.html', response_text=response_text)

if __name__ == '__main__':
    app.run(debug=True)