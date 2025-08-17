from flask import Flask, request, render_template, redirect, url_for
import requests
import time
import os

app = Flask(__name__)

# ✅ Replace with your real AssemblyAI API key
API_KEY = "add_your_api_key"
UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
TRANSCRIPT_ENDPOINT = "https://api.assemblyai.com/v2/transcript"

headers = {"authorization": API_KEY}

def upload_file(file_path):
    """Upload local file (mp3, wav, etc.) to AssemblyAI"""
    with open(file_path, "rb") as f:
        response = requests.post(
            UPLOAD_ENDPOINT,
            headers=headers,
            data=f
        )
    response_json = response.json()
    return response_json["upload_url"]

def transcribe(audio_url):
    """Send request to transcribe"""
    transcript_request = {"audio_url": audio_url}
    response = requests.post(
        TRANSCRIPT_ENDPOINT,
        json=transcript_request,
        headers=headers
    )
    return response.json()["id"]

def poll_transcription(transcript_id):
    """Check status until transcription is complete"""
    polling_endpoint = TRANSCRIPT_ENDPOINT + "/" + transcript_id
    while True:
        response = requests.get(polling_endpoint, headers=headers)
        result = response.json()

        if result["status"] == "completed":
            return result["text"]
        elif result["status"] == "error":
            return "❌ Error: " + result["error"]
        time.sleep(3)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript_text = None
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded"

        file = request.files["file"]
        if file.filename == "":
            return "No selected file"

        # Save temporarily
        filepath = os.path.join("temp_" + file.filename)
        file.save(filepath)

        # Upload → Transcribe → Poll
        audio_url = upload_file(filepath)
        transcript_id = transcribe(audio_url)
        transcript_text = poll_transcription(transcript_id)

        os.remove(filepath)  # cleanup temp file

    return render_template("index.html", transcript=transcript_text)

if __name__ == "__main__":
    app.run(debug=True)
