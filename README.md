# Gemini Glasses Bridge (Fairphone/Android Bluetooth Proxy Edition)

## Overview
This project allows a rooted Android device (e.g. Fairphone) to act as a Bluetooth proxy—using your Meta (Ray-Ban) smart glasses as a wireless front-end for Google's Gemini AI.

- **Speech → Gemini → Speech**: Speak into your glasses, get an AI response read back to you.
- **Runs on your Android (rooted recommended)**, using Python.

## Setup

### 1. Install dependencies

Make sure you have Python 3.8+ and pip.  
Install system dependencies if needed (for PyAudio):

```bash
apt update
apt install -y portaudio19-dev# gemini-glasses-bridge

On Android, use Termux:
bash

pkg install python
pip install wheel
pip install --upgrade pip

Install Python requirements:
bash

pip install -r requirements.txt

2. Set up your Gemini API key

Export your Gemini API key as an environment variable:
bash

export GEMINI_API_KEY=your-gemini-api-key

Or add it to your ~/.bashrc or ~/.profile for persistence.
3. Pair your Meta glasses

    Use Android Bluetooth settings to pair your Meta (Ray-Ban) glasses as a headset.
    Set them as the default input/output audio device.

4. Run the script
bash

python main.py

Talk into your glasses and hear Gemini's response!
Notes

    Requires root for persistent and background audio routing on Android.
    pyttsx3 and SpeechRecognition are cross-platform, but their backend may vary.
    For full automation, consider using Tasker or Termux:Boot.

Troubleshooting

If you have audio routing issues:

    Use an audio router app, or
    Modify audio_policy.conf for system-wide routing (root required).

If you get "PyAudio not found", install portaudio with your package manager.
Advanced

Want to automate everything? Use Tasker or Termux background scripts to launch this on boot. Root allows you to force audio routing even when the device is locked or idle.
