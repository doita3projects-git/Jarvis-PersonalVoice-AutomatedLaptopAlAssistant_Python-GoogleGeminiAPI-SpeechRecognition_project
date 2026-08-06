import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
import numpy as np
import os
import subprocess  # For the "Modern" app launching
import pyautogui
import psutil
import webbrowser
import pywhatkit  # For the smart YouTube search
import google.generativeai as genai
from datetime import datetime

# --- 1. THE BRAIN CONFIGURATION (Self-Healing) ---
genai.configure(api_key="AIzaSyC7jIsQNBUevm43DvfmD5Ie1mn4KyxLEvo")

try:
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    best_model = next((m for m in available_models if '1.5-flash' in m), available_models[0])
    model = genai.GenerativeModel(best_model)
    print(f"SUCCESS: Jarvis is using the {best_model} brain.")
except Exception as e:
    model = genai.GenerativeModel('gemini-1.5-flash')


def ask_brain(question):
    try:
        prompt = f"You are Jarvis, a super friendly, cheerful assistant. Keep it under 2 sentences. Question: {question}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "I'm having trouble reaching my neural network, boss."


# --- 2. THE MOUTH ---
def speak(text):
    print(f"Jarvis: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# --- 3. THE EARS ---
def listen_for_wake():
    """Short listener specifically for the name 'Jarvis'"""
    fs = 44100
    seconds = 3  # Shorter time for faster response
    filename = 'wake_detect.wav'
    print(".", end="", flush=True)  # Small dots to show he is listening
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, myrecording)

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)
            query = recognizer.recognize_google(audio_data)
            return query.lower()
    except Exception:
        return "none"


def listen():
    """Full listener for commands"""
    fs = 44100
    seconds = 5
    filename = 'output.wav'
    print(f"\nListening for command ({seconds}s)...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, myrecording)

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.0
    try:
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)
            query = recognizer.recognize_google(audio_data)
            print(f"DEBUG: Jarvis heard: '{query}'")
            return query.lower()
    except Exception:
        return "none"


# --- 4. THE COMMAND CENTER ---
if __name__ == "__main__":
    print("Systems Online. Waiting for you to call 'Jarvis'...")

    while True:
        # Step 1: Only wake up if his name is heard
        wake_query = listen_for_wake()

        if "jarvis" in wake_query:
            speak("Yes, boss? I'm listening.")

            # Step 2: Now listen for the actual command
            query = listen()

            # --- PRIORITY 1: APP LAUNCHER ---
            if "open" in query or "launch" in query:
                if "whatsapp" in query:
                    speak("Opening WhatsApp now.")
                    subprocess.Popen(["start", "whatsapp:"], shell=True)

                elif "spotify" in query:
                    speak("Launching Spotify. Enjoy your music!")
                    subprocess.Popen(["start", "spotify:"], shell=True)

                elif "chrome" in query or "google" in query:
                    speak("Opening Google Chrome.")
                    subprocess.Popen(["start", "chrome"], shell=True)

                elif "calculator" in query:
                    speak("Opening Calculator.")
                    subprocess.Popen(["start", "calculator:"], shell=True)

            # --- PRIORITY 2: YOUTUBE SEARCH ---
            elif "play" in query and "on youtube" in query:
                search_term = query.replace("play", "").replace("on youtube", "").strip()
                speak(f"Finding {search_term} on YouTube.")
                pywhatkit.playonyt(search_term)

            # --- PRIORITY 3: SYSTEM COMMANDS ---
            elif "status" in query or "report" in query:
                ram = psutil.virtual_memory().percent
                battery = psutil.sensors_battery()
                status_msg = f"Of course! Your RAM is at {ram} percent."
                if battery:
                    status_msg += f" And your battery is at {battery.percent} percent. Everything looks great!"
                speak(status_msg)

            elif "time" in query:
                now = datetime.now().strftime("%I:%M %p")
                speak(f"It is currently {now}.")

            elif "shot" in query or "snap" in query:
                speak("Snapping the screen.")
                try:
                    pyautogui.hotkey('win', 'prtscr')
                    speak("Screenshot saved to your Pictures folder, boss.")
                except:
                    speak("My camera module is having trouble with this version of Python.")

            elif "lockdown" in query or "hide" in query:
                speak("No problem at all! Hiding your windows and pulling up Geeks for Geeks for you.")
                pyautogui.hotkey('win', 'd')
                webbrowser.open("https://www.geeksforgeeks.org/")

            elif "im bored" in query or "bored" in query:
                speak("I've got just the thing to cheer you up! Let's hear some music!")
                webbrowser.open("https://www.youtube.com/watch?v=pRpeEdMmmQ0")

            # --- PRIORITY 4: SHUTDOWN ---
            elif "goodbye" in query or "exit" in query or "sleep" in query:
                speak("Going back to sleep. Just say my name if you need me again!")
                # This doesn't stop the code, it just exits the 'Active' loop

            elif "turn off" in query:
                speak("Powering down completely. Have a great day, boss!")
                break

            # --- PRIORITY 5: THE AI BRAIN (Default / Fallback) ---
            elif query != "none":
                ai_response = ask_brain(query)
                speak(ai_response)