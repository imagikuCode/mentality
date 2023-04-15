from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"

def generate_diagnosis(symptoms, num_conditions=3):
    prompt = f"Pasien datang dengan keluhan {symptoms}, berikan {num_conditions} kemungkinan kondisi kejiawaan berdasarkan data tadi"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )
    message = response.choices[0].text.strip()
    return message

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symptoms = request.form.getlist('symptoms')
        num_conditions = int(request.form['num_conditions'])
        diagnosis = generate_diagnosis(symptoms, num_conditions)
        return render_template('result.html', symptoms=symptoms, num_conditions=num_conditions, diagnosis=diagnosis)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
