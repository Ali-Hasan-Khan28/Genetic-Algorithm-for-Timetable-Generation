# Schedbot

**Schedbot** is a timetable generator for university students that leverages **Genetic Algorithms** and **Simulated Annealing** to create optimized schedules in just minutes. Traditional fixed timetables cannot easily adapt to users' changing needs. Schedbot solves this problem by allowing users to generate personalized timetables on-demand for a year, month, or day based on their specific requirements.

The project is designed to work with a **chatbot interface**, where users can input data and communicate with the bot to generate the timetable. Alternatively, users without an API key can still generate timetables by clicking the **"Generate Timetable"** button.

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
    flask run
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
