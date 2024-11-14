from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
from genetic_algorithm import genetic_algorithm
from chatbot import query_openai

app = Flask(__name__)

# Global variable to store uploaded course metadata
course_metadata = None
result_chatbot = pd.DataFrame(columns=['time_slots', "unique_id"])


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            global course_metadata
            course_metadata = pd.read_csv(file)
            return redirect(url_for('chatbot'))
    return render_template('upload.html')


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    global result_chatbot
    if request.method == 'POST':
        prompt = request.form['prompt']
        if prompt.lower() == "exit":
            return redirect(url_for('generate_timetable'))
        # Generate chatbot response
        prompt_result = query_openai(prompt)
        new_row = {"time_slots": prompt_result[1], "unique_id": prompt_result[0]}
        result_chatbot.loc[len(result_chatbot)] = new_row
        return render_template('chatbot.html', result=result_chatbot.to_dict(orient='records'))
    return render_template('chatbot.html', result=[])


@app.route('/generate_timetable', methods=['GET'])
def generate_timetable():
    unique_ids = result_chatbot["unique_id"].tolist()
    timetable = genetic_algorithm(course_metadata, result_chatbot, unique_ids)
    return render_template('timetable.html', timetable=timetable.to_html(classes='timetable'))


if __name__ == '__main__':
    app.run(debug=True)
