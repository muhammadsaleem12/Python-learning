# 🤖 Jarvis — Python Voice Assistant

Jarvis is a personal voice assistant built with **Python**. It listens for the wake word `"Jarvis"`, takes voice commands, performs different tasks, and uses Gemini AI when it doesn't recognize a built-in command.

## ✨ Features

* 🎙️ Voice recognition
* 🔊 Text-to-speech responses
* 🌐 Open websites using voice commands
* 🎵 Play music from a custom music library
* 📰 Get and read the latest news
* 🤖 Gemini AI integration
* 🔐 Secure API key handling with `.env`

## 🛠️ Built With

* Python
* SpeechRecognition
* pyttsx3
* Google Gemini API
* NewsAPI
* Requests
* python-dotenv

## 📁 Project Structure

```text
Jarvis/
│
├── main.py
├── client.py
├── musicLibrary.py
├── .env
├── .gitignore
└── README.md
```

`main.py` contains the main assistant and command processing.

`client.py` handles communication with Gemini AI.

`musicLibrary.py` contains the music links used by the assistant.

`.env` stores the API keys and should **never be uploaded to GitHub**.

## 🚀 Setup

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Create a virtual environment:

```bash
python -m venv env
env\Scripts\activate
```

Install the required packages:

```bash
pip install SpeechRecognition pyttsx3 python-dotenv requests google-genai
```

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_news_api_key
```

Use **your own API keys**. Never share or commit them.

Also make sure `.gitignore` contains:

```text
.env
env/
__pycache__/
```

## ▶️ Run Jarvis

```bash
python main.py
```

Once Jarvis starts, say:

```text
Jarvis
```

and then give it a command such as:

```text
Open Google
Play Starboy
What's the news?
Explain Python functions
```

## 📚 What I Learned

This was one of my first larger Python projects. It helped me bring together many of the concepts I had learned so far, including functions, loops, dictionaries, modules, APIs, exception handling, environment variables, and external Python libraries.

It also gave me practical experience working with **voice recognition, text-to-speech, web automation, and AI APIs**.

The project is still a work in progress, and I plan to improve it as I continue learning Python.

**Built with Python 🐍**
