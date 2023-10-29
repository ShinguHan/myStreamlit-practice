import streamlit as st
from pydub import AudioSegment, silence
import pathlib
import logging
import speech_recognition as sr

recog = sr.Recognizer()

# l = logging.getLogger("pydub.converter")
# l.setLevel(logging.DEBUG)
# l.addHandler(logging.StreamHandler())


st.title("Audio to Text")

audio = st.file_uploader("Upload Your File", type=["m4a", "mp3", "wav"])
if audio:
    segments = AudioSegment.from_file(audio)
    chunks = silence.split_on_silence(segments, min_silence_len=500, silence_thresh=-20, keep_silence=100)
    for index, chunk in enumerate(chunks):
        chunk.export(str(index)+".wav",format="wav")

        with sr.AudioFile(str(index)+".wav") as source:
            recorded = recog.record(audio)
            print(recorded)
            try:
                text = recog.recognize_google(recorded, language = "en-US")
                print(text)
            except:
                print("None")
        

# import speech_recognition as sr

# # obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
# 	print("Say something!")
# 	audio = r.listen(source)

# # recognize speech using Google Speech Recognition
# try:
# 	# for testing purposes, we're just using the default API key
# 	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# 	# instead of `r.recognize_google(audio)`
# 	print("Google Speech Recognition thinks you said in English: -  " + r.recognize_google(audio, language = "en-US"))
# 	print("Google Speech Recognition thinks you said in Turkish: -  " + r.recognize_google(audio, language = "tr-TR"))
# except sr.UnknownValueError:
# 	print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
# 	print("Could not request results from Google Speech Recognition service; {0}".format(e))