import speech_recognition as sr
import moviepy.editor as mp
import os


# Define the base path starting from the root directory. E.g. '\'
base_path = os.path.join(os.path.sep)

# Construct the data path starting from the root directory
data_path = os.path.join(base_path, 'data')

video_path = os.path.join(data_path, 'video.mp4')
audio_path = os.path.join(data_path, 'audio.wav')
transcription_path = os.path.join(data_path, 'transcription.txt')


video = mp.VideoFileClip(video_path)
print('Video loaded: ', video_path)


video.audio.write_audiofile(
    audio_path,
    codec='pcm_s16le', # 'pcm_s16le' -> 16-bit / 'pcm_s32le' -> 32-bit wav
    bitrate='64k',
    fps=16000)
print('Audio extracted: ', audio_path)


file_audio = sr.AudioFile(audio_path)
print('Audio file loaded', audio_path)


# Use the audio file as the audio source
r = sr.Recognizer()

with file_audio as source:
    audio = r.record(source)
    text = r.recognize_google(audio)


print('Text extracted from audio:\n\n')
print(text)


file = open(transcription_path, 'w')
file.write(text)
file.close()
