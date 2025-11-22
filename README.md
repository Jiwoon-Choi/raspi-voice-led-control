# Voice-Controlled LED System on Raspberry Pi 5

This project demonstrates a simple **voice-controlled hardware system** using a **Raspberry Pi 5**, **Python**, **speech recognition**, and **GPIO LED control**.

I built this project to explore the integration of **automatic speech interfaces** with **embedded systems**, which is a foundational technique in robotics, human–robot interaction (HRI), and voice-control systems.

---

## Overview

Using the `speech_recognition` library and a USB microphone, the Raspberry Pi listens for voice commands such as:

- `red`
- `green`
- `blue`
- `off`

When the Pi detects a valid command, it controls three physical LEDs via the GPIO pins using the `gpiozero` library.

---

## Features

- Real-time speech-to-text using the Google Web Speech API  
- Ambient noise adjustment  
- Timeout handling for silence  
- LED control using GPIO pins  
- Modular design: one script for STT, one for LED control logic  
- A demonstration video showing live voice control

---

## Project Structure

```text
voice_led_control/
├── transcribe.py # Handles microphone input + speech recognition (speech-to-text)
├── voice_led_control.py # Parses voice commands & turns RGB LEDs on/off
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

## Demo Video

**Uploaded on YouTube (Unlisted)**  
- Video link: https://youtu.be/En7OnufQjQ4

---

## Hardware Used

- Raspberry Pi 5  
- USB microphone  
- Breadboard  
- 3 LEDs: red, green, blue  
- Resistors (220Ω)  
- M/F Jumper wires

---

## How to Run

### 1. Clone this repository on your Raspberry Pi:
```bash
git clone https://github.com/Jiwoon-Choi/raspi-voice-led-control.git
cd raspi-voice-led-control
```

### 2. Prerequisites (system-level installation)

Before installing Python dependencies, make sure necessary system packages are installed on your Raspberry Pi.

1. Update package lists
```bash
sudo apt update
```

2. Install audio-related system libraries
```bash
sudo apt install portaudio19-dev flac
```

* portaudio19-dev: Required for PyAudio to capture microphone input

* flac: Required by SpeechRecognition to convert audio to FLAC before sending to Google STT

Once these are installed, you can proceed with installing Python dependencies.

### 3. Install required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Prepare your hardware setup:
Make sure the following components are connected properly:
- USB microphone connected to the Raspberry Pi
- Red, Green, and Blue LEDs wired to the correct GPIO pins
- Appropriate resistors in series with the LEDs
- GPIO interface enabled on the Raspberry Pi
- Internet connection available (required for Google STT)

(Note: The project is designed to run on Raspberry Pi OS with Python 3.10+)

### 5. Run the program:
```bash
python voice_led_control.py
```

### 6. Speak one of the supported voice commands:
- "red"
- "green"
- "blue"
- "off"

If recognized successfully, the corresponding LED will light up or turn off.
