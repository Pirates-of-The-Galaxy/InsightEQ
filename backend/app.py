from roboflow import Roboflow
from moviepy.editor import VideoFileClip
from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import nltk
nltk.download('vader_lexicon')
import speech_recognition as sr
from nltk.sentiment import SentimentIntensityAnalyzer


rf = Roboflow(api_key="LF4lxbBefvMh8W3awrgv")
project = rf.workspace().project("face-emotion-s9kw9")
model = project.version("1").model

project2 = rf.workspace().project("dress-model-gknib")
model2 = project.version("1").model

def analyze_sentiment(audio_file):  
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

        sid = SentimentIntensityAnalyzer()
        sentiment_score = sid.polarity_scores(text)['compound']

        threshold = 0.5

        if sentiment_score >= threshold:
            classification = "formal"
        else:
             classification = "informal"

        return classification
    
def analyze_stutter(audio):

    audio_duration = len(audio)
    stutter_count = 0
    stutter_threshold = 0.3  # You may need to adjust this based on your analysis

    words = audio.split()  # Using 'audio.text' to access the transcribed text
    expected_word_duration = audio_duration / len(words)

    for word in words:
        actual_word_duration = len(word) * expected_word_duration / len(audio)
        if abs(actual_word_duration - expected_word_duration) > stutter_threshold:
            stutter_count += 1

    if stutter_count > 0:
        return f"Stuttering detected with {stutter_count} instances."
    else:
        return "No stuttering detected."