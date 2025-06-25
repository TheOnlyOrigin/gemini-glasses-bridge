import os
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import time

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    print("CRITICAL: GEMINI_API_KEY not found in environment.")
    exit()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen_for_audio_from_glasses():
    print("\n[GLASSES SIM] Listening for your voice...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return audio_data
        except sr.WaitTimeoutError:
            print("[GLASSES SIM] Listening timed out. No speech detected.")
            return None

def transcribe_audio_to_text(audio_data):
    if audio_data is None:
        return None
    print("[PHONE] Transcribing audio...")
    try:
        text_query = recognizer.recognize_google(audio_data)
        print(f"[PHONE] You said: '{text_query}'")
        return text_query
    except sr.UnknownValueError:
        print("[PHONE] Transcription failed: Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"[PHONE] Transcription service error: {e}")
        return "Error with the transcription service."

def query_gemini_model(text_query):
    if not text_query:
        return "I didn't receive a query."
    print(f"[CLOUD] Sending to Gemini: '{text_query}'")
    try:
        response = model.generate_content(text_query)
        time.sleep(1)
        print("[CLOUD] Received response from Gemini.")
        return response.text
    except Exception as e:
        print(f"[CLOUD] Gemini API Error: {e}")
        return "I'm having trouble connecting to my AI model right now."

def stream_response_to_glasses(text_response):
    print(f"\n[GLASSES SIM] Speaking response: '{text_response}'")
    tts_engine.say(text_response)
    tts_engine.runAndWait()
    print("[GLASSES SIM] Finished speaking.")

def main():
    print("--- Gemini Glasses Bridge Initialized ---")
    print("Say something into your microphone to begin.")
    while True:
        captured_audio = listen_for_audio_from_glasses()
        if captured_audio:
            user_query = transcribe_audio_to_text(captured_audio)
            if user_query:
                gemini_response = query_gemini_model(user_query)
                stream_response_to_glasses(gemini_response)

if __name__ == "__main__":
    main()
