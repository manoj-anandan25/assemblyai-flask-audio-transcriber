
# 🎙 AssemblyAI Flask Audio Transcriber

A simple **Flask web app** that allows users to upload an `.mp3` or `.wav` file and get the **transcribed text** using the **AssemblyAI API**.  

---

##  Features
- Upload `.mp3` or `.wav` audio files
- Automatic transcription using [AssemblyAI](https://www.assemblyai.com/)
- Simple web interface with Flask
- Easy to set up and run (no technical knowledge required)

---

##  Project Structure
```

assemblyai-flask-audio-transcriber/
│── app.py                # Main Flask app
│── sdk.py                # SDK wrapper for developers
│── requirements.txt      # Dependencies
│── templates/
│    └── index.html       # Upload form + display transcript

````

---

## Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/assemblyai-flask-audio-transcriber.git
cd assemblyai-flask-audio-transcriber
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add your API Key

Open `app.py` and replace:

```python
API_KEY = "YOUR_ASSEMBLYAI_API_KEY"
```

👉 Get your key from [AssemblyAI Dashboard](https://www.assemblyai.com/).

---

## Running the App

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

* Upload an `.mp3` or `.wav` file
* Wait a few seconds 
* See the transcription result 

---

##  SDK Usage (Optional for Developers)

Instead of using the web interface, developers can use the included `sdk.py`:

```python
from sdk import AudioTranscriber

API_KEY = "YOUR_ASSEMBLYAI_API_KEY"

transcriber = AudioTranscriber(API_KEY)
text = transcriber.transcribe("sample.mp3")
print("Transcript:", text)
```

---

##  Error Handling

*  **"No file uploaded"** → You didn’t select any file.
*  **"No selected file"** → File field is empty.
* **AssemblyAI error** → API key is invalid or request failed.
*  **Timeout** → If the audio is too long, polling may take several minutes.

---

##📺 Demo Video

👉 You can watch a step-by-step setup & execution video here:
🔗 [AssemblyAI Flask Transcriber Demo (YouTube)](https://youtu.be/a0py8Ps__y4)

---
## 🖼️ Output

Here is an example of the transcription result after uploading an MP3/WAV file:

![App Output](<img width="1530" height="903" alt="image" src="https://github.com/user-attachments/assets/915fff4e-d041-430f-a3b6-05c42ca2d0bb" />)


✅ With this setup, even a **non-technical user** can:

* Install → Run → Upload audio → Get transcription
* Watch the YouTube demo for execution
* Developers can directly use `sdk.py`

---
