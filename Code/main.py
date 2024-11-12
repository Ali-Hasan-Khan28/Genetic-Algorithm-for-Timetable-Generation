import pandas as pd
from chabot import unique_ids_in_resultschatbot
from genetic_algorithm import genetic_algorithm

input_data = pd.read_csv("csv_dataframe - Sheet1.csv")
result_chabot = pd.read_csv("results_chatbot.csv")

columns = [f'lh{i}' for i in range(15)]
data = [[None for _ in range(15)] for _ in range(5)]
timetable = pd.DataFrame(data, columns=columns)

genetic_algorithm(input_data,result_chabot,unique_ids_in_resultschatbot)

