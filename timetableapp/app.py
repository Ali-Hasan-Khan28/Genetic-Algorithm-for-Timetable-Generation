# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import pandas as pd
# from genetic_algorithm import genetic_algorithm
# from chatbot import query_openai

# app = Flask(__name__)

# # Global variable to store uploaded course metadata
# course_metadata = None
# result_chatbot = pd.DataFrame(columns=['time_slots', "unique_id"])


# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             global course_metadata
#             course_metadata = pd.read_csv(file)
#             return redirect(url_for('chatbot'))
#     return render_template('upload.html')


# @app.route('/chatbot', methods=['GET', 'POST'])
# def chatbot():
#     global result_chatbot
#     if request.method == 'POST':
#         prompt = request.form['prompt']
#         if prompt.lower() == "exit":
#             return redirect(url_for('generate_timetable'))
#         # Generate chatbot response
#         prompt_result = query_openai(prompt)
#         new_row = {"time_slots": prompt_result[1], "unique_id": prompt_result[0]}
#         result_chatbot.loc[len(result_chatbot)] = new_row
#         return render_template('chatbot.html', result=result_chatbot.to_dict(orient='records'))
#     return render_template('chatbot.html', result=[])


# # @app.route('/generate_timetable', methods=['GET','POST'])
# # def generate_timetable():
# #     unique_ids = result_chatbot["unique_id"].tolist()
# #     timetable = genetic_algorithm(course_metadata, result_chatbot, unique_ids)
# #     return render_template('timetable.html', timetable=timetable.to_html(classes='timetable'))


# @app.route('/generate_timetable', methods=['GET', 'POST'])
# def generate_timetable():
#     unique_ids = result_chatbot["unique_id"].tolist()
#     timetable = genetic_algorithm(course_metadata, result_chatbot, unique_ids)
#     lecture_halls = [f'LH{i}' for i in range(1, 16)]  # List of lecture halls LH1 to LH15
#     selected_hall = None  # Default to no selection
    
#     if request.method == 'POST':
#         selected_hall = request.form.get('lecture_hall')  # Get selected lecture hall from form
        
#         if selected_hall:
#             # Extract timetable data for the selected hall
#             new_timetable = timetable[selected_hall]
#             new_df = pd.DataFrame(columns=["8:00am to 8:50am","9:00am to 9:50am","10:00am to 10:50am","10:50am to 11:40am","11:40am to 12:30pm","2:30pm to 3:20pm","3:30pm to 4:20pm","4:30pm to 5:20pm"])
#             for i in range(0,5):
#                 course_unique_id_list = new_timetable.iloc[i]
#                 new_row = {"8:00am to 8:50am":course_unique_id_list[0] ,"9:00am to 9:50am":course_unique_id_list[1] ,"10:00am to 10:50am":course_unique_id_list[2] ,"10:50am to 11:40am":course_unique_id_list[3] ,"11:40am to 12:30pm":course_unique_id_list[4] ,"2:30pm to 3:20pm":course_unique_id_list[5] ,"3:30pm to 4:20pm":course_unique_id_list[6] ,"4:30pm to 5:20pm":course_unique_id_list[7] }
#                 new_df = new_df._append(new_row, ignore_index=True)

#             # hall_index = lecture_halls.index(selected_hall)  # Find column index for the selected hall
#             # filtered_timetable = timetable[[selected_hall]].copy()  # Filter timetable DataFrame for the hall

#             # # Rename the column to 'Time' to display timetable in HTML
#             # filtered_timetable.columns = ['Time']

#             return render_template('timetable.html', lecture_halls=lecture_halls, selected_hall=selected_hall, timetable=new_df.to_html(classes='timetable'))

#     # Display selection form if no POST data is present
#     return render_template('timetable.html', lecture_halls=lecture_halls, selected_hall=selected_hall, timetable=None)


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from genetic_algorithm import genetic_algorithm
from chatbot import query_openai

app = Flask(__name__)

# Global variables to store uploaded course metadata and generated timetable
course_metadata = None
result_chatbot = pd.DataFrame(columns=['time_slots', "unique_id"])
timetable_data = None  # To store the generated timetable once


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
        print("SDssdddddd")
        prompt = request.form['prompt']
        if prompt.lower() == "exit":
            return redirect(url_for('generate_timetable'))
        print("aaaaaaaaaaa")
        # Generate chatbot response
        prompt_result = query_openai(prompt)
        new_row = {"time_slots": prompt_result[1], "unique_id": prompt_result[0]}
        result_chatbot.loc[len(result_chatbot)] = new_row
        print(result_chatbot)
        return render_template('chatbot.html', result=result_chatbot.to_dict(orient='records'))
    return render_template('chatbot.html', result=[])


def generate_timetable_data():
    """Generate the timetable once and store it globally."""
    global timetable_data
    if timetable_data is None and course_metadata is not None:
        unique_ids = result_chatbot["unique_id"].tolist()
        timetable_data = genetic_algorithm(course_metadata, result_chatbot, unique_ids)
    return timetable_data


@app.route('/generate_timetable', methods=['GET', 'POST'])
def generate_timetable():
    global timetable_data
    timetable_data = generate_timetable_data()  # Ensure timetable is generated only once
    lecture_halls = [f'LH{i}' for i in range(0, 2)]
    selected_hall = None  # Default to no selection
    
    if request.method == 'POST':
        print("sdsd",timetable_data)
        selected_hall = request.form.get('lecture_hall')
        
        if selected_hall and timetable_data is not None:
            new_timetable = timetable_data[selected_hall]  # Extract timetable for the selected hall
            
            # Create a new DataFrame for the selected hall
            new_df = pd.DataFrame(columns=["8:00am to 8:50am", "9:00am to 9:50am", "10:00am to 10:50am",
                                           "10:50am to 11:40am", "11:40am to 12:30pm", "2:30pm to 3:20pm",
                                           "3:30pm to 4:20pm", "4:30pm to 5:20pm"])
            for i in range(5):
                course_unique_id_list = new_timetable.iloc[i]
                new_row = {
                    "8:00am to 8:50am": course_unique_id_list[0],
                    "9:00am to 9:50am": course_unique_id_list[1],
                    "10:00am to 10:50am": course_unique_id_list[2],
                    "10:50am to 11:40am": course_unique_id_list[3],
                    "11:40am to 12:30pm": course_unique_id_list[4],
                    "2:30pm to 3:20pm": course_unique_id_list[5],
                    "3:30pm to 4:20pm": course_unique_id_list[6],
                    "4:30pm to 5:20pm": course_unique_id_list[7]
                }
                new_df = new_df._append(new_row, ignore_index=True)

            return render_template('timetable.html', lecture_halls=lecture_halls, selected_hall=selected_hall,
                                   timetable=new_df.to_html(classes='timetable'))

    return render_template('timetable.html', lecture_halls=lecture_halls, selected_hall=selected_hall, timetable=None)


if __name__ == '__main__':
    app.run(debug=True)
