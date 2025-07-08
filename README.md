# AI-Powered Chatbot with Gemini API (Python)
This project demonstrates a Python-based chatbot that leverages the Google Gemini API to provide intelligent and engaging conversations.

## Overview
1) This chatbot is designed to interact with users through natural language, providing informative, creative, and helpful responses. 
2) It utilizes the power of the Gemini API to understand user input, generate relevant replies, and maintain context throughout the conversation.
3) This project serves as a starting point for building more complex and customized chatbots.  
4) It's a great way to learn about:
  A)  Integrating with the Gemini API in Python.
  B)  Handling user input and generating responses.

## Features
1)  Gemini API Integration:   Leverages the Gemini API for natural language understanding and generation.
2)  Command-Line Interface (CLI):    Interactive chatbot accessible through the terminal.

## Prerequisites

1) Python 3.7+:   Ensure you have Python 3.7 or a later version installed. You can download it from [python.org](https://www.python.org/downloads/).
2) Google Gemini API Key:   You need a Google Gemini API key. You can obtain one by signing up for the Google AI Studio: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
3) pip:   Python package installer.  Most Python installations come with pip pre-installed.

## Installation

1.    Clone the repository:

  ```bash
  git clone https://github.com/[your-github-username]/[your-repo-name].git
   cd [your-repo-name]
    ```

2.    Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.    Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```
    google-generativeai
    ```

## Usage

1.    Set your Gemini API key:    You need to set your API key as an environment variable or directly in the script (not recommended for security reasons).

      Option 1: Environment Variable (Recommended)

    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY"  # Linux/macOS
    set GOOGLE_API_KEY="YOUR_API_KEY"     # Windows
    ```

      Option 2:  Directly in the script (Not Recommended)

    ```python
    # In chatbot.py (or your main script)
    api_key = "YOUR_API_KEY"
    ```

      IMPORTANT:   Never commit your API key directly to the repository. Use environment variables whenever possible.

2.    Run the chatbot:

    ```bash
    python chatbot.py
    ```

    The chatbot will start in the terminal and prompt you to enter your messages.

## Configuration

      `GOOGLE_API_KEY` environment variable:    Used to store your Gemini API key.  Highly recommended for security.
      `chatbot.py` (or your main script):
        You can adjust the `model` used by the Gemini API (e.g., `'gemini-1.5-pro-latest'` or `'gemini-1.0-pro'`).
        You can modify the `generation_config` and `safety_settings`  passed to the Gemini API to fine-tune the chatbot's behavior and response style.  See the Gemini API documentation for more details.

## Example Conversations

```
User: Hello, can you tell me about the solar system?

Chatbot: The Solar System is a gravitationally bound system consisting of the Sun and the objects that orbit it, either directly or indirectly. Of the objects that orbit the Sun directly, the largest are the eight planets, with the remainder being smaller objects, such as dwarf planets and small Solar System bodies.

User: What's the capital of France?

Chatbot: The capital of France is Paris.

User:  Write a short poem about a cat.

Chatbot: A shadow sleek, a furry friend,
With eyes of emerald, stories penned.
A purring rumble, soft and low,
A feline grace, where mysteries grow.
```

## Contributing

We welcome contributions to this project! If you have any suggestions, bug reports, or improvements, please feel free to submit a pull request.   

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your branch to your forked repository.
5.  Submit a pull request.

## Credits

    This project utilizes the Google Gemini API, a powerful tool for natural language processing and generation.
    Thanks to the Google AI team for making this API available.
    I want to thank speech_recognition for enabling voice to text , voice to voice conversation.
    I want to thanks pygame for supporting voice based conversation.
    I want to thanks gtts for supporting text to speech conversation
    I want to thanks io for supporting voice conversation.

Created with ❤️ by Aditya Upadhyay
