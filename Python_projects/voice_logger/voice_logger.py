import pyttsx3

engine = pyttsx3.init()
all_voices = engine.getProperty("voices")

print(f"Total voices found: {len(all_voices)}")

if len(all_voices) > 0:
    engine.setProperty("voice", all_voices[0].id)

engine.setProperty("rate", 150)
def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("All systems are functional.")
print("\nAvailable voices:")
for index, v in enumerate(all_voices):
    print(f"{index}: {v.name}"
