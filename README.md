# Jarvis-PersonalVoice-AutomatedLaptopAlAssistant_Python-GoogleGeminiAPI-SpeechRecognition_project
A Python-based voice-controlled desktop assistant that listens for the wake word **"Jarvis"** and performs various laptop automation tasks through voice commands. It integrates **Google Gemini AI** to provide intelligent responses while also automating common desktop operations such as launching applications, searching YouTube, checking system status, taking screenshots, and opening websites.

# 📌 Project Overview
Jarvis is an AI-powered personal desktop assistant developed using Python. It combines **Speech Recognition**, **Text-to-Speech**, **Google Gemini API**, and desktop automation libraries to create a hands-free interaction experience. After hearing the wake word "Jarvis", the assistant listens to the user's command, processes it, performs the requested action, and responds with voice feedback.

# 📖 Description
The purpose of this project is to simplify daily computer usage using voice commands. Instead of manually opening applications or browsing the internet, users can simply speak commands to Jarvis.
The assistant supports both predefined automation commands and AI-generated conversations. For known commands, it performs desktop operations such as opening applications, reporting system information, taking screenshots, or searching YouTube. For general questions, it uses the **Google Gemini API** to generate intelligent responses.
This project demonstrates the practical integration of Artificial Intelligence, Natural Language Processing (NLP), Speech Recognition, and Desktop Automation in a single application.

# 🎯 Objectives
- Develop a voice-controlled desktop assistant.
- Enable hands-free interaction with the computer.
- Automate frequently used laptop operations.
- Integrate Google Gemini AI for intelligent conversations.
- Improve productivity through voice automation.
- Demonstrate the integration of AI and desktop automation using Python.

# ✨ Key Features
### 🎙️ Wake Word Detection
The assistant remains in standby mode and activates only after detecting the wake word **"Jarvis"**.
### 🗣️ Voice Recognition
Converts spoken commands into text using Google's Speech Recognition service.
### 🤖 AI-Powered Conversations
Uses Google Gemini API to answer general questions intelligently.
### 🔊 Voice Responses
Replies to the user using Text-to-Speech technology.
### 💻 Desktop Automation
Launches installed desktop applications such as:
- Google Chrome
- Spotify
- WhatsApp
- Calculator
### 📺 Smart YouTube Search
Searches and plays videos directly on YouTube using voice commands.
### ⚡ System Monitoring
Reports:
- RAM Usage
- Battery Percentage
### 🕒 Time Assistant
Speaks the current system time.
### 📸 Screenshot Capture
Captures screenshots using a voice command.
### 🌐 Website Automation
Opens websites automatically when requested.
### 🔒 Desktop Shortcut
Minimizes desktop windows and opens GeeksforGeeks for quick access.
### 😊 Interactive Assistant
Provides natural, friendly AI-generated responses for everyday conversations.
# 🛠️ Tech Stack
| Category | Technology |
|----------|------------|
| Programming Language | Python 3.x |
| AI Model | Google Gemini API |
| Speech Recognition | SpeechRecognition |
| Text-to-Speech | pyttsx3 |
| Audio Recording | sounddevice |
| Audio Processing | scipy |
| Desktop Automation | pyautogui |
| System Monitoring | psutil |
| Web Automation | webbrowser |
| YouTube Search | pywhatkit |
| Numerical Processing | NumPy |

# 📂 Project Structure
Jarvis/
│
├── Jarvis.py                 # Main application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
│
├── assets/
│   ├── architecture.png
│   ├── demo.gif
    └── screenshots/


# ⚙️ Installation
### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Jarvis.git
```
### Step 2: Move into the Project Folder
```bash
cd Jarvis
```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
# 🔑 Configuration
### Create a Google Gemini API Key
Visit Google AI Studio and generate your API key.
Replace the API key in the project with your own key.
Example:
python
genai.configure(api_key="YOUR_API_KEY")
Save the file after updating the API key.

# ▶️ Usage
Run the assistant using:
```bash
python Jarvis.py
```
Wait for the assistant to listen.
Say:
**Jarvis**
Then give a command.
Example commands:
- Open Chrome
- Open Spotify
- Open WhatsApp
- Open Calculator
- Play Believer on YouTube
- What's the time?
- System status
- Take a screenshot
- Open Google
- Goodbye
- Turn off
For any other question, Jarvis will generate an AI response using Google Gemini.

# 🏗️ System Workflow

                User Voice
                     │
                     ▼
          Wake Word Detection
                     │
                     ▼
          Speech Recognition
                     │
                     ▼
          Command Processing
                     │
     ┌───────────────┼───────────────┐
     │               │               │
     ▼               ▼               ▼
Desktop        YouTube Search    Gemini AI
Automation                        Response
     │               │               │
     └───────────────┼───────────────┘
                     ▼
          Text-to-Speech Output

# 🚀 Future Enhancements

- Weather Information
- News Updates
- Email Automation
- Calendar Integration
- Task Reminder System
- File Search
- Voice Authentication
- Multi-language Support
- Offline Speech Recognition
- Smart Home Integration
- Chat History
- Voice Customization

# 📚 Libraries Used
- numpy
- scipy
- sounddevice
- SpeechRecognition
- pyttsx3
- google-generativeai
- pyautogui
- psutil
- webbrowser
- pywhatkit
- subprocess
- datetime
- os



<img width="2048" height="692" alt="image" src="https://github.com/user-attachments/assets/058bd942-b56c-4483-8157-855b4ab06cee" />
<img width="2816" height="1536" alt="image" src="https://github.com/user-attachments/assets/eb36315e-35d1-4792-95c5-63a8b310f176" />
<img width="626" height="482" alt="WhatsApp Image 2026-08-07 at 4 52 44 AM" src="https://github.com/user-attachments/assets/ae633d08-68d2-4092-b74f-e3ad846e9604" />

