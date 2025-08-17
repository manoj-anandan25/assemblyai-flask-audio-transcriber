import requests
import time
import os

class AudioTranscriber:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"authorization": self.api_key}
        self.upload_endpoint = "https://api.assemblyai.com/v2/upload"
        self.transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

    def _read_file(self, file_path, chunk_size=5242880):
        with open(file_path, "rb") as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                yield data

    def upload(self, file_path):
        response = requests.post(
            self.upload_endpoint,
            headers=self.headers,
            data=self._read_file(file_path)
        )
        return response.json()["upload_url"]

    def start_transcription(self, audio_url):
        response = requests.post(
            self.transcript_endpoint,
            json={"audio_url": audio_url},
            headers=self.headers
        )
        return response.json()["id"]

    def poll(self, transcript_id):
        polling_endpoint = f"{self.transcript_endpoint}/{transcript_id}"
        while True:
            response = requests.get(polling_endpoint, headers=self.headers).json()
            if response["status"] == "completed":
                return response["text"]
            elif response["status"] == "error":
                return "Error: " + response["error"]
            time.sleep(3)

    def transcribe(self, file_path):
        audio_url = self.upload(file_path)
        transcript_id = self.start_transcription(audio_url)
        return self.poll(transcript_id)
