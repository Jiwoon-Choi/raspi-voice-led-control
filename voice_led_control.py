import speech_recognition as sr

MIC_INDEX = 0
r = sr.Recognizer()

from gpiozero import LED

greenLed = LED(16)
blueLed = LED(20)
redLed = LED(21)

try:
    while True:
        with sr.Microphone(device_index=MIC_INDEX) as source:
            print("\n[1] Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            
            print("[2] Say something! (you have ~10 seconds)")
            try:
                r.pause_threshold = 3.0
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("[!] No speech detected within 10 seconds, trying again...")
                continue
        
        print("[3] Got audio, sending to Google...")
        
        try:
            text = r.recognize_google(audio, language='en-US')
            print("[4] You said:", text)
            
            text_lower = text.lower()
            
            if "red" in text_lower:
                print("-> Setting RED")
                greenLed.value = 0
                blueLed.value = 0
                redLed.value = 1
            elif "blue" in text_lower:
                print("-> Setting BLUE")
                greenLed.value = 0
                blueLed.value = 1
                redLed.value = 0
            elif "green" in text_lower:
                print("-> Setting GREEN")
                greenLed.value = 1
                blueLed.value = 0
                redLed.value = 0
            elif "off" in text_lower:
                print("-> Turning all OFF")
                greenLed.value = 0
                blueLed.value = 0
                redLed.value = 0
                
        except sr.UnknownValueError:
            print("[!] Google Speech Recognition could not understand audio")
            
        except sr.RequestError as e:
            print("[!] Could not request results from Google; {0}".format(e))

except KeyboardInterrupt:
    print("\nKeyboardInterrupt received. Exiting.")