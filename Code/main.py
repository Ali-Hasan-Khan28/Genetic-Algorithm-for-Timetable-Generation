import pandas as pd
from genetic_algorithm import genetic_algorithm
from chabot import query_openai

course_metadata = pd.read_csv("csv_dataframe - Sheet1.csv")
result_chatbot = pd.DataFrame(columns=['time_slots',"unique_id"])

prompt = "Sdfs"
while True:
    prompt = input("Enter the promt::")
    if prompt  == "EXIT":
        break
    prompti = query_openai(prompt)
    new_row = {"time_slots":prompti[1],"unique_id":prompti[0]}
    result_chatbot.loc[len(result_chatbot)] = new_row

unique_ids_in_resultschatbot = result_chatbot["unique_id"].tolist()

columns = [f'lh{i}' for i in range(15)]
data = [[None for _ in range(15)] for _ in range(5)]
timetable = pd.DataFrame(data, columns=columns)

print(genetic_algorithm(course_metadata,result_chatbot,unique_ids_in_resultschatbot))

