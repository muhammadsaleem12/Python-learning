# 🤖 Auto Reply Chatbot — WhatsApp

A Python automation project that reads a WhatsApp chat, detects when a specific person sends the latest message, generates a reply using **Google Gemini AI**, and automatically sends the response back through WhatsApp.

This project was built as a practical Python project to experiment with **automation, AI APIs, clipboard control, and GUI interaction**.

---

## ✨ How It Works

The basic flow is:

```text
WhatsApp
    ↓
Select & copy chat history
    ↓
Read clipboard
    ↓
Check the last sender
    ↓
Gemini generates a response
    ↓
Copy response
    ↓
Paste into WhatsApp
    ↓
Send message
```

The chatbot is currently configured to look for messages from:

```text
Chris
```

When the latest message is from that sender, the chat history is sent to Gemini, which generates a short response.

---

## 🛠️ Technologies Used

* 🐍 Python
* 🤖 Google Gemini API
* 🖱️ PyAutoGUI
* 📋 Pyperclip
* 🔐 python-dotenv
* ⏱️ Time

---

## 📁 Project Structure

```text
Auto-Reply-Chatbot/
│
├── main.py
├── gemini.py
├── get_cursor.py
├── .env
├── requirements.txt
└── README.md
```

### `main.py`

The main automation script.

It controls the mouse and keyboard, copies the WhatsApp chat history, checks the latest sender, asks Gemini for a response, and sends the generated reply.

### `gemini.py`

Handles communication with the Gemini API.

It contains the `ask_ai()` function, which sends the chat history to Gemini and returns the generated response.

### `get_cursor.py`

A small helper script used to find the screen coordinates required by PyAutoGUI.

Because the automation interacts with WhatsApp through mouse clicks and selections, the correct coordinates are important.

### `.env`

Stores the Gemini API key.

**This file should never be uploaded to GitHub.**

---

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

Install the required libraries:

```bash
pip install pyautogui pyperclip google-genai python-dotenv
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Use your own API key and never share it publicly.

Also add this to `.gitignore`:

```text
.env
env/
__pycache__/
```

---

## ▶️ Running the Bot

Make sure WhatsApp Web is open in Chrome and the required chat is visible.

Then run:

```bash
python main.py
```

The program will use PyAutoGUI to interact with the browser automatically.

---

## ⚠️ Important

This project currently depends on **fixed screen coordinates**.

For example, the program has coordinates for:

* Chrome
* The WhatsApp chat area
* Selecting chat history
* The message box

This means the automation may stop working if the browser window, screen resolution, scaling, or WhatsApp layout changes.

The `get_cursor.py` script can be used to find new coordinates.

**Use this project only with chats and accounts you are authorized to automate.**

---

## 🧠 What I Learned

This project gave me practical experience combining Python with external tools and APIs.

While building it, I worked with:

* Python modules
* Functions
* APIs
* Environment variables
* Clipboard automation
* GUI automation
* PyAutoGUI
* Gemini AI
* Working with multiple Python files
* Automating repetitive tasks

It was also a good example of how Python can interact with applications outside of Python itself.

---

## 🚧 Future Improvements

There are several things I would like to improve in the future:

* Replace fixed coordinates with more reliable element detection
* Improve sender detection
* Add better error handling
* Prevent duplicate replies
* Make the configuration easier
* Add more control over how Gemini responds
* Improve the overall reliability of the automation

**Built with Python 🐍**
