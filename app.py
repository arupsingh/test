from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the POST request contains a file
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Read the audio file
    audio = recognizer.record(file)

    try:
        # Use the recognizer to convert speech to text
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return 'Could not understand audio'
    except sr.RequestError as e:
        return 'Error: {}'.format(e)

if __name__ == '__main__':
    app.run(debug=True)
