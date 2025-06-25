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
