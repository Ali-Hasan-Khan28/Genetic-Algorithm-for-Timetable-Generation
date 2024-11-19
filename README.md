# Schedbot

**Schedbot** is a timetable generator for university students that leverages **Genetic Algorithms** and **Simulated Annealing** to create optimized schedules in just minutes. Traditional fixed timetables cannot easily adapt to users' changing needs. Schedbot solves this problem by allowing users to generate personalized timetables on-demand for a year, month, or day based on their specific requirements.

The project is designed to work with a **chatbot interface**, where users can input data and communicate with the bot to generate the timetable. Alternatively, users without an API key can still generate timetables by clicking the **"Generate Timetable"** button.

---
## Video Demonstration

[![Watch the Video](data:image/jpeg;base64,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)]([https://www.youtube.com/watch?v=VIDEO_ID](https://www.youtube.com/watch?v=BsFHELEgMy0))

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
