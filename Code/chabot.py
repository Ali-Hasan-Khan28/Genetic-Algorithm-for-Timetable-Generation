# unique_ids_in_resultschatbot = ['Mr. Sajid Ali', 'Dr Salman Ahmed', 'CS112']
 

import pandas as pd
from openai import OpenAI
import re
import os



# df = course_metadata

def query_openai(prompt):
    client = OpenAI(
  api_key="",  # this is also the default, it can be omitted
)

    context = """
                      You are helpful assistant that will help me in finding the name of course or name teacher mentioned inside the prompt.
                      The output should be just the name of teacher or course.
              """

    context2 = """
                    You are a helpful assistant. Provide only the one line of Python code necessary to complete the query.

                    Instructions:
                    1. If a time is mentioned in the prompt, store the corresponding INDEX values based on the following schedule in a list.:

                    - Morning (8:00 AM to 12:30 PM):
                        - [0: 8:00 - 8:50]
                        - [1: 8:50 - 9:50]
                        - [2: 9:50 - 10:40]
                        - [3: 10:40 - 11:30]
                        - [4: 11:30 - 12:30]

                    - Evening (2:30 PM to 5:30 PM):
                        - [5: 2:30 - 3:30]
                        - [6: 3:30 - 4:30]
                        - [7: 4:30 - 5:30]

                    2. If the user refers to a specific time range (e.g., "after 2:30 PM"), interpret the range and store the corresponding values in list based on the above schedule.
                    The ouput should be a list. Not anything other than that.
               """

    # Send prompt to OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    response2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context2},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )


    # Extract response text
    reply = response.choices[0].message.content
    reply2 = response2.choices[0].message.content
    return reply, reply2

results_chatbot = pd.DataFrame(columns=['time_slots',"unique_id"])