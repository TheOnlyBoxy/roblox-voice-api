from flask import Flask, request, jsonify
import speech_recognition as sr
import urllib.request
import os

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        data = request.json
        audio_url = data.get('audio')
        
        # Download the audio from Roblox
        audio_path = "/tmp/audio.wav"
        urllib.request.urlretrieve(audio_url, audio_path)
        
        # Transcribe it
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
        
        return jsonify({"success": True, "text": text})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/')
def home():
    return "Voice API is running!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
