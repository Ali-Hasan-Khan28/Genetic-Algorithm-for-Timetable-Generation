# Schedbot

**Schedbot** is a timetable generator for university students that leverages **Genetic Algorithms** and **Simulated Annealing** to create optimized schedules in just minutes. Traditional fixed timetables cannot easily adapt to users' changing needs. Schedbot solves this problem by allowing users to generate personalized timetables on-demand for a year, month, or day based on their specific requirements.

The project is designed to work with a **chatbot interface**, where users can input data and communicate with the bot to generate the timetable. Alternatively, users without an API key can still generate timetables by clicking the **"Generate Timetable"** button.

---
## Video Demonstration

[![Watch the Video](data:image/jpeg;base64,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)](https://www.youtube.com/watch?v=JbKrwBhFxLc&pp=ygUPMzUgc2Vjb25kIHRpbWVy)

Click the thumbnail above to watch a demonstration of **Schedbot** in action.

---

## Features

- **Instant Timetable Generation**: Generate timetables for the entire academic year, month, or even just a day.
- **AI-Driven Chatbot**: Communicate with the chatbot to generate a personalized timetable based on input data.
- **Customizable**: Users can tweak the timetable as per their preferences.
- **Two Modes**:
  - **Chatbot Mode**: Interact with the chatbot and generate a timetable based on your inputs.
  - **Quick Mode**: Directly generate a timetable without a chatbot by clicking the "Generate Timetable" button (requires an API key).
- **Optimized Scheduling**: Utilizes **Genetic Algorithm** and **Simulated Annealing** techniques for optimal schedule creation.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask (Python web framework)  
- **API**: OpenAI API (for chatbot functionality)  
- **Programming Languages**: Python  
- **Algorithms**: Genetic Algorithm, Simulated Annealing  

---

## Installation

### Prerequisites

Ensure you have the following software installed on your machine:

- Python (version >= 3.7)  
- Flask  
- OpenAI API key  

### Steps to Install

1. Clone the repository:

    ```bash
    git clone https://github.com/username/Schedbot.git
    cd Schedbot
    ```

2. Set up a Python virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:

    - Create a `.env` file in the project root and add your OpenAI API key:

      ```bash
      nano .env
      ```

    - Add the following line, replacing `your-api-key-here` with your actual OpenAI API key:

      ```bash
      OPENAI_API_KEY="your-api-key-here"
      ```

5. Start the application:

    ```bash
    python3 app.py
    ```

    Your application should now be running locally on `http://localhost:5000`.

---

## Usage

### Chatbot Mode

1. Navigate to the application in your web browser.
2. Start a conversation with the chatbot by filling out the required details (e.g., courses, preferences, constraints).
3. The chatbot will generate a timetable based on your inputs using Genetic Algorithms and Simulated Annealing.
4. Review the generated timetable and make adjustments as needed.

### Quick Mode (Without API Key)

If you don’t have an OpenAI API key, you can still generate a timetable:

1. Go to the **"Generate Timetable"** section on the web page.
2. Click the button to generate the timetable for your selected day, month, or year.
3. Note that this will not include chatbot interaction, but the timetable will still be generated using the same underlying algorithms.

---

## Contributing

We welcome contributions! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:

    ```bash
    git checkout -b feature-branch
    ```

3. Make your changes and commit them:

    ```bash
    git commit -am 'Add new feature'
    ```

4. Push to your fork:

    ```bash
    git push origin feature-branch
    ```

5. Open a pull request on the main repository.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to **OpenAI** for providing the API that powers the chatbot.  
- Special thanks to the contributors who have helped improve the algorithms behind timetable generation.
